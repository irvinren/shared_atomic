'''
Created on 29 Mar 2022

@author: philren
'''
import pytest
from multiprocessing import Value, Process
from threading import Thread
from threading import RLock as ThreadLock

import ctypes
import re
import sys
from shared_atomic import loaddll
from shared_atomic import loadffiddl
from shared_atomic import sharable64


import random

atomic = None
atomicffi, lib = None, None

if sys.platform in ('linux','darwin'):
    types = ('ctypes.c_bool',
             'ctypes.c_wchar',
             'ctypes.c_byte',
             'ctypes.c_ubyte',
             'ctypes.c_short',
             'ctypes.c_ushort',
             'ctypes.c_int',
             'ctypes.c_uint',
             'ctypes.c_long',
             'ctypes.c_ulong',
             'ctypes.c_longlong',
             'ctypes.c_ulonglong',
             'ctypes.c_size_t',
             'ctypes.c_ssize_t',
             'ctypes.c_float',
             'ctypes.c_double',
             'ctypes.c_longdouble')

    inlist = (False,
              '国',
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              )

    exlist = (True,
              '中',
              127,
              255,
              2 ** 15 - 1,
              2 ** 16 - 1,
              2 ** 31 - 1,
              2 ** 32 - 1,
              2 ** 63 - 1,
              2 ** 64 - 1,
              2 ** 63 - 1,
              2 ** 64 - 1,
              2 ** 64 - 1,
              2 ** 63 - 1,
              2.0 ** 30 - 1,
              2.0 ** 63 - 1,
              2.0 ** 63 - 1,
              )
    sublist = (True,
               '之',
               100,
               100,
               100,
               100,
               100,
               100,
               100,
               100,
               100,
               100,
               100,
               100,
               )

elif sys.platform == 'win32':
    types = ('ctypes.c_bool',
             'ctypes.c_wchar',
             'ctypes.c_byte',
             'ctypes.c_ubyte',
             'ctypes.c_short',
             'ctypes.c_ushort',
             'ctypes.c_int',
             'ctypes.c_uint',
             'ctypes.c_long',
             'ctypes.c_ulong',
             'ctypes.c_longlong',
             'ctypes.c_ulonglong',
             'ctypes.c_size_t',
             'ctypes.c_ssize_t',
             'ctypes.c_float',
             'ctypes.c_double',
             'ctypes.c_longdouble')
    inlist = (False,
              '国',
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              )

    exlist = (True,
              '中',
              127,
              255,
              2 ** 15 - 1,
              2 ** 16 - 1,
              2 ** 31 - 1,
              2 ** 32 - 1,
              2 ** 31 - 1,
              2 ** 32 - 1,
              2 ** 63 - 1,
              2 ** 64 - 1,
              2 ** 64 - 1,
              2 ** 63 - 1,
              2.0 ** 30 - 1,
              2.0 ** 63 - 1,
              2.0 ** 63 - 1,
              )
    sublist = (True,
               '之',
               100,
               100,
               100,
               100,
               100,
               100,
               100,
               100,
               100,
               100,
               100,
               100,
               )

addlist = sublist

r = random.Random()

andlist = []
orlist = []
xorlist = []
nandlist = []

for i in range(len(types)):
    andlist.append(r.randrange(0, 128))
    orlist.append(r.randrange(0, 128))
    xorlist.append(r.randrange(0, 128))
    nandlist.append(r.randrange(0, 128))

def setup_function():
    """
    pre function for pytest
    :return: None
    """
    global atomic, atomicffi, lib
    # if sys.platform in ('darwin','linux'):
    #     dlltype = ctypes.CDLL
    #     os.chdir('/Users/philren/.local/share/virtualenvs/spark-examples--HrH57AW/lib/python3.6/site-packages')
    #     filename = 'shared_atomic.cpython-36m-darwin.so'
    # elif sys.platform == "win32":
    #     dlltype = ctypes.windll
    # else:
    #     return
    #atomic = ctypes.LibraryLoader(dlltype).LoadLibrary(filename)


    atomic = loaddll()
    atomicffi, lib = loadffiddl()

def teardown_function():
    """
    post function for pytest
    :return: None
    """
    global atomic
    atomic = None

def signed2unsigned(type, input):

    if type in ('ctypes.c_ubyte',
                'ctypes.c_ushort',
                'ctypes.c_uint',
                'ctypes.c_ulong',
                'ctypes.c_ulonglong',
                'ctypes.c_size_t'):
        if input < 0:
            return input + 2**(ctypes.sizeof(eval(type))*8)
        return input
    else:
        return input

def test_value_atomic():
    """
    test single process single thread
    :return: None
    """
    i = 0
    result = None
    try:
        for type in types:
            result=[]
            t=[]
            exec('t.append(' + type + ')')
            a = Value(t[0], lock=False)
            aref = ctypes.byref(a, 0)
            typetext=re.findall("c_.*", type)[0][2:]
            functext = typetext

            if type == 'ctypes.c_wchar':
                exec('init = ctypes.c_'+typetext+"('" + f'{inlist[i]}' + "')")
                exec('atomic.'+functext+'_store(aref,ctypes.byref(init))')
                assert a.value == inlist[i]
                exec('result.append(atomic.' + functext + '_get_and_set(aref,ctypes.c_' + typetext + "('" + f'{exlist[i]}' + "')))")
                #result[-1] = int.to_bytes(result[-1], ctypes.sizeof(ctypes.c_wchar), byteorder=sys.byteorder).decode('utf-16-be')[0:-1]
                assert result[-1] == inlist[i]
                assert a.value == exlist[i]
                c = []
                exec('c.append(ctypes.c_' + typetext + "('" + f'{exlist[i]}' + "'))")
                exec('result.append(atomic.' + functext + '_compare_and_set(aref,ctypes.byref(c[-1]),ctypes.c_' + typetext + "('" + f'{inlist[i]}' + "')))")
                assert result[-1]
                assert a.value == inlist[i]
                exec('c.append(ctypes.c_' + typetext + '("' + f'{inlist[i]}' + '"))')
                exec('c.append(ctypes.c_' + typetext + '("' + f'{exlist[i]}' + '"))')
                exec('result.append(atomic.' + functext + '_shift(aref, ctypes.byref(c[-1]), ctypes.byref(c[-2])))')
                assert c[-1].value == a.value
                assert c[-2].value == inlist[i]
                exec('result.append(atomic.'+functext+'_add_and_fetch(aref,ctypes.c_'+typetext+"('" + f'{addlist[i]}' + "')))")
                #result[-1] = int.to_bytes(result[-1], ctypes.sizeof(ctypes.c_wchar), byteorder=sys.byteorder).decode('utf-16-be')[0:-1]
                assert result[-1] == int.to_bytes(
                       int.from_bytes(exlist[i].encode("utf-16-be"), byteorder='big') + \
                       int.from_bytes(addlist[i].encode("utf-16-be"), byteorder='big'),
                       length=4,
                       byteorder='big',
                ).decode(encoding='utf-16-be')[1:]
                assert a.value == result[-1]
                print(result[-1])
                exec('result.append(atomic.'+functext+'_sub_and_fetch(aref,ctypes.c_'+typetext+"('" + f'{addlist[i]}' + "')))")
                #result[-1] = int.to_bytes(result[-1], ctypes.sizeof(ctypes.c_wchar), byteorder=sys.byteorder).decode('utf-16-be')[0:-1]
                assert result[-1] == exlist[i]
                assert a.value == result[-1]
                print(result[-1])
                exec('result.append(atomic.'+functext+'_fetch_and_add(aref,ctypes.c_'+typetext+"('" + f'{addlist[i]}' + "')))")
                #result[-1] = int.to_bytes(result[-1], ctypes.sizeof(ctypes.c_wchar), byteorder=sys.byteorder).decode('utf-16-be')[0:-1]
                assert result[-1] == exlist[i]
                assert a.value == int.to_bytes(
                       int.from_bytes(exlist[i].encode("utf-16-be"), byteorder='big') + \
                       int.from_bytes(addlist[i].encode("utf-16-be"), byteorder='big'),
                       length=4,
                       byteorder='big',
                ).decode(encoding='utf-16-be')[1:]
                print(result[-1])
                exec('result.append(atomic.'+functext+'_fetch_and_sub(aref,ctypes.c_'+typetext+"('" + f'{addlist[i]}' + "')))")
                #result[-1] = int.to_bytes(result[-1], ctypes.sizeof(ctypes.c_wchar), byteorder=sys.byteorder).decode('utf-16-be')[0:-1]
                assert result[-1] == int.to_bytes(
                       int.from_bytes(exlist[i].encode("utf-16-be"), byteorder='big') + \
                       int.from_bytes(addlist[i].encode("utf-16-be"), byteorder='big'),
                       length=4,
                       byteorder='big',
                ).decode(encoding='utf-16-be')[1:]
                print(result[-1])
                assert a.value == exlist[i]

            else:
                exec('init = ctypes.c_'+typetext+"(" + f'{inlist[i]}' + ")")
                exec('atomic.'+functext+'_store(aref,ctypes.byref(init))')
                assert a.value == inlist[i]
                if type not in ('ctypes.c_float', 'ctypes.c_double', 'ctypes.c_longdouble'):
                    exec('result.append(atomic.'+functext+'_get_and_set(aref,ctypes.c_'+typetext+"(" + f'{exlist[i]}' + ")))")
                    assert result[-1] == inlist[i]
                    assert a.value == exlist[i]
                    c=[]
                    exec('c.append(ctypes.c_'+typetext+'('+f'{exlist[i]}'+'))')
                    exec('result.append(atomic.'+functext+'_compare_and_set(aref,ctypes.byref(c[-1]),ctypes.c_'+typetext+"(" + f'{inlist[i]}' + ")))")
                    assert result[-1]
                    assert a.value == inlist[i]
                    exec('c.append(ctypes.c_'+typetext+'('+f'{inlist[i]}'+'))')
                    exec('c.append(ctypes.c_'+typetext+'('+f'{exlist[i]}'+'))')
                    exec('result.append(atomic.'+functext+'_shift(aref, ctypes.byref(c[-1]), ctypes.byref(c[-2])))')
                    assert c[-1].value == a.value
                    assert c[-2].value == inlist[i]
                if type not in ('ctypes.c_bool', 'ctypes.c_float', 'ctypes.c_double', 'ctypes.c_longdouble'):
                    exec('result.append(atomic.'+functext+'_sub_and_fetch(aref,ctypes.c_'+typetext+"(" + f'{sublist[i]}' + ")))")
                    assert result[-1] == exlist[i] - addlist[i]
                    assert a.value == result[-1]
                    exec('result.append(atomic.'+functext+'_add_and_fetch(aref,ctypes.c_'+typetext+"(" + f'{addlist[i]}' + ")))")
                    assert result[-1] == exlist[i]
                    assert a.value == result[-1]
                    exec('result.append(atomic.'+functext+'_and_and_fetch(aref,ctypes.c_'+typetext+"(" + f'{andlist[i]}' + ")))")
                    assert result[-1] == signed2unsigned(type,exlist[i] & andlist[i])
                    assert a.value == result[-1]
                    exec('result.append(atomic.'+functext+'_or_and_fetch(aref,ctypes.c_'+typetext+"(" + f'{orlist[i]}' + ")))")
                    assert result[-1] == signed2unsigned(type,(exlist[i] & andlist[i]) | orlist[i])
                    assert a.value == result[-1]
                    exec('result.append(atomic.'+functext+'_xor_and_fetch(aref,ctypes.c_'+typetext+"(" + f'{xorlist[i]}' + ")))")
                    assert result[-1] == signed2unsigned(type,((exlist[i] & andlist[i]) | orlist[i]) ^ xorlist[i])
                    assert a.value == result[-1]
                    exec('result.append(atomic.'+functext+'_nand_and_fetch(aref,ctypes.c_'+typetext+"(" + f'{nandlist[i]}' + ")))")
                    assert result[-1] == signed2unsigned(type,~((((exlist[i] & andlist[i]) | orlist[i]) ^ xorlist[i]) & nandlist[i]))
                    assert a.value == result[-1]
                    exec('init = ctypes.c_' + typetext + "(" + f'{exlist[i]}' + ")")
                    exec('atomic.' + functext + '_store(aref,ctypes.byref(init))')
                    exec('result.append(atomic.'+functext+'_fetch_and_sub(aref,ctypes.c_'+typetext+"(" + f'{sublist[i]}' + ")))")
                    assert result[-1] == exlist[i]
                    assert a.value == exlist[i] - sublist[i]
                    exec('result.append(atomic.'+functext+'_fetch_and_add(aref,ctypes.c_'+typetext+"(" + f'{addlist[i]}' + ")))")
                    assert result[-1] == exlist[i] - sublist[i]
                    assert a.value == exlist[i]
                    exec('result.append(atomic.'+functext+'_fetch_and_and(aref,ctypes.c_'+typetext+"(" + f'{andlist[i]}' + ")))")
                    assert result[-1] == exlist[i]
                    assert a.value == signed2unsigned(type,result[-1] & andlist[i])
                    exec('result.append(atomic.'+functext+'_fetch_and_or(aref,ctypes.c_'+typetext+"(" + f'{orlist[i]}' + ")))")
                    assert result[-1] == exlist[i] & andlist[i]
                    assert a.value == signed2unsigned(type,(exlist[i] & andlist[i]) | orlist[i])
                    exec('result.append(atomic.'+functext+'_fetch_and_xor(aref,ctypes.c_'+typetext+"(" + f'{xorlist[i]}' + ")))")
                    assert result[-1] == (exlist[i] & andlist[i]) | orlist[i]
                    assert a.value == signed2unsigned(type,((exlist[i] & andlist[i]) | orlist[i]) ^ xorlist[i])
                    exec('result.append(atomic.'+functext+'_fetch_and_nand(aref,ctypes.c_'+typetext+"(" + f'{nandlist[i]}' + ")))")
                    assert result[-1] == ((exlist[i] & andlist[i]) | orlist[i]) ^ xorlist[i]
                    assert a.value == signed2unsigned(type,~((((exlist[i] & andlist[i]) | orlist[i]) ^ xorlist[i]) & nandlist[i]))

            i += 1
    except Exception as e:
        print(e)
        print(type, typetext)
        raise e


def test_thread_atomic():
    """
    test single process multiple threads
    :return: None
    """
    #v = sharable64(2 ** 63 - 1)

    a = atomicffi.new("long long *",1)
    a[0] = 2 ** 63 - 1

    def thread_atomic_run(b):
        for j in range(1000):
            lib.longlong_sub_and_fetch(b,100)


    threadlist=[]

    for i in range(10000):
        threadlist.append(Thread(target=thread_atomic_run, args=(a, )))

    for i in range(10000):
        threadlist[i].start()

    for i in range(10000):
        threadlist[i].join()

    assert a[0] == 2 ** 63 - 1 - 100 * 1000 * 10000


def test_thread_native_atomic():
    """
    test single process multiple threads
    :return: None
    """
    v = 2 ** 63 - 1

    threadlist = []
    lock = ThreadLock()

    def thread_native_run():
        nonlocal lock
        nonlocal v
        for j in range(1000):
            lock.acquire()
            v -= 100
            lock.release()

    for i in range(10000):
        threadlist.append(Thread(target=thread_native_run))

    for i in range(10000):
        threadlist[i].start()

    for i in range(10000):
        threadlist[i].join()

    assert v == 2 ** 63 - 1 - 100 * 1000 * 10000

if sys.platform in ('linux','darwin'):
    def test_processing_atomic():
        """
        test multiple process
        :return: None
        """
        a = sharable64(2 ** 63 - 1)

        def process_run(reference):
            for i in range(1000):
                lib.longlong_sub_and_fetch(reference, 100)

        processlist = []
        for i in range(10000):
            processlist.append(Process(target=process_run, args=(a.reference,)))

        for i in range(10000):
            processlist[i].start()

        for i in range(10000):
            processlist[i].join()

        assert a.get() == 2 ** 63 - 1 - 100 * 1000 * 10000

    def test_processing_native_atomic():
        """
        test multiple process
        :return: None
        """

        v = Value(ctypes.c_size_t, 2 ** 63 - 1, lock=True)

        def process_native_run():
            nonlocal v
            for i in range(1000):
                with v.get_lock():
                    v.value -= 100

        processlist = []
        for i in range(10000):
            processlist.append(Process(target=process_native_run))

        for i in range(10000):
            processlist[i].start()

        for i in range(10000):
            processlist[i].join()

        assert v.value == 2 ** 63 - 1 - 100 * 1000 * 10000


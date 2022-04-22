'''
Created on 29 Mar 2022

@author: philren
'''
import pytest
from multiprocessing import Value, Process
from threading import Thread
import ctypes
import os
import re
import sys
from shared_atomic import loaddll

atomic = None
types = (ctypes.c_bool,
         ctypes.c_wchar,
         ctypes.c_byte,
         ctypes.c_ubyte,
         ctypes.c_short,
         ctypes.c_ushort,
         ctypes.c_int,
         ctypes.c_uint,
         ctypes.c_long,
         ctypes.c_ulong,
         ctypes.c_longlong,
         ctypes.c_ulonglong,
         ctypes.c_size_t,
         ctypes.c_ssize_t,
         ctypes.c_float,
         ctypes.c_double,
         ctypes.c_longdouble)
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
addlist = sublist

def setup_function():
    global atomic
    # if sys.platform in ('darwin','linux'):
    #     dlltype = ctypes.CDLL
    #     os.chdir('/Users/philren/.local/share/virtualenvs/spark-examples--HrH57AW/lib/python3.6/site-packages')
    #     filename = 'shared_atomic.cpython-36m-darwin.so'
    # elif sys.platform == "win32":
    #     dlltype = ctypes.windll
    # else:
    #     return
    #atomic = ctypes.LibraryLoader(dlltype).LoadLibrary(filename)


    atomic=loaddll()

def teardown_function():
    global atomic
    atomic = None

def test_atomic():
    """
    test single process single thread
    :return: None
    """
    i = 0
    result=None
    try:
        for type in types:
            result=[]
            a = Value(type, lock=False)
            aref = ctypes.byref(a, 0)
            typetext=re.findall('c_.*', re.findall("'.*'", f'{type}')[0])[0][2:-1]
            functext = typetext

            if type == ctypes.c_wchar:
                exec('init = ctypes.c_'+typetext+"('" + f'{inlist[i]}' + "')")
                exec('atomic.'+functext+'_store(aref,ctypes.byref(init))')
                assert a.value == inlist[i]
                exec('result.append(atomic.' + functext + '_get_and_set(aref,ctypes.c_' + typetext + "('" + f'{exlist[i]}' + "')))")
                result[-1] = int.to_bytes(result[-1], ctypes.sizeof(ctypes.c_wchar), byteorder=sys.byteorder).decode('utf-16-le')[0:-1]
                assert result[-1] == inlist[i]
                assert a.value == exlist[i]
                exec('result.append(atomic.'+functext+'_add_and_fetch(aref,ctypes.c_'+typetext+"('" + f'{addlist[i]}' + "')))")
                result[-1] = int.to_bytes(result[-1], ctypes.sizeof(ctypes.c_wchar), byteorder=sys.byteorder).decode('utf-16-le')[0:-1]
                assert result[-1] == int.to_bytes(
                       int.from_bytes(exlist[i].encode("utf-16-le"), byteorder=sys.byteorder) + \
                       int.from_bytes(addlist[i].encode("utf-16-le"), byteorder=sys.byteorder),
                       length=ctypes.sizeof(ctypes.c_wchar),
                       byteorder=sys.byteorder,
                ).decode(encoding='utf-16-le')[0:-1]
                assert a.value == result[-1]
                exec('result.append(atomic.'+functext+'_sub_and_fetch(aref,ctypes.c_'+typetext+"('" + f'{addlist[i]}' + "')))")
                result[-1] = int.to_bytes(result[-1], ctypes.sizeof(ctypes.c_wchar), byteorder=sys.byteorder).decode('utf-16-le')[0:-1]
                assert result[-1] == exlist[i]
                assert a.value == result[-1]
            else:
                exec('init = ctypes.c_'+typetext+"(" + f'{inlist[i]}' + ")")
                exec('atomic.'+functext+'_store(aref,ctypes.byref(init))')
                assert a.value == inlist[i]
                if type not in (ctypes.c_float, ctypes.c_double, ctypes.c_longdouble):
                    exec('result.append(atomic.'+functext+'_get_and_set(aref,ctypes.c_'+typetext+"(" + f'{exlist[i]}' + ")))")
                    assert result[-1] == inlist[i]
                    assert a.value == exlist[i]
                if type not in (ctypes.c_bool, ctypes.c_float, ctypes.c_double, ctypes.c_longdouble):
                    exec('result.append(atomic.'+functext+'_sub_and_fetch(aref,ctypes.c_'+typetext+"(" + f'{sublist[i]}' + ")))")
                    assert result[-1] == exlist[i] - addlist[i]
                    assert a.value == result[-1]
                    exec('result.append(atomic.'+functext+'_add_and_fetch(aref,ctypes.c_'+typetext+"(" + f'{addlist[i]}' + ")))")
                    assert result[-1] == exlist[i]
                    assert a.value == result[-1]
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
    v = ctypes.c_size_t(2 ** 63 - 1)
    vref = ctypes.byref(v)

    threadlist=[]

    for i in range(10000):
        threadlist.append(Thread(target=atomic.size_t_sub_and_fetch, args=(vref, ctypes.c_size_t(100))))

    for i in range(10000):
        threadlist[i].start()

    for i in range(10000):
        threadlist[i].join()

    assert v.value == 2 ** 63 - 1 - 100 * 10000


def test_processing_atomic():
    """
    test multiple process
    :return: None
    """
    v = Value(ctypes.c_size_t, 2 ** 63 - 1, lock=False)
    vref = ctypes.byref(v)

    processlist = []
    for i in range(10000):
        processlist.append(Process(target=atomic.size_t_sub_and_fetch, args=(vref, ctypes.c_size_t(100))))

    for i in range(10000):
        processlist[i].start()

    for i in range(10000):
        processlist[i].join()

    assert v.value == 2 ** 63 - 1 - 100 * 10000


def test_compile():
    """
    test compile
    :return: None
    """
    os.chdir('/Users/philren/PycharmProjects/shared_atomic')
    from shared_atomic import atomic_setup
    atomic_setup.main()

def test_loaddll():
    dll=loaddll()

from shared_atomic import atomic_string
from shared_atomic import loaddll
import ctypes
import sys
from threading import Thread
from multiprocessing import Process, Value


inlist = (
         'a',
         'é',
         '重1',
         '重重',
)


exlist = ('b',
         'è',
         '启2',
         '轻轻',
          )

atomic = loaddll()

def signed2unsigned(input, i):
    if input < 0:
        return int.to_bytes(input + 2**((i+1)*8),length=i+1, byteorder='big').lstrip(b'\0')
    return int.to_bytes(input,length=2**i, byteorder='big').lstrip(b'\0')


def setup_function():
    """
    pre function for pytest
    :return: None
    """
    global atomic
    atomic = loaddll()
    # if sys.platform in ('darwin','linux'):
    #     dlltype = ctypes.CDLL
    #     os.chdir('/Users/philren/.local/share/virtualenvs/spark-examples--HrH57AW/lib/python3.6/site-packages')
    #     filename = 'shared_atomic.cpython-36m-darwin.so'
    # elif sys.platform == "win32":
    #     dlltype = ctypes.windll
    # else:
    #     return
    #atomic = ctypes.LibraryLoader(dlltype).LoadLibrary(filename)

def teardown_function():
    pass

def test_init():
    a = atomic_string('ab1234567', length=7)
    a.get_string()
    a = atomic_string('ab')
    assert a.value == 'ab'
    a = atomic_string('ab', length=7, paddingdirection='l', paddingstr='012')
    assert a.value == '01201ab'
    a = atomic_string('ab', length=7, paddingdirection='r', paddingstr='012')
    assert a.value == 'ab01201'
    a = atomic_string('ab', length=7)
    assert a.value == 'ab     '
    a = atomic_string('ab1234567', length=7, trimming_direction='l')
    assert a.value == '1234567'
    a = atomic_string('ab1234567', length=7)
    assert a.value == 'ab12345'


def test_resize():
    a = atomic_string('ab1234567', length=7)
    a.resize(6)
    assert a.value == 'ab1234'
    a.resize(5, trimming_direction='l')
    assert a.value == 'b1234'
    a.resize(7, paddingstr='a', paddingdirection='l')
    assert a.value == 'aab1234'
    a.resize(6, trimming_direction='l')
    assert a.value == 'ab1234'
    a.resize(7, paddingstr='a', paddingdirection='r')
    assert a.value == 'ab1234a'

def test_string():
    a = atomic_string('ab', length=7, paddingdirection='r', paddingstr='012', mode='m')
    assert a.get_string() == 'ab01201'
    a.set_string('abc')

    aa = atomic_string('aa', length=7, paddingdirection='r', paddingstr='012', mode='m')
    bb = atomic_string('bb', length=7, paddingdirection='r', paddingstr='012', mode='m')
    result = aa.string_compare_and_set(bb, 'ab')

    assert result == False
    assert bb.get_string() == aa.get_string()

    result = aa.string_compare_and_set(bb, 'ab')

    assert result == True
    assert aa.get_string() == 'ab'


def test_value_string():
    """
    test single process single thread
    :return: None
    """
    i = 0
    result = None
    try:
        for i in range(4):
            print("i=",f'{i}')
            if i != 3:
                a = atomic_string('a'*(2**i))
            else:
                a = atomic_string('a'*7)

            result = []
            b = atomic_string(inlist[i])
            a.string_store(b)
            assert a.get_string() == inlist[i]
            result.append(a.string_get_and_set(exlist[i]))
            assert result[-1] == inlist[i]
            assert a.get_string() == exlist[i]
            c = []
            c.append(atomic_string(exlist[i]))
            result.append(a.string_compare_and_set(c[-1], inlist[i]))
            assert result[-1]
            assert a.get_string() == inlist[i]
            c.append(atomic_string(inlist[i]))
            c.append(atomic_string(exlist[i]))
            result.append(a.string_shift(c[-1], c[-2]))
            assert c[-1].get_string() == a.get_string()
            assert c[-2].get_string() == inlist[i]

            value = a.get_string()
            a.reencode('utf-16-le')
            assert a.value == value

            if sys.platform != 'win32':
                value = a.get_string()
                a.change_mode('m')
                assert value == a.get_string()
                assert a.mode == 'm'
                a.change_mode('s')
                assert value == a.get_string()
                assert a.mode == 's'


            i += 1
    except Exception as e:
        print(e)
        print(i)
        raise e


def thread_run(a,c):

    b = atomic_string('ab')
    if a.string_compare_and_set(b, 'cd'):
        atomic.long_add_and_fetch(ctypes.byref(c), ctypes.c_long(1))

def test_thread_atomic():
    """
    test single process multiple threads
    :return: None
    """
    a = atomic_string('ab')
    b = ctypes.c_long(0)

    threadlist=[]

    for i in range(10000):
        threadlist.append(Thread(target=thread_run, args=(a,b)))

    for i in range(10000):
        threadlist[i].start()

    for i in range(10000):
        threadlist[i].join()

    assert a.value == 'cd'
    assert b.value == 1


if sys.platform != "win32":
    def process_run(a,c):
        b = atomic_string('ab')
        if a.string_compare_and_set(b, 'cd'):
            atomic.long_add_and_fetch(ctypes.byref(c), ctypes.c_long(1))

    def test_process_atomic():
        """
        test multiple processes
        :return: None
        """
        a = atomic_string('ab', mode='m')
        c = Value(ctypes.c_long, lock=False)
        c.value = 0
        processlist = []
        for i in range(10000):
            processlist.append(Process(target=process_run, args=(a,c)))

        for i in range(10000):
            processlist[i].start()

        for i in range(10000):
            processlist[i].join()

        assert a.value == 'cd'
        assert c.value == 1


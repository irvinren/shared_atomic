from shared_atomic import *
import sys
from threading import Thread
from multiprocessing import Process

def setup_function():
    """
    pre function for pytest
    :return: None
    """
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

def test_uinit():
    a = atomic_uint(2**64-1)
    assert a.get() == 2**64-1
    a = atomic_uint(0)
    assert a.get() == 0

def test_uint():
    a = atomic_uint(2**64-1)
    assert a.get() == 2**64-1
    a.set(0)
    assert a.get() == 0
    b = atomic_uint(2**64-1)
    result = a.uint_compare_and_set(b, 2**64-1)
    assert result == False
    assert b.get() == a.get()
    result = a.uint_compare_and_set(b, 2**64-1)

    assert result == True
    assert a.get() == 2**64-1

    b = atomic_uint(2**64-2)
    a.uint_store(b)

    assert a.value == b.value

    result = a.uint_get_and_set(2**64-1)
    assert result == 2**64-2
    assert a.value == 2**64-1

    c = atomic_uint(2**64-4)
    b = atomic_uint(2**64-5)
    a.uint_shift(b, c)
    assert a.value == 2**64-5
    assert c.value == 2**64-1

    assert a.uint_add_and_fetch(1) == 2**64-4
    assert a.uint_sub_and_fetch(1) == 2**64-5
    assert a.uint_and_and_fetch(1111) == 2**64-5 & 1111
    assert a.uint_or_and_fetch(1111) == (2**64-5 & 1111) | 1111
    assert a.uint_xor_and_fetch(1111) == ((2**64-5 & 1111) | 1111) ^ 1111
    assert a.uint_nand_and_fetch(1111) == ~(( ((2**64-5 & 1111) | 1111) ^ 1111 ) & 1111)+2**64
    a.set(2**64-4)
    assert a.uint_fetch_and_add(1) == 2**64-4
    assert a.uint_fetch_and_sub(1) == 2**64-3
    assert a.uint_fetch_and_and(1111) == 2**64-4
    assert a.uint_fetch_and_or(1111) == 2**64-4 & 1111
    assert a.uint_fetch_and_xor(1111) == (2**64-4 & 1111) | 1111
    assert a.uint_fetch_and_nand(1111) == ((2**64-4 & 1111) | 1111) ^ 1111
    assert a.value == ~((((2**64-4 & 1111) | 1111) ^ 1111) & 1111) + 2**64

    a.value = 2**64-5

    assert uint_add_and_fetch(a.reference, 1) == 2**64-4
    assert uint_sub_and_fetch(a.reference, 1) == 2**64-5
    assert uint_and_and_fetch(a.reference,1111) == 2**64-5 & 1111
    assert uint_or_and_fetch(a.reference, 1111) == (2**64-5 & 1111) | 1111
    assert uint_xor_and_fetch(a.reference, 1111) == ((2**64-5 & 1111) | 1111) ^ 1111
    assert uint_nand_and_fetch(a.reference, 1111) == ~((((2**64-5 & 1111) | 1111) ^ 1111) & 1111) + 2**64
    a.set(2**64-4)
    assert uint_fetch_and_add(a.reference,1) == 2**64-4
    assert uint_fetch_and_sub(a.reference,1) == 2**64-3
    assert uint_fetch_and_and(a.reference,1111) == 2**64-4
    assert uint_fetch_and_or(a.reference,1111) == 2**64-4 & 1111
    assert uint_fetch_and_xor(a.reference,1111) == (2**64-4 & 1111) | 1111
    assert uint_fetch_and_nand(a.reference,1111) == ((2**64-4 & 1111) | 1111) ^ 1111
    assert a.value == ~((((2**64-4 & 1111) | 1111) ^ 1111) & 1111) + 2**64


def thread_run(i):
    uint_add_and_fetch(i.reference, 100)

def test_thread_atomic():
    """
    test single process multiple threads
    :return: None
    """
    a = atomic_uint(0)

    threadlist = []

    for i in range(10000):
        threadlist.append(Thread(target=thread_run, args=(a,)))

    for i in range(10000):
        threadlist[i].start()

    for i in range(10000):
        threadlist[i].join()

    assert a.value == 100 * 10000


if sys.platform != "win32":
    def process_run(a):

        def subthread_run(a):
            uint_add_and_fetch(a.reference, 100)

        threadlist = []
        for t in range(5000):
            threadlist.append(Thread(target=subthread_run, args=(a,)))

        for t in range(5000):
            threadlist[t].start()

        for t in range(5000):
            threadlist[t].join()

    def test_process_atomic():
        """
        test multiple processes
        :return: None
        """
        a = atomic_uint(0, mode= 'm')
        processlist = []
        for i in range(2):
            processlist.append(Process(target=process_run, args=(a,)))

        for i in range(2):
            processlist[i].start()

        for i in range(2):
            processlist[i].join()

        assert a.get() == 100*10000

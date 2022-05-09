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

def test_init():
    a = atomic_int(2**63-1)
    assert a.get() == 2**63-1
    a = atomic_int(-2**63)
    assert a.get() == -2**63

def test_int():
    a = atomic_int(2**63-1)
    assert a.get() == 2**63-1
    a.set(-2**63)
    assert a.get() == -2**63
    b = atomic_int(2**63-2)
    result = a.int_compare_and_set(b, 1)
    assert result == False
    assert b.get() == a.get()
    result = a.int_compare_and_set(b, 1)

    assert result == True
    assert a.get() == 1

    b = atomic_int(2**63-2)
    a.int_store(b)

    assert a.value == b.value

    result = a.int_get_and_set(2**63-3)
    assert result == 2**63-2
    assert a.value == 2**63-3

    c = atomic_int(2**63-4)
    b = atomic_int(2**63-5)
    a.int_shift(b, c)
    assert a.value == 2**63-5
    assert c.value == 2**63-3

    assert a.int_add_and_fetch(1) == 2**63-4
    assert a.int_sub_and_fetch(1) == 2**63-5
    assert a.int_and_and_fetch(1111) == 2**63-5 & 1111
    assert a.int_or_and_fetch(1111) == (2**63-5 & 1111) | 1111
    assert a.int_xor_and_fetch(1111) == ((2**63-5 & 1111) | 1111) ^ 1111
    assert a.int_nand_and_fetch(1111) == ~((((2**63-5 & 1111) | 1111) ^ 1111) & 1111)
    a.set(2**63-4)
    assert a.int_fetch_and_add(1) == 2**63-4
    assert a.int_fetch_and_sub(1) == 2**63-3
    assert a.int_fetch_and_and(1111) == 2**63-4
    assert a.int_fetch_and_or(1111) == 2**63-4 & 1111
    assert a.int_fetch_and_xor(1111) == (2**63-4 & 1111) | 1111
    assert a.int_fetch_and_nand(1111) == ((2**63-4 & 1111) | 1111) ^ 1111
    assert a.value == ~((((2**63-4 & 1111) | 1111) ^ 1111) & 1111)

    a.value = 2**63-5

    assert int_add_and_fetch(a.reference, 1) == 2**63-4
    assert int_sub_and_fetch(a.reference, 1) == 2**63-5
    assert int_and_and_fetch(a.reference,1111) == 2**63-5 & 1111
    assert int_or_and_fetch(a.reference, 1111) == (2**63-5 & 1111) | 1111
    assert int_xor_and_fetch(a.reference, 1111) == ((2**63-5 & 1111) | 1111) ^ 1111
    assert int_nand_and_fetch(a.reference, 1111) == ~((((2**63-5 & 1111) | 1111) ^ 1111) & 1111)
    a.set(2**63-4)
    assert int_fetch_and_add(a.reference,1) == 2**63-4
    assert int_fetch_and_sub(a.reference,1) == 2**63-3
    assert int_fetch_and_and(a.reference,1111) == 2**63-4
    assert int_fetch_and_or(a.reference,1111) == 2**63-4 & 1111
    assert int_fetch_and_xor(a.reference,1111) == (2**63-4 & 1111) | 1111
    assert int_fetch_and_nand(a.reference,1111) == ((2**63-4 & 1111) | 1111) ^ 1111
    assert a.value == ~((((2**63-4 & 1111) | 1111) ^ 1111) & 1111)


def thread_run(i):
    int_add_and_fetch(i.reference, 100)

def test_thread_atomic():
    """
    test single process multiple threads
    :return: None
    """
    a = atomic_int(0)

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
            int_add_and_fetch(a.reference, 100)

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
        a = atomic_int(0, mode= 'm')
        processlist = []
        for i in range(2):
            processlist.append(Process(target=process_run, args=(a,)))

        for i in range(2):
            processlist[i].start()

        for i in range(2):
            processlist[i].join()

        assert a.get() == 100*10000


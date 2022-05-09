from shared_atomic import *
import sys
from threading import Thread
from multiprocessing import Process
import math

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
    a = atomic_bool(True)
    assert a.get() == True
    a = atomic_bool(False)
    assert a.get() == False
    a = atomic_float(math.pi)
    assert a.get() == math.pi
    a.set(math.e)
    assert a.get() == math.e

def test_int():
    a = atomic_bool(True)
    a.set(False)

    assert a.value == False
    a.set(True)
    assert a.get() == True

    b = atomic_bool(False)
    a.bool_store(b)

    assert a.value == b.value

    result = a.bool_get_and_set(True)
    assert result == False
    assert a.value == True

    b = atomic_bool(False)

    assert a.bool_compare_and_set(b, True) == False
    assert a.get() == b.get()

    assert a.bool_compare_and_set(b, False) == True
    assert a.get() == False


    a = atomic_bool(True)
    b = atomic_bool(False)

    bool_store(a.reference, b.reference)

    assert a.value == b.value
    result = bool_get_and_set(a.reference, True)

    assert result == False
    assert a.value == True

    b = atomic_bool(False)

    assert bool_compare_and_set(a.reference, b.reference, True) == False
    assert a.get() == b.get()

    assert a.bool_compare_and_set(b, True) == True
    assert a.get() == True

    a = atomic_float(math.pi)
    a.set(math.e)
    assert a.value == math.e
    a.set(math.pi)
    assert a.value == math.pi

    b = atomic_float(math.e)
    float_store(a.reference, b.reference)
    a.value = math.e


def thread_run(a, b, c):
    x = atomic_bool(False)
    if a.bool_compare_and_set(x, True):
        int_add_and_fetch(c.reference, 1)

    y = atomic_float(math.pi)
    b.float_store(y)

def test_thread_atomic():
    """
    test single process multiple threads
    :return: None
    """
    a = atomic_bool(False)
    b = atomic_float(math.e)
    c = atomic_int(0)


    threadlist = []

    for i in range(10000):
        threadlist.append(Thread(target=thread_run, args=(a,b,c)))

    for i in range(10000):
        threadlist[i].start()

    for i in range(10000):
        threadlist[i].join()

    assert a.value == True
    assert c.value == 1
    assert b.value == math.pi


if sys.platform != "win32":
    def process_run(a,b,c):

        def subthread_run(a,b,c):
            x = atomic_bool(False)
            if a.bool_compare_and_set(x, True):
                int_add_and_fetch(c.reference, 1)

            y = atomic_float(math.pi)
            b.float_store(y)

        threadlist = []
        for t in range(5000):
            threadlist.append(Thread(target=subthread_run, args=(a,b,c)))

        for t in range(5000):
            threadlist[t].start()

        for t in range(5000):
            threadlist[t].join()

    def test_process_atomic():
        """
        test multiple processes
        :return: None
        """
        a = atomic_bool(False, mode='m')
        b = atomic_float(math.e, mode='m')
        c = atomic_int(0, mode='m')
        processlist = []
        for i in range(2):
            processlist.append(Process(target=process_run, args=(a,b,c)))

        for i in range(2):
            processlist[i].start()

        for i in range(2):
            processlist[i].join()

        assert a.value == True
        assert c.value == 1
        assert b.value == math.pi


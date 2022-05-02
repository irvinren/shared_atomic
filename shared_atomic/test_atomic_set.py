from shared_atomic import atomic_set
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
    a = atomic_set({1, 2, 3})
    assert a.get_set() == {1,2,3}
    a = atomic_set((True, False,))
    assert a.get_set() == {True, False}
    a = atomic_set({b'ab',b'cd'})
    assert a.get_set() == {b'ab',b'cd'}
    a = atomic_set({'ab','cd'})
    assert a.get_set() == {'ab','cd'}
    a = atomic_set({'中','国'},encoding='utf-16-le')
    assert a.get_set() == {'中','国'}

    a = atomic_set({1,'中',True,b'x12'}, encoding='utf-16-le')
    assert a.get_set() == {1,'中',True,b'x12'}

def test_set():
    a = atomic_set({1,'中',True,b'x12'}, encoding='utf-16-le')
    assert a.get_set() == {1,'中',True,b'x12'}
    a = atomic_set({1}, encoding='utf-16-le')
    a.set_set({0,'国',True,b'x21'})
    assert a.get_set() == {0,'国',True,b'x21'}
    b = atomic_set({0,'国',True,b'x12'}, encoding='utf-16-le')

    result = a.set_compare_and_set(b, {1,2,3})

    assert result == False
    assert b.get_set() == a.get_set()

    result = a.set_compare_and_set(b, {0,1,2,3,4,5,6})

    assert result == True
    assert a.get_set() == {0,1,2,3,4,5,6}

    a.set_set({0,'国',True,b'x2'})

    a.reencode('utf-8')

    a.value = {0,'国',True,b'x2'}

    b = atomic_set({12,'s',True,b'x12'})
    a.set_store(b)

    assert a.value == b.value

    result = a.set_get_and_set({0,1,2,3})
    assert result == {12,'s',True,b'x12'}
    assert a.value == {0,1,2,3}

    c = atomic_set({12,'s',3,4,5})
    b = atomic_set({0,1,4,3,2,5,6})
    a.set_shift(b, c)
    assert a.value == {0,1,4,3,2,5,6}
    assert c.value == {0,1,2,3}

def thread_run(a,i):

    b = atomic_set({'ab'})
    if a.set_compare_and_set(b, {'cd'}):
        atomic.long_add_and_fetch(ctypes.byref(i), ctypes.c_long(1))

def test_thread_atomic():
    """
    test single process multiple threads
    :return: None
    """
    a = atomic_set({'ab'})
    b = ctypes.c_long(0)

    threadlist = []

    for i in range(10000):
        threadlist.append(Thread(target=thread_run, args=(a, b)))

    for i in range(10000):
        threadlist[i].start()

    for i in range(10000):
        threadlist[i].join()

    assert a.value == {'cd'}
    assert b.value == 1


if sys.platform != "win32":
    def process_run(a,c):
        b = atomic_set({'ab'})
        if a.set_compare_and_set(b, {'cd'}):
            atomic.long_add_and_fetch(ctypes.byref(c), ctypes.c_long(1))

    def test_process_atomic():
        """
        test multiple processes
        :return: None
        """
        a = atomic_set({'ab'}, mode='m')
        c = Value(ctypes.c_long, lock=False)
        c.value = 0
        processlist = []
        for i in range(10000):
            processlist.append(Process(target=process_run, args=(a,c)))

        for i in range(10000):
            processlist[i].start()

        for i in range(10000):
            processlist[i].join()

        assert a.value == {'cd'}
        assert c.value == 1

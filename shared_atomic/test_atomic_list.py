from shared_atomic import atomic_list
from shared_atomic import atomic_int
from shared_atomic import int_add_and_fetch
import ctypes
import sys
from threading import Thread
from multiprocessing import Process


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
def teardown_function():
    pass

def test_init():
    a = atomic_list([1, 2, 2, 3])
    assert a.get_list() == [1,2,2,3]
    a = atomic_list((True, False,))
    assert a.get_list() == [True, False]
    a = atomic_list([b'ab',b'cd'])
    assert a.get_list() == [b'ab',b'cd']
    a = atomic_list(['ab','cd'])
    assert a.get_list() == ['ab','cd']
    a = atomic_list(['中','国',b'1'],encoding='utf-16-le')
    assert a.get_list() == ['中','国',b'1']

    a = atomic_list([1,'中',True,b'x12'], encoding='utf-16-le')
    assert a.get_list() == [1,'中',True,b'x12']

def test_list():
    a = atomic_list([1,'中',True,b'x12'], encoding='utf-16-le')
    assert a.get_list() == [1,'中',True,b'x12']
    a = atomic_list([1], encoding='utf-16-le')
    a.set_list([0,'国',True,b'x21'])
    assert a.get_list() == [0,'国',True,b'x21']
    b = atomic_list([0,'国',True,b'x12'], encoding='utf-16-le')

    result = a.list_compare_and_set(b, [1,2,3])

    assert result == False
    assert b.get_list() == a.get_list()

    result = a.list_compare_and_set(b, [0,1,2,3,4,5,6])

    assert result == True
    assert a.get_list() == [0,1,2,3,4,5,6]

    a.set_list([0,'国',True,b'x2'])

    a.reencode('utf-8')

    a.value = [0,'国',True,b'x2']

    b = atomic_list([12,'s',True,b'x12'])
    a.list_store(b)

    assert a.value == b.value

    result = a.list_get_and_set([0,1,2,3])
    assert result == [12,'s',True,b'x12']
    assert a.value == [0,1,2,3]

    c = atomic_list([12,'s',3,4,5])
    b = atomic_list([0,1,4,3,2,5,6])
    a.list_shift(b, c)
    assert a.value == [0,1,4,3,2,5,6]
    assert c.value == [0,1,2,3]

def thread_run(a,i):

    b = atomic_list(['ab'])
    if a.list_compare_and_set(b, ['cd']):
        i.int_add_and_fetch(1)

def test_thread_atomic():
    """
    test single process multiple threads
    :return: None
    """
    a = atomic_list(['ab'])
    b = atomic_int(0)

    threadlist = []

    for i in range(10000):
        threadlist.append(Thread(target=thread_run, args=(a, b)))

    for i in range(10000):
        threadlist[i].start()

    for i in range(10000):
        threadlist[i].join()

    assert a.value == ['cd']
    assert b.value == 1


if sys.platform != "win32":

    def process_run(a,c):

        def subthread_run(a, c):
            b = atomic_list(['ab'])
            if a.list_compare_and_set(b, ['cd']):
                c.int_add_and_fetch(1)

        threadlist = []
        for t in range(5000):
            threadlist.append(Thread(target=subthread_run, args=(a,c)))

        for t in range(5000):
            threadlist[t].start()

        for t in range(5000):
            threadlist[t].join()
    def test_process_atomic():
        """
        test multiple processes
        :return: None
        """
        a = atomic_list({'ab'}, mode='m')
        c = atomic_int(0, mode='m')
        processlist = []
        for i in range(2):
            processlist.append(Process(target=process_run, args=(a,c)))

        for i in range(2):
            processlist[i].start()

        for i in range(2):
            processlist[i].join()

        assert a.value == ['cd']
        assert c.value == 1


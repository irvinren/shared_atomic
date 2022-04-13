'''
Created on 29 Mar 2022

@author: philren
'''
import pytest
from multiprocessing import Array, Value, Process
from threading import Thread
import ctypes
import os

atomic=None

def setup_function():
    global atomic
    os.chdir('/Users/philren/PycharmProjects/shared_atomic/build/lib.macosx-11.5-x86_64-3.6')
    atomic = ctypes.CDLL('shared_atomic.cpython-36m-darwin.so')

def teardown_function():
    global atomic
    atomic = None

def test_atomic():
    """
    test single process single thread
    :return: None
    """
    a = Array(ctypes.c_long, 100, lock=False)
    aref = ctypes.byref(a, 0)
    atomic.long_get_and_set(aref, ctypes.c_long(100))
    assert a[0] == 100



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

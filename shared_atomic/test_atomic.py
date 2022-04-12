'''
Created on 29 Mar 2022

@author: philren
'''
from multiprocessing import Array, Value
import ctypes
import os
def test_atomic():
    os.chdir('/Users/philren/PycharmProjects/shared_atomic/build/lib.macosx-11.5-x86_64-3.6')
    atomic = ctypes.CDLL('shared_atomic.cpython-36m-darwin.so')
    v = Value(ctypes.c_long, 100, lock=False)
    a = Array(ctypes.c_long, 100, lock=False)
    aref = ctypes.byref(a, 0)
    atomic.long_get_and_set(aref,ctypes.c_long(100))
    print(a[0])

def test_compile():
    os.chdir('/Users/philren/PycharmProjects/shared_atomic')
    from shared_atomic import atomic_setup
    atomic_setup.main()

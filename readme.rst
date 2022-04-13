With the help of multiprocessing shared ctypes,
we have achieved shared variables and arrays. but synchronization could be achieved by locks.
this package provided a second way to access those primitive ctypes with atomic operations.
can be used in python version above 3.0 till the latest 3.11

Usage
    #load the compiled .so file with ctypes

    import ctypes

    atomic = ctypes.CDLL('shared_atomic.cpython-36m-darwin.so')


    #create shared variables

    v = Value(ctypes.c_long, 100, lock=False)

    a = Array(ctypes.c_long, 100, lock=False)


    #get pointer address by ctypes.byref

    aref = ctypes.byref(a, 0)


    #atomic operations can be used at last

    atomic.long_get_and_set(aref,ctypes.c_long(100))

Installation
    #To install shared_atomic, use pip:

    pip install shared_atomic


Sourcecode Repo:
https://github.com/irvinren/shared_atomic.git
https://gitee.com/irvinren/shared_atomic.git

For documentation, please go to:
https://shared-atomic.readthedocs.io/en/latest/

The project is licensed under GPL v3.0
With the help of multiprocessing shared ctypes,
we have achieved shared variables and arrays. but synchronization could be achieved by locks.
this package provided a second way to access those primitive ctypes with atomic operations.
can be used in

- Environment,

 - LINUX/MacOSX
    - CPython 3.0 - 3.11
    - Pypy 3.0 - 3.9

 - Windows
    - CPython 3.0 - 3.11
    - Pypy not supported

- Requirement,

 - LINUX/MacOSX

    - the package requires libatomic installed on Linux platform

    - cffi >= 1.0.0 <= 1.1.15 to compile through on Linux/MacOSX platform

    - gcc >= 4.8 to include the atomic APIs.

 - Windows

    - cppyy >= 1.5.0 <=2.3.1

    - only support single thread/multiple threads modes, multiprocessing mode is not supported on windows

- Installation

 - To install shared_atomic, use pip:

    pip install shared_atomic


- Usage

 - load the compiled .so file with ctypes

    import ctypes
    
    from shared_atomic import loaddll
    
    atomic = loaddll()

 - you can also import by CDLL, but not recommended since the CDLL will casting all the return type to c_int. For the 64bit integer, it will return the wrong result.

    atomic = ctypes.CDLL('shared_atomic.cpython-36m-darwin.so')


 - in multiple threads condition:

  - get pointer address by ctypes.byref

    v = ctypes.c_size_t(2 ** 63 - 1)

    vref = ctypes.byref(v)

  - start multiple threads

    threadlist=[]

    for i in range(10000):
        threadlist.append(Thread(target=atomic.size_t_sub_and_fetch, args=(vref, ctypes.c_size_t(100))))

    for i in range(10000):
        threadlist[i].start()

    for i in range(10000):
        threadlist[i].join()


 - in multiple processing condition:

  - get pointer address by ctypes.byref

    v = multiprocessing.Value(ctypes.c_size_t, 2 ** 63 - 1, lock=False)

    vref = ctypes.byref(v)


  - start multiple processes

    processlist = []

    for i in range(10000):
        processlist.append(Process(target=atomic.size_t_sub_and_fetch, args=(vref, ctypes.c_size_t(100))))

    for i in range(10000):
        processlist[i].start()

    for i in range(10000):
        processlist[i].join()

 - Currently concurrent.futures.ProcessPoolExecutor and concurrent.futures.ThreadPoolExecutor cannot be used to start multiple executions ,since the cdll function cannot be serilized by pickle.

Sourcecode Repo:

 https://github.com/irvinren/shared_atomic.git

 https://gitee.com/irvinren/shared_atomic.git

For documentation, please go to:

 https://shared-atomic.readthedocs.io/en/latest/

The project is licensed under GPL v3.0

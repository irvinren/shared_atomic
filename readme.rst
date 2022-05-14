The module can be used for atomic operations under multiple processes and multiple threads conditions.

- Environment,

 - LINUX/MacOSX
    - CPython 3.0 - 3.11
    - Pypy 3.0 - 3.9

 - Windows
    - CPython 3.0 - 3.11
    - Pypy not supported

- Included Datatypes:

 - - atomic_int

 - - atomic_uint

 - - atomic_float

 - - atomic_bool

 - - atomic_bytearray

 - - atomic_string

 - - atomic_set, package bitarray >= 2.4.0 is needed.

 - - atomic_list, package bitarray >= 2.4.0 is needed.


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

 - create function used by child processes, refer to UIntAPIs, IntAPIs, BytearrayAPIs, StringAPIs, SetAPIs, ListAPIs, in each process, you can create multiple threads.

        - def process_run(a):

             def subthread_run(a):

                 a.array_sub_and_fetch(b'\x0F')

             threadlist = []

             for t in range(5000):

                 threadlist.append(Thread(target=subthread_run, args=(a,)))

             for t in range(5000):

                 threadlist[t].start()

             for t in range(5000):

                 threadlist[t].join()

 - create the shared bytearray

        a = atomic_bytearray(b'ab', length=7, paddingdirection='r', paddingbytes=b'012', mode='m')

 - start processes/threads to utilize the shared bytearray

        processlist = []

        for p in range(2):

            processlist.append(Process(target=process_run, args=(a,)))

        for p in range(2):

            processlist[p].start()

        for p in range(2):

            processlist[p].join()

        assert a.value == int.to_bytes(27411031864108609,length=8,byteorder='big')

 - Currently concurrent.futures.ProcessPoolExecutor and concurrent.futures.ThreadPoolExecutor cannot be used to start multiple executions ,for serialization problems.

Sourcecode Repo:

 https://github.com/irvinren/shared_atomic.git

 https://gitee.com/irvinren/shared_atomic.git

For documentation, please go to:

 https://shared-atomic.readthedocs.io/en/latest/

中文文档，请参阅：

 https://shared-atomic.readthedocs.io/zh_CN/latest/

繁體中文文檔，請參閲：
 https://shared-atomic.readthedocs.io/zh_TW/latest/

The project is licensed under GPL v3.0

# Example:

You need the following steps to utilize the module:

1) dynamically linked library is loaded by shared_atomic.loaddll(),

    `atomic = shared_atomic.loaddll()`

2) define shared ctypes between processes / threads

    `v = multiprocessing.Value(ctypes.c_long, 100, lock=False)`
    
    `a = multiprocessing.Array(ctypes.c_long, 100, lock=False)`
    
    if only threads are needed
    
    `a = ctypes.c_long(100)`
    
3) get the pointer from ctypes.byref
    
    `aref = ctypes.byref(a, 0)`

4) pass the pointer to atomic functions
    
    `atomic.long_get_and_set(aref,ctypes.c_long(100))`
    
    `processlist = []`
    
    `for i in range(10000):`
    `    processlist.append(Process(target=atomic.long_get_and_set, args=(aref,ctypes.c_long(100))))`

    `for i in range(10000):`
    `    processlist[i].start()`

    `for i in range(10000):`
    `    processlist[i].join()`

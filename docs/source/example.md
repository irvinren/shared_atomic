# Example:

You need the following steps to utilize the module:

1) dynamically linked library is loaded by ctypes.CDLL,

    `atomic = ctypes.CDLL('shared_atomic.cpython-36m-darwin.so')`

2) define shared ctypes between processes

    `v = multiprocessing.Value(ctypes.c_long, 100, lock=False)`
    
    `a = multiprocessing.Array(ctypes.c_long, 100, lock=False)`
    
3) get the pointer from ctypes.byref
    
    `aref = ctypes.byref(a, 0)`

4) pass the pointer to atomic functions
    
    `atomic.long_get_and_set(aref,ctypes.c_long(100))`

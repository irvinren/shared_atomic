# Bytearray Example:

You need the following steps to utilize the module:

1) create function used by child processs/threads is use  [BytearrayAPIs](./bytearray_api.md),

    `def process_run(a):`
    
    `    a.array_sub_and_fetch(b'\x0F')`

2) create the shared bytearray


    `    a = atomic_bytearray(b'ab', length=7, paddingdirection='r', paddingbytes=b'012', mode='m')`

3) start processes/threads to utilize the shared bytearray

    `    processlist = []`
    
    `    for i in range(10000):`
    
    `        processlist.append(Process(target=process_run, args=(a,)))`

    `    for i in range(10000):`
    
    `        processlist[i].start()`

    `    for i in range(10000):`
    
    `        processlist[i].join()`

    `    assert a.value == int.to_bytes(27411031864108609,length=8,byteorder='big')`


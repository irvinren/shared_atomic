# atomic api Example:

You need the following steps to utilize the module:

1) create function used by child processes, refer to [UIntAPIs](./uint_api.md), [IntAPIs](./int_api.md), [BytearrayAPIs](./bytearray_api.md), [StringAPIs](./string_api.md), [SetAPIs](./set_api.md), [ListAPIs](./list_api.md), in each process, you can create multiple threads.

   `def process_run(a):`

   `     def subthread_run(a):`
   
   `         a.array_sub_and_fetch(b'\x0F')`

   `     threadlist = []`
   
   `     for t in range(5000):`
   
   `         threadlist.append(Thread(target=subthread_run, args=(a,)))`

   `     for t in range(5000):`
   
   `         threadlist[t].start()`

   `     for t in range(5000):`
   
   `         threadlist[t].join()`

2) create the shared bytearray

    `    a = atomic_bytearray(b'ab', length=7, paddingdirection='r', paddingbytes=b'012', mode='m')`

3) start processes/threads to utilize the shared bytearray

    `    processlist = []`
    
    `    for p in range(2):`
    
    `        processlist.append(Process(target=process_run, args=(a,)))`

    `    for p in range(2):`
    
    `        processlist[p].start()`

    `    for p in range(2):`
    
    `        processlist[p].join()`

    `    assert a.value == int.to_bytes(27411031864108609,length=8,byteorder='big')`


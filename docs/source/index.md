Welcome to shared_atomic's documentation!
=========================================

<big> The module can be used for atomic operations under multiple processs and multiple threads conditions.

Included datatypes, detailed reference, please see docstring in the sourcecode
- - atomic_int
- - atomic_uint
- - atomic_float
- - atomic_bool
- - atomic_bytearray
- - atomic_string
- - atomic_set, package [bitarray>=2.4.0](https://pypi.org/project/bitarray/) is needed.
- - atomic_list, package [bitarray>=2.4.0](https://pypi.org/project/bitarray/) is needed

Ctypes APIs inherited from the old version continue to work.

Requirement:
- On Linux/MacOSX, 
- - the module support CPython 3.0-3.11, Pypy 3.0-3.9, 
- - should be built upon cffi >= 1.0.0, <= 1.1.15, 
- On Windows, 
- - the module only support CPython 3.0-3.11, doesn't support Pypy. 
- - The module depends on cppyy >=1.5.0, <=2.3.1, which use [cling](https://github.com/vgvassilev/cling/tree/master/tools/packaging) as dynamic intepreter.
- - multiprocessing mode is not supported, only single process, multiple threads modes are supported.

For example usage of the module, please visit this [atomic_api_example](./atomic_api_example.md)

  [ctypes_example](./ctypes_example.md) and

For ctypes api references, please visit [ctypes api](./ctypes_api.md).</big>

##

```{eval-rst}
.. toctree::

   atomic_api_example.md
   ctypes_example.md
   ctypes_api.md

 ```
 
 ![Python Logo](https://www.python.org/static/community_logos/python-logo.png)


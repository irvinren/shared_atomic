Welcome to shared_atomic's documentation!
=========================================

<big> The module can be used for atomic operations on shared ctypes value and arrays under multiple processs and multiple threads conditions.

Datatypes:
- Use ctypes or multiprocessing.Value/Array to achieve atomicy.
- Other types included in this package,
- - [atomic_bytearray](./bytearray_api.md)
- - [atomic_string](./string_api.md)
- - [atomic_set](./set_api.md), package [bitarray>=2.4.0](https://pypi.org/project/bitarray/) is needed.
- - [atomic_list](./list_api.md), package [bitarray>=2.4.0](https://pypi.org/project/bitarray/) is needed


Requirement:
- On Linux/MacOSX, 
- - the module support CPython 3.0-3.11, Pypy 3.0-3.9, 
- - should be built upon cffi >= 1.0.0, <= 1.1.15, 
- On Windows, 
- - the module only support CPython 3.0-3.11, doesn't support Pypy. 
- - The module depends on cppyy >=1.5.0, <=2.3.1, which use [cling](https://github.com/vgvassilev/cling/tree/master/tools/packaging) as dynamic intepreter.


For example usage of the module, please visit this  [ctypes_example](./ctypes_example.md) and [bytearray/set/string_example](./bytearray_example.md)

For ctypes api references, please visit [ctypes api](./ctypes_api.md).

For python atomic_bytearray api references, please visit [atomic_bytearray](./bytearray_api.md).

For python atomic_string api references, please visit [atomic_string](./string_api.md).

For python atomic_list api references, please visit [atomic_list](./list_api.md).

For python atomic_set api references, please visit [atomic_set](./set_api.md).</big>

##

```{eval-rst}
.. toctree::

   ctypes_example.md
   bytearray_example.md
   ctypes_api.md
   bytearray_api.md
   string_api.md
   set_api.md
   list_api.md
 ```
 
 ![Python Logo](https://www.python.org/static/community_logos/python-logo.png)


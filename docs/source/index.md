Welcome to shared_atomic's documentation!
=========================================

<big> The module can be used for atomic operations on shared ctypes value and arrays under multiple processs and multiple threads conditions.

On Linux/MacOSX, the module should be built upon CFFI>1.0, can be loaded dynamically by [ctypes.CDLL](https://docs.python.org/3/library/ctypes.html?highlight=ctypes%20cdll#ctypes.CDLL) .
On Windows, the module use cppyy ==2.3.1, which use [cling](https://github.com/vgvassilev/cling/tree/master/tools/packaging) as dynamic intepreter.

When calling those functions, the address of the shared variables could be get by [ctypes.byref](https://docs.python.org/3/library/ctypes.html?highlight=ctypes.byref#ctypes.byref)

For detailed usage of the module, please visit this  [example](./example.md).

For api references, please visit [api](./api.md).</big>

![Python Logo](https://www.python.org/static/community_logos/python-logo.png)


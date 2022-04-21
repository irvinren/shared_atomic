import sys
import ctypes
from pathlib import Path


def loaddll():
    if sys.platform == 'darwin':
        filepatten = 'shared_atomic.cpython-*-darwin.so'
    elif sys.platform == 'linux':
        filepatten = 'shared_atomic.cpython-*-linux-gnu.so'

    result = None
    if sys.platform in ('darwin', 'linux'):
        for search_path in sys.path:
            dll_list = Path(search_path).glob(filepatten)
            try:
                result = next(dll_list)
                break
            except StopIteration:
                continue
        if not result:
            raise FileNotFoundError(f'{filepatten} not found in search path!')
        return ctypes.CDLL(result)

    elif sys.platform == "win32":
        import cppyy
        cfilepath = Path.joinpath(Path(__file__).parent, 'atomic_csource.c')
        with open(cfilepath, 'r') as cfile:
            ctext = cfile.read()
        cppyy.cppdef('''
        #if defined(_MSC_VER)
        #include <BaseTsd.h>
        typedef SSIZE_T ssize_t;
        #endif
        typedef bool _Bool;
        ''' + ctext)
        return cppyy.gbl
    else:
        return
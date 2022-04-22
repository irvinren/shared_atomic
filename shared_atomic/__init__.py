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
        lib = ctypes.CDLL(result)

        # bool functions
        lib.bool_store.restype = None
        lib.bool_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.bool_get_and_set.restype = ctypes.c_bool
        lib.bool_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_bool]

        lib.bool_compare_and_set.restype = ctypes.c_bool
        lib.bool_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool]

        # byte functions

        lib.byte_store.restype = None
        lib.byte_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.byte_add_and_fetch.restype = ctypes.c_byte
        lib.byte_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_byte]

        lib.byte_sub_and_fetch.restype = ctypes.c_byte
        lib.byte_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_byte]

        lib.byte_get_and_set.restype = ctypes.c_byte
        lib.byte_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_byte]

        lib.byte_compare_and_set.restype = ctypes.c_bool
        lib.byte_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_byte]

        # ubyte functions

        lib.ubyte_store.restype = None
        lib.ubyte_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.ubyte_add_and_fetch.restype = ctypes.c_ubyte
        lib.ubyte_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]

        lib.ubyte_sub_and_fetch.restype = ctypes.c_ubyte
        lib.ubyte_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]

        lib.ubyte_get_and_set.restype = ctypes.c_ubyte
        lib.ubyte_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]

        lib.ubyte_compare_and_set.restype = ctypes.c_bool
        lib.ubyte_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ubyte]

        # short functions

        lib.short_store.restype = None
        lib.short_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.short_add_and_fetch.restype = ctypes.c_short
        lib.short_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_short]

        lib.short_sub_and_fetch.restype = ctypes.c_short
        lib.short_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_short]

        lib.short_get_and_set.restype = ctypes.c_short
        lib.short_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_short]

        lib.short_compare_and_set.restype = ctypes.c_bool
        lib.short_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_short]

        # ushort functions

        lib.ushort_store.restype = None
        lib.ushort_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.ushort_add_and_fetch.restype = ctypes.c_ushort
        lib.ushort_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ushort]

        lib.ushort_sub_and_fetch.restype = ctypes.c_ushort
        lib.ushort_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ushort]

        lib.ushort_get_and_set.restype = ctypes.c_ushort
        lib.ushort_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_ushort]

        lib.ushort_compare_and_set.restype = ctypes.c_bool
        lib.ushort_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ushort]

        # int functions

        lib.int_store.restype = None
        lib.int_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.int_add_and_fetch.restype = ctypes.c_int
        lib.int_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_int]

        lib.int_sub_and_fetch.restype = ctypes.c_int
        lib.int_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_int]

        lib.int_get_and_set.restype = ctypes.c_int
        lib.int_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_int]

        lib.int_compare_and_set.restype = ctypes.c_bool
        lib.int_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

        # uint functions

        lib.uint_store.restype = None
        lib.uint_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.uint_add_and_fetch.restype = ctypes.c_uint
        lib.uint_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_uint]

        lib.uint_sub_and_fetch.restype = ctypes.c_uint
        lib.uint_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_uint]

        lib.uint_get_and_set.restype = ctypes.c_uint
        lib.uint_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_uint]

        lib.uint_compare_and_set.restype = ctypes.c_bool
        lib.uint_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint]

        # long functions

        lib.long_store.restype = None
        lib.long_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.long_add_and_fetch.restype = ctypes.c_long
        lib.long_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_long]

        lib.long_sub_and_fetch.restype = ctypes.c_long
        lib.long_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_long]

        lib.long_get_and_set.restype = ctypes.c_long
        lib.long_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_long]

        lib.long_compare_and_set.restype = ctypes.c_bool
        lib.long_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_long]

        # ulong functions

        lib.ulong_store.restype = None
        lib.ulong_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.ulong_add_and_fetch.restype = ctypes.c_ulong
        lib.ulong_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ulong]

        lib.ulong_sub_and_fetch.restype = ctypes.c_ulong
        lib.ulong_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ulong]

        lib.ulong_get_and_set.restype = ctypes.c_ulong
        lib.ulong_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_ulong]

        lib.ulong_compare_and_set.restype = ctypes.c_bool
        lib.ulong_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulong]

        # c_longlong functions

        lib.longlong_store.restype = None
        lib.longlong_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.longlong_add_and_fetch.restype = ctypes.c_longlong
        lib.longlong_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_longlong]

        lib.longlong_sub_and_fetch.restype = ctypes.c_longlong
        lib.longlong_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_longlong]

        lib.longlong_get_and_set.restype = ctypes.c_longlong
        lib.longlong_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_longlong]

        lib.longlong_compare_and_set.restype = ctypes.c_bool
        lib.longlong_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]

        # c_ulonglong functions

        lib.ulonglong_store.restype = None
        lib.ulonglong_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.ulonglong_add_and_fetch.restype = ctypes.c_longlong
        lib.ulonglong_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong]

        lib.ulonglong_sub_and_fetch.restype = ctypes.c_longlong
        lib.ulonglong_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong]

        lib.ulonglong_get_and_set.restype = ctypes.c_longlong
        lib.ulonglong_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong]

        lib.ulonglong_compare_and_set.restype = ctypes.c_bool
        lib.ulonglong_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulonglong]

        # size_t functions

        lib.size_t_store.restype = None
        lib.size_t_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.size_t_add_and_fetch.restype = ctypes.c_size_t
        lib.size_t_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

        lib.size_t_sub_and_fetch.restype = ctypes.c_size_t
        lib.size_t_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

        lib.size_t_get_and_set.restype = ctypes.c_size_t
        lib.size_t_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

        lib.size_t_compare_and_set.restype = ctypes.c_bool
        lib.size_t_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]

        # ssize_t functions

        lib.ssize_t_store.restype = None
        lib.ssize_t_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.ssize_t_add_and_fetch.restype = ctypes.c_ssize_t
        lib.ssize_t_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ssize_t]

        lib.ssize_t_sub_and_fetch.restype = ctypes.c_ssize_t
        lib.ssize_t_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ssize_t]

        lib.ssize_t_get_and_set.restype = ctypes.c_ssize_t
        lib.ssize_t_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_ssize_t]

        lib.ssize_t_compare_and_set.restype = ctypes.c_bool
        lib.ssize_t_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ssize_t]

        # float functions

        lib.float_store.restype = None
        lib.float_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        # double functions

        lib.double_store.restype = None
        lib.double_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        # longdouble functions

        lib.longdouble_store.restype = None
        lib.longdouble_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        return lib

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
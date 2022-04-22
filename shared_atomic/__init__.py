import sys
import ctypes
from pathlib import Path

win_ddl = None
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

        # wchar functions

        lib.wchar_store.restype = None
        lib.wchar_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.wchar_add_and_fetch.restype = ctypes.c_wchar
        lib.wchar_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_wchar]

        lib.wchar_sub_and_fetch.restype = ctypes.c_wchar
        lib.wchar_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_wchar]

        lib.wchar_get_and_set.restype = ctypes.c_wchar
        lib.wchar_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_wchar]

        lib.wchar_compare_and_set.restype = ctypes.c_bool
        lib.wchar_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_wchar]

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
        global win_ddl
        if win_ddl is None:
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
            win_ddl = cppyy.gbl

        class result_dll:

            @staticmethod
            def bool_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.bool_store(v, n)
            @staticmethod
            def bool_get_and_set(v: ctypes.c_void_p, n: ctypes.c_bool)->bool:
                return win_ddl.bool_get_and_set(v, n)
            @staticmethod
            def bool_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_bool)->bool:
                return win_ddl.bool_get_and_set(v, e, n)

            @staticmethod
            def ubyte_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.ubyte_store(v, n)
            @staticmethod
            def ubyte_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ubyte)->int:
                return int.from_bytes(win_ddl.ubyte_add_and_fetch(v, n.value).encode(encoding='latin1'), byteorder=sys.byteorder)
            @staticmethod
            def ubyte_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ubyte)->int:
                return int.from_bytes(win_ddl.ubyte_sub_and_fetch(v, n.value).encode(encoding='latin1'), byteorder=sys.byteorder)
            @staticmethod
            def ubyte_get_and_set(v: ctypes.c_void_p, n: ctypes.c_ubyte)->int:
                return int.from_bytes(win_ddl.ubyte_get_and_set(v, n.value).encode(encoding='latin1'), byteorder=sys.byteorder)
            @staticmethod
            def ubyte_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_ubyte)->bool:
                return win_ddl.ubyte_compare_and_set(v, e, n.value)

            @staticmethod
            def short_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.short_store(v, n)
            @staticmethod
            def short_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_short)->int:
                return win_ddl.short_add_and_fetch(v, n.value)
            @staticmethod
            def short_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_short)->int:
                return win_ddl.short_sub_and_fetch(v, n.value)
            @staticmethod
            def short_get_and_set(v: ctypes.c_void_p, n: ctypes.c_short)->int:
                return win_ddl.short_get_and_set(v, n.value)
            @staticmethod
            def short_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_int)->bool:
                return win_ddl.short_compare_and_set(v, e, n.value)

            @staticmethod
            def ushort_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.ushort_store(v, n)
            @staticmethod
            def ushort_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ushort)->int:
                return win_ddl.ushort_add_and_fetch(v, n.value)
            @staticmethod
            def ushort_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ushort)->int:
                return win_ddl.ushort_sub_and_fetch(v, n.value)
            @staticmethod
            def ushort_get_and_set(v: ctypes.c_void_p, n: ctypes.c_ushort)->int:
                return win_ddl.ushort_get_and_set(v, n.value)
            @staticmethod
            def ushort_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_ushort)->bool:
                return win_ddl.ushort_compare_and_set(v, e, n.value)

            @staticmethod
            def int_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.int_store(v, n)
            @staticmethod
            def int_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_int)->int:
                return win_ddl.int_add_and_fetch(v, n.value)
            @staticmethod
            def int_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_int)->int:
                return win_ddl.int_sub_and_fetch(v, n.value)
            @staticmethod
            def int_get_and_set(v: ctypes.c_void_p, n: ctypes.c_int)->int:
                return win_ddl.int_get_and_set(v, n.value)
            @staticmethod
            def int_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_int)->bool:
                return win_ddl.int_get_and_set(v, e, n.value)

            @staticmethod
            def uint_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.uint_store(v, n)
            @staticmethod
            def uint_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
                return win_ddl.uint_add_and_fetch(v, n.value)
            @staticmethod
            def uint_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
                return win_ddl.uint_sub_and_fetch(v, n.value)
            @staticmethod
            def uint_get_and_set(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
                return win_ddl.uint_get_and_set(v, n.value)
            @staticmethod
            def uint_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_uint) -> bool:
                return win_ddl.uint_get_and_set(v, e, n.value)

            @staticmethod
            def long_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.long_store(v, n)
            @staticmethod
            def long_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
                return win_ddl.long_add_and_fetch(v, n.value)
            @staticmethod
            def long_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
                return win_ddl.long_sub_and_fetch(v, n.value)
            @staticmethod
            def long_get_and_set(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
                return win_ddl.long_get_and_set(v, n.value)
            @staticmethod
            def long_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_long) -> bool:
                return win_ddl.long_get_and_set(v, e, n.value)

            @staticmethod
            def ulong_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.ulong_store(v, n)
            @staticmethod
            def ulong_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
                return win_ddl.ulong_add_and_fetch(v, n.value)
            @staticmethod
            def ulong_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
                return win_ddl.ulong_sub_and_fetch(v, n.value)
            @staticmethod
            def ulong_get_and_set(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
                return win_ddl.ulong_get_and_set(v, n.value)
            @staticmethod
            def ulong_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_ulong) -> bool:
                return win_ddl.ulong_get_and_set(v, e, n.value)

            @staticmethod
            def longlong_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.longlong_store(v, n)
            @staticmethod
            def longlong_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
                return win_ddl.longlong_add_and_fetch(v, n.value)
            @staticmethod
            def longlong_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
                return win_ddl.longlong_sub_and_fetch(v, n.value)
            @staticmethod
            def longlong_get_and_set(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
                return win_ddl.longlong_get_and_set(v, n.value)
            @staticmethod
            def longlong_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_longlong) -> bool:
                return win_ddl.longlong_get_and_set(v, e, n.value)

            @staticmethod
            def ulonglong_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.ulonglong_store(v, n)
            @staticmethod
            def ulonglong_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
                return win_ddl.ulonglong_add_and_fetch(v, n.value)
            @staticmethod
            def ulonglong_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
                return win_ddl.ulonglong_sub_and_fetch(v, n.value)
            @staticmethod
            def ulonglong_get_and_set(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
                return win_ddl.ulonglong_get_and_set(v, n.value)
            @staticmethod
            def ulonglong_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_ulonglong) -> bool:
                return win_ddl.ulonglong_get_and_set(v, e, n.value)

            @staticmethod
            def size_t_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.size_t_store(v, n)
            @staticmethod
            def size_t_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
                return win_ddl.size_t_add_and_fetch(v, n.value)
            @staticmethod
            def size_t_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
                return win_ddl.size_t_sub_and_fetch(v, n.value)
            @staticmethod
            def size_t_get_and_set(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
                return win_ddl.size_t_get_and_set(v, n.value)
            @staticmethod
            def size_t_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_size_t) -> bool:
                return win_ddl.size_t_get_and_set(v, e, n.value)

            @staticmethod
            def ssize_t_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.size_t_store(v, n)
            @staticmethod
            def ssize_t_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
                return win_ddl.size_t_add_and_fetch(v, n.value)
            @staticmethod
            def ssize_t_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
                return win_ddl.size_t_sub_and_fetch(v, n.value)
            @staticmethod
            def ssize_t_get_and_set(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
                return win_ddl.size_t_get_and_set(v, n.value)
            @staticmethod
            def ssize_t_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_ssize_t) -> bool:
                return win_ddl.size_t_get_and_set(v, e, n.value)

            @staticmethod
            def float_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.float_store(v, n)

            @staticmethod
            def double_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.double_store(v, n)

            @staticmethod
            def longdouble_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.longdouble_store(v, n)

        return result_dll


    else:
        return
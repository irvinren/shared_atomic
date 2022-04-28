import sys
import ctypes
from pathlib import Path
import sysconfig
win_ddl = None
def loaddll():
    """
    function to load the dynamiclly linked library to scope

    :return: class with atomic operation functions as class method
    """

    result = None
    if sys.platform in ('darwin', 'linux'):
        filepatten = {
            'darwin': {'PyPy': 'shared_atomic.pypy*-darwin.so',
                       '': 'shared_atomic.cpython-*-darwin.so'},
            'linux': {'PyPy': 'shared_atomic.pypy*-linux-gnu.so',
                      '': 'shared_atomic.cpython-*-linux-gnu.so'},
        }
        for search_path in sys.path:
            dll_list = Path(search_path).glob(
                filepatten[sys.platform]
                ['' if sysconfig.get_config_var('implementation') is None else sysconfig.get_config_var('implementation')]
            )
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

        lib.bool_shift.restype = None
        lib.bool_shift.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

        lib.bool_compare_and_set.restype = ctypes.c_bool
        lib.bool_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool]

        # byte functions

        lib.byte_store.restype = None
        lib.byte_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.byte_get_and_set.restype = ctypes.c_byte
        lib.byte_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_byte]

        lib.byte_shift.restype = None
        lib.byte_shift.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

        lib.byte_compare_and_set.restype = ctypes.c_bool
        lib.byte_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_byte]

        lib.byte_add_and_fetch.restype = ctypes.c_byte
        lib.byte_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_byte]

        lib.byte_sub_and_fetch.restype = ctypes.c_byte
        lib.byte_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_byte]

        lib.byte_and_and_fetch.restype = ctypes.c_byte
        lib.byte_and_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_byte]

        lib.byte_or_and_fetch.restype = ctypes.c_byte
        lib.byte_or_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_byte]

        lib.byte_xor_and_fetch.restype = ctypes.c_byte
        lib.byte_xor_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_byte]

        lib.byte_nand_and_fetch.restype = ctypes.c_byte
        lib.byte_nand_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_byte]

        lib.byte_fetch_and_add.restype = ctypes.c_byte
        lib.byte_fetch_and_add.argtypes = [ctypes.c_void_p, ctypes.c_byte]

        lib.byte_fetch_and_sub.restype = ctypes.c_byte
        lib.byte_fetch_and_sub.argtypes = [ctypes.c_void_p, ctypes.c_byte]

        lib.byte_fetch_and_and.restype = ctypes.c_byte
        lib.byte_fetch_and_and.argtypes = [ctypes.c_void_p, ctypes.c_byte]

        lib.byte_fetch_and_or.restype = ctypes.c_byte
        lib.byte_fetch_and_or.argtypes = [ctypes.c_void_p, ctypes.c_byte]

        lib.byte_fetch_and_xor.restype = ctypes.c_byte
        lib.byte_fetch_and_xor.argtypes = [ctypes.c_void_p, ctypes.c_byte]

        lib.byte_fetch_and_nand.restype = ctypes.c_byte
        lib.byte_fetch_and_nand.argtypes = [ctypes.c_void_p, ctypes.c_byte]

        # ubyte functions

        lib.ubyte_store.restype = None
        lib.ubyte_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.ubyte_shift.restype = None
        lib.ubyte_shift.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

        lib.ubyte_get_and_set.restype = ctypes.c_ubyte
        lib.ubyte_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]

        lib.ubyte_compare_and_set.restype = ctypes.c_bool
        lib.ubyte_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ubyte]

        lib.ubyte_add_and_fetch.restype = ctypes.c_ubyte
        lib.ubyte_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]

        lib.ubyte_sub_and_fetch.restype = ctypes.c_ubyte
        lib.ubyte_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]

        lib.ubyte_and_and_fetch.restype = ctypes.c_ubyte
        lib.ubyte_and_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]

        lib.ubyte_or_and_fetch.restype = ctypes.c_ubyte
        lib.ubyte_or_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]

        lib.ubyte_xor_and_fetch.restype = ctypes.c_ubyte
        lib.ubyte_xor_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]

        lib.ubyte_nand_and_fetch.restype = ctypes.c_ubyte
        lib.ubyte_nand_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]

        lib.ubyte_fetch_and_add.restype = ctypes.c_ubyte
        lib.ubyte_fetch_and_add.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]

        lib.ubyte_fetch_and_sub.restype = ctypes.c_ubyte
        lib.ubyte_fetch_and_sub.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]

        lib.ubyte_fetch_and_and.restype = ctypes.c_ubyte
        lib.ubyte_fetch_and_and.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]

        lib.ubyte_fetch_and_or.restype = ctypes.c_ubyte
        lib.ubyte_fetch_and_or.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]

        lib.ubyte_fetch_and_xor.restype = ctypes.c_ubyte
        lib.ubyte_fetch_and_xor.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]

        lib.ubyte_fetch_and_nand.restype = ctypes.c_ubyte
        lib.ubyte_fetch_and_nand.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]

        # wchar functions

        lib.wchar_store.restype = None
        lib.wchar_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.wchar_shift.restype = None
        lib.wchar_shift.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

        lib.wchar_get_and_set.restype = ctypes.c_wchar
        lib.wchar_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_wchar]

        lib.wchar_compare_and_set.restype = ctypes.c_bool
        lib.wchar_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_wchar]

        lib.wchar_add_and_fetch.restype = ctypes.c_wchar
        lib.wchar_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_wchar]

        lib.wchar_sub_and_fetch.restype = ctypes.c_wchar
        lib.wchar_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_wchar]

        lib.wchar_fetch_and_add.restype = ctypes.c_wchar
        lib.wchar_fetch_and_add.argtypes = [ctypes.c_void_p, ctypes.c_wchar]

        lib.wchar_fetch_and_sub.restype = ctypes.c_wchar
        lib.wchar_fetch_and_sub.argtypes = [ctypes.c_void_p, ctypes.c_wchar]


        # short functions

        lib.short_store.restype = None
        lib.short_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.short_shift.restype = None
        lib.short_shift.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

        lib.short_get_and_set.restype = ctypes.c_short
        lib.short_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_short]

        lib.short_compare_and_set.restype = ctypes.c_bool
        lib.short_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_short]

        lib.short_add_and_fetch.restype = ctypes.c_short
        lib.short_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_short]

        lib.short_sub_and_fetch.restype = ctypes.c_short
        lib.short_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_short]

        lib.short_and_and_fetch.restype = ctypes.c_short
        lib.short_and_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_short]

        lib.short_or_and_fetch.restype = ctypes.c_short
        lib.short_or_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_short]

        lib.short_xor_and_fetch.restype = ctypes.c_short
        lib.short_xor_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_short]

        lib.short_nand_and_fetch.restype = ctypes.c_short
        lib.short_nand_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_short]

        lib.short_fetch_and_add.restype = ctypes.c_short
        lib.short_fetch_and_add.argtypes = [ctypes.c_void_p, ctypes.c_short]

        lib.short_fetch_and_sub.restype = ctypes.c_short
        lib.short_fetch_and_sub.argtypes = [ctypes.c_void_p, ctypes.c_short]

        lib.short_fetch_and_and.restype = ctypes.c_short
        lib.short_fetch_and_and.argtypes = [ctypes.c_void_p, ctypes.c_short]

        lib.short_fetch_and_or.restype = ctypes.c_short
        lib.short_fetch_and_or.argtypes = [ctypes.c_void_p, ctypes.c_short]

        lib.short_fetch_and_xor.restype = ctypes.c_short
        lib.short_fetch_and_xor.argtypes = [ctypes.c_void_p, ctypes.c_short]

        lib.short_fetch_and_nand.restype = ctypes.c_short
        lib.short_fetch_and_nand.argtypes = [ctypes.c_void_p, ctypes.c_short]

        # ushort functions

        lib.ushort_store.restype = None
        lib.ushort_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.ushort_shift.restype = None
        lib.ushort_shift.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

        lib.ushort_get_and_set.restype = ctypes.c_ushort
        lib.ushort_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_ushort]

        lib.ushort_compare_and_set.restype = ctypes.c_bool
        lib.ushort_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ushort]

        lib.ushort_add_and_fetch.restype = ctypes.c_ushort
        lib.ushort_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ushort]

        lib.ushort_sub_and_fetch.restype = ctypes.c_ushort
        lib.ushort_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ushort]

        lib.ushort_and_and_fetch.restype = ctypes.c_ushort
        lib.ushort_and_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ushort]

        lib.ushort_or_and_fetch.restype = ctypes.c_ushort
        lib.ushort_or_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ushort]

        lib.ushort_xor_and_fetch.restype = ctypes.c_ushort
        lib.ushort_xor_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ushort]

        lib.ushort_nand_and_fetch.restype = ctypes.c_ushort
        lib.ushort_nand_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ushort]

        lib.ushort_fetch_and_add.restype = ctypes.c_ushort
        lib.ushort_fetch_and_add.argtypes = [ctypes.c_void_p, ctypes.c_ushort]

        lib.ushort_fetch_and_sub.restype = ctypes.c_ushort
        lib.ushort_fetch_and_sub.argtypes = [ctypes.c_void_p, ctypes.c_ushort]

        lib.ushort_fetch_and_and.restype = ctypes.c_ushort
        lib.ushort_fetch_and_and.argtypes = [ctypes.c_void_p, ctypes.c_ushort]

        lib.ushort_fetch_and_or.restype = ctypes.c_ushort
        lib.ushort_fetch_and_or.argtypes = [ctypes.c_void_p, ctypes.c_ushort]

        lib.ushort_fetch_and_xor.restype = ctypes.c_ushort
        lib.ushort_fetch_and_xor.argtypes = [ctypes.c_void_p, ctypes.c_ushort]

        lib.ushort_fetch_and_nand.restype = ctypes.c_ushort
        lib.ushort_fetch_and_nand.argtypes = [ctypes.c_void_p, ctypes.c_ushort]

        # int functions

        lib.int_store.restype = None
        lib.int_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.int_shift.restype = None
        lib.int_shift.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

        lib.int_get_and_set.restype = ctypes.c_int
        lib.int_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_int]

        lib.int_compare_and_set.restype = ctypes.c_bool
        lib.int_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

        lib.int_add_and_fetch.restype = ctypes.c_int
        lib.int_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_int]

        lib.int_sub_and_fetch.restype = ctypes.c_int
        lib.int_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_int]

        lib.int_and_and_fetch.restype = ctypes.c_int
        lib.int_and_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_int]

        lib.int_or_and_fetch.restype = ctypes.c_int
        lib.int_or_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_int]

        lib.int_xor_and_fetch.restype = ctypes.c_int
        lib.int_xor_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_int]

        lib.int_nand_and_fetch.restype = ctypes.c_int
        lib.int_nand_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_int]

        lib.int_fetch_and_add.restype = ctypes.c_int
        lib.int_fetch_and_add.argtypes = [ctypes.c_void_p, ctypes.c_int]

        lib.int_fetch_and_sub.restype = ctypes.c_int
        lib.int_fetch_and_sub.argtypes = [ctypes.c_void_p, ctypes.c_int]

        lib.int_fetch_and_and.restype = ctypes.c_int
        lib.int_fetch_and_and.argtypes = [ctypes.c_void_p, ctypes.c_int]

        lib.int_fetch_and_or.restype = ctypes.c_int
        lib.int_fetch_and_or.argtypes = [ctypes.c_void_p, ctypes.c_int]

        lib.int_fetch_and_xor.restype = ctypes.c_int
        lib.int_fetch_and_xor.argtypes = [ctypes.c_void_p, ctypes.c_int]

        lib.int_fetch_and_nand.restype = ctypes.c_int
        lib.int_fetch_and_nand.argtypes = [ctypes.c_void_p, ctypes.c_int]

        # uint functions

        lib.uint_store.restype = None
        lib.uint_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.uint_shift.restype = None
        lib.uint_shift.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

        lib.uint_get_and_set.restype = ctypes.c_uint
        lib.uint_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_uint]

        lib.uint_compare_and_set.restype = ctypes.c_bool
        lib.uint_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint]

        lib.uint_add_and_fetch.restype = ctypes.c_uint
        lib.uint_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_uint]

        lib.uint_sub_and_fetch.restype = ctypes.c_uint
        lib.uint_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_uint]

        lib.uint_and_and_fetch.restype = ctypes.c_uint
        lib.uint_and_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_uint]

        lib.uint_or_and_fetch.restype = ctypes.c_uint
        lib.uint_or_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_uint]

        lib.uint_xor_and_fetch.restype = ctypes.c_uint
        lib.uint_xor_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_uint]

        lib.uint_nand_and_fetch.restype = ctypes.c_uint
        lib.uint_nand_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_uint]

        lib.uint_fetch_and_add.restype = ctypes.c_uint
        lib.uint_fetch_and_add.argtypes = [ctypes.c_void_p, ctypes.c_uint]

        lib.uint_fetch_and_sub.restype = ctypes.c_uint
        lib.uint_fetch_and_sub.argtypes = [ctypes.c_void_p, ctypes.c_uint]

        lib.uint_fetch_and_and.restype = ctypes.c_uint
        lib.uint_fetch_and_and.argtypes = [ctypes.c_void_p, ctypes.c_uint]

        lib.uint_fetch_and_or.restype = ctypes.c_uint
        lib.uint_fetch_and_or.argtypes = [ctypes.c_void_p, ctypes.c_uint]

        lib.uint_fetch_and_xor.restype = ctypes.c_uint
        lib.uint_fetch_and_xor.argtypes = [ctypes.c_void_p, ctypes.c_uint]

        lib.uint_fetch_and_nand.restype = ctypes.c_uint
        lib.uint_fetch_and_nand.argtypes = [ctypes.c_void_p, ctypes.c_uint]

        # long functions

        lib.long_store.restype = None
        lib.long_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.long_shift.restype = None
        lib.long_shift.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

        lib.long_get_and_set.restype = ctypes.c_long
        lib.long_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_long]

        lib.long_compare_and_set.restype = ctypes.c_bool
        lib.long_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_long]

        lib.long_add_and_fetch.restype = ctypes.c_long
        lib.long_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_long]

        lib.long_sub_and_fetch.restype = ctypes.c_long
        lib.long_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_long]

        lib.long_and_and_fetch.restype = ctypes.c_long
        lib.long_and_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_long]

        lib.long_or_and_fetch.restype = ctypes.c_long
        lib.long_or_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_long]

        lib.long_xor_and_fetch.restype = ctypes.c_long
        lib.long_xor_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_long]

        lib.long_nand_and_fetch.restype = ctypes.c_long
        lib.long_nand_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_long]

        lib.long_fetch_and_add.restype = ctypes.c_long
        lib.long_fetch_and_add.argtypes = [ctypes.c_void_p, ctypes.c_long]

        lib.long_fetch_and_sub.restype = ctypes.c_long
        lib.long_fetch_and_sub.argtypes = [ctypes.c_void_p, ctypes.c_long]

        lib.long_fetch_and_and.restype = ctypes.c_long
        lib.long_fetch_and_and.argtypes = [ctypes.c_void_p, ctypes.c_long]

        lib.long_fetch_and_or.restype = ctypes.c_long
        lib.long_fetch_and_or.argtypes = [ctypes.c_void_p, ctypes.c_long]

        lib.long_fetch_and_xor.restype = ctypes.c_long
        lib.long_fetch_and_xor.argtypes = [ctypes.c_void_p, ctypes.c_long]

        lib.long_fetch_and_nand.restype = ctypes.c_long
        lib.long_fetch_and_nand.argtypes = [ctypes.c_void_p, ctypes.c_long]

        # ulong functions

        lib.ulong_store.restype = None
        lib.ulong_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.ulong_shift.restype = None
        lib.ulong_shift.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

        lib.ulong_get_and_set.restype = ctypes.c_ulong
        lib.ulong_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_ulong]

        lib.ulong_compare_and_set.restype = ctypes.c_bool
        lib.ulong_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulong]

        lib.ulong_add_and_fetch.restype = ctypes.c_ulong
        lib.ulong_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ulong]

        lib.ulong_sub_and_fetch.restype = ctypes.c_ulong
        lib.ulong_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ulong]

        lib.ulong_and_and_fetch.restype = ctypes.c_ulong
        lib.ulong_and_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ulong]

        lib.ulong_or_and_fetch.restype = ctypes.c_ulong
        lib.ulong_or_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ulong]

        lib.ulong_xor_and_fetch.restype = ctypes.c_ulong
        lib.ulong_xor_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ulong]

        lib.ulong_nand_and_fetch.restype = ctypes.c_ulong
        lib.ulong_nand_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ulong]

        lib.ulong_fetch_and_add.restype = ctypes.c_ulong
        lib.ulong_fetch_and_add.argtypes = [ctypes.c_void_p, ctypes.c_ulong]

        lib.ulong_fetch_and_sub.restype = ctypes.c_ulong
        lib.ulong_fetch_and_sub.argtypes = [ctypes.c_void_p, ctypes.c_ulong]

        lib.ulong_fetch_and_and.restype = ctypes.c_ulong
        lib.ulong_fetch_and_and.argtypes = [ctypes.c_void_p, ctypes.c_ulong]

        lib.ulong_fetch_and_or.restype = ctypes.c_ulong
        lib.ulong_fetch_and_or.argtypes = [ctypes.c_void_p, ctypes.c_ulong]

        lib.ulong_fetch_and_xor.restype = ctypes.c_ulong
        lib.ulong_fetch_and_xor.argtypes = [ctypes.c_void_p, ctypes.c_ulong]

        lib.ulong_fetch_and_nand.restype = ctypes.c_ulong
        lib.ulong_fetch_and_nand.argtypes = [ctypes.c_void_p, ctypes.c_ulong]

        # c_longlong functions

        lib.longlong_store.restype = None
        lib.longlong_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.longlong_shift.restype = None
        lib.longlong_shift.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

        lib.longlong_get_and_set.restype = ctypes.c_longlong
        lib.longlong_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_longlong]

        lib.longlong_compare_and_set.restype = ctypes.c_bool
        lib.longlong_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]

        lib.longlong_add_and_fetch.restype = ctypes.c_longlong
        lib.longlong_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_longlong]

        lib.longlong_sub_and_fetch.restype = ctypes.c_longlong
        lib.longlong_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_longlong]

        lib.longlong_and_and_fetch.restype = ctypes.c_longlong
        lib.longlong_and_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_longlong]

        lib.longlong_or_and_fetch.restype = ctypes.c_longlong
        lib.longlong_or_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_longlong]

        lib.longlong_xor_and_fetch.restype = ctypes.c_longlong
        lib.longlong_xor_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_longlong]

        lib.longlong_nand_and_fetch.restype = ctypes.c_longlong
        lib.longlong_nand_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_longlong]

        lib.longlong_fetch_and_add.restype = ctypes.c_longlong
        lib.longlong_fetch_and_add.argtypes = [ctypes.c_void_p, ctypes.c_longlong]

        lib.longlong_fetch_and_sub.restype = ctypes.c_longlong
        lib.longlong_fetch_and_sub.argtypes = [ctypes.c_void_p, ctypes.c_longlong]

        lib.longlong_fetch_and_and.restype = ctypes.c_longlong
        lib.longlong_fetch_and_and.argtypes = [ctypes.c_void_p, ctypes.c_longlong]

        lib.longlong_fetch_and_or.restype = ctypes.c_longlong
        lib.longlong_fetch_and_or.argtypes = [ctypes.c_void_p, ctypes.c_longlong]

        lib.longlong_fetch_and_xor.restype = ctypes.c_longlong
        lib.longlong_fetch_and_xor.argtypes = [ctypes.c_void_p, ctypes.c_longlong]

        lib.longlong_fetch_and_nand.restype = ctypes.c_longlong
        lib.longlong_fetch_and_nand.argtypes = [ctypes.c_void_p, ctypes.c_longlong]

        # c_ulonglong functions

        lib.ulonglong_store.restype = None
        lib.ulonglong_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.ulonglong_shift.restype = None
        lib.ulonglong_shift.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

        lib.ulonglong_get_and_set.restype = ctypes.c_ulonglong
        lib.ulonglong_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong]

        lib.ulonglong_compare_and_set.restype = ctypes.c_bool
        lib.ulonglong_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulonglong]

        lib.ulonglong_add_and_fetch.restype = ctypes.c_ulonglong
        lib.ulonglong_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong]

        lib.ulonglong_sub_and_fetch.restype = ctypes.c_ulonglong
        lib.ulonglong_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong]

        lib.ulonglong_and_and_fetch.restype = ctypes.c_ulonglong
        lib.ulonglong_and_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong]

        lib.ulonglong_or_and_fetch.restype = ctypes.c_ulonglong
        lib.ulonglong_or_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong]

        lib.ulonglong_xor_and_fetch.restype = ctypes.c_ulonglong
        lib.ulonglong_xor_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong]

        lib.ulonglong_nand_and_fetch.restype = ctypes.c_ulonglong
        lib.ulonglong_nand_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong]

        lib.ulonglong_fetch_and_add.restype = ctypes.c_ulonglong
        lib.ulonglong_fetch_and_add.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong]

        lib.ulonglong_fetch_and_sub.restype = ctypes.c_ulonglong
        lib.ulonglong_fetch_and_sub.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong]

        lib.ulonglong_fetch_and_and.restype = ctypes.c_ulonglong
        lib.ulonglong_fetch_and_and.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong]

        lib.ulonglong_fetch_and_or.restype = ctypes.c_ulonglong
        lib.ulonglong_fetch_and_or.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong]

        lib.ulonglong_fetch_and_xor.restype = ctypes.c_ulonglong
        lib.ulonglong_fetch_and_xor.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong]

        lib.ulonglong_fetch_and_nand.restype = ctypes.c_ulonglong
        lib.ulonglong_fetch_and_nand.argtypes = [ctypes.c_void_p, ctypes.c_ulonglong]


        # size_t functions

        lib.size_t_store.restype = None
        lib.size_t_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.size_t_shift.restype = None
        lib.size_t_shift.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

        lib.size_t_get_and_set.restype = ctypes.c_size_t
        lib.size_t_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

        lib.size_t_compare_and_set.restype = ctypes.c_bool
        lib.size_t_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]

        lib.size_t_add_and_fetch.restype = ctypes.c_size_t
        lib.size_t_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

        lib.size_t_sub_and_fetch.restype = ctypes.c_size_t
        lib.size_t_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

        lib.size_t_and_and_fetch.restype = ctypes.c_size_t
        lib.size_t_and_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

        lib.size_t_or_and_fetch.restype = ctypes.c_size_t
        lib.size_t_or_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

        lib.size_t_xor_and_fetch.restype = ctypes.c_size_t
        lib.size_t_xor_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

        lib.size_t_nand_and_fetch.restype = ctypes.c_size_t
        lib.size_t_nand_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

        lib.size_t_fetch_and_add.restype = ctypes.c_size_t
        lib.size_t_fetch_and_add.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

        lib.size_t_fetch_and_sub.restype = ctypes.c_size_t
        lib.size_t_fetch_and_sub.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

        lib.size_t_fetch_and_and.restype = ctypes.c_size_t
        lib.size_t_fetch_and_and.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

        lib.size_t_fetch_and_or.restype = ctypes.c_size_t
        lib.size_t_fetch_and_or.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

        lib.size_t_fetch_and_xor.restype = ctypes.c_size_t
        lib.size_t_fetch_and_xor.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

        lib.size_t_fetch_and_nand.restype = ctypes.c_size_t
        lib.size_t_fetch_and_nand.argtypes = [ctypes.c_void_p, ctypes.c_size_t]


        # ssize_t functions

        lib.ssize_t_store.restype = None
        lib.ssize_t_store.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

        lib.ssize_t_shift.restype = None
        lib.ssize_t_shift.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

        lib.ssize_t_get_and_set.restype = ctypes.c_ssize_t
        lib.ssize_t_get_and_set.argtypes = [ctypes.c_void_p, ctypes.c_ssize_t]

        lib.ssize_t_compare_and_set.restype = ctypes.c_bool
        lib.ssize_t_compare_and_set.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ssize_t]

        lib.ssize_t_add_and_fetch.restype = ctypes.c_ssize_t
        lib.ssize_t_add_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ssize_t]

        lib.ssize_t_sub_and_fetch.restype = ctypes.c_ssize_t
        lib.ssize_t_sub_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ssize_t]

        lib.ssize_t_and_and_fetch.restype = ctypes.c_ssize_t
        lib.ssize_t_and_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ssize_t]

        lib.ssize_t_or_and_fetch.restype = ctypes.c_ssize_t
        lib.ssize_t_or_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ssize_t]

        lib.ssize_t_xor_and_fetch.restype = ctypes.c_ssize_t
        lib.ssize_t_xor_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ssize_t]

        lib.ssize_t_nand_and_fetch.restype = ctypes.c_ssize_t
        lib.ssize_t_nand_and_fetch.argtypes = [ctypes.c_void_p, ctypes.c_ssize_t]

        lib.ssize_t_fetch_and_add.restype = ctypes.c_ssize_t
        lib.ssize_t_fetch_and_add.argtypes = [ctypes.c_void_p, ctypes.c_ssize_t]

        lib.ssize_t_fetch_and_sub.restype = ctypes.c_ssize_t
        lib.ssize_t_fetch_and_sub.argtypes = [ctypes.c_void_p, ctypes.c_ssize_t]

        lib.ssize_t_fetch_and_and.restype = ctypes.c_ssize_t
        lib.ssize_t_fetch_and_and.argtypes = [ctypes.c_void_p, ctypes.c_ssize_t]

        lib.ssize_t_fetch_and_or.restype = ctypes.c_ssize_t
        lib.ssize_t_fetch_and_or.argtypes = [ctypes.c_void_p, ctypes.c_ssize_t]

        lib.ssize_t_fetch_and_xor.restype = ctypes.c_ssize_t
        lib.ssize_t_fetch_and_xor.argtypes = [ctypes.c_void_p, ctypes.c_ssize_t]

        lib.ssize_t_fetch_and_nand.restype = ctypes.c_ssize_t
        lib.ssize_t_fetch_and_nand.argtypes = [ctypes.c_void_p, ctypes.c_ssize_t]

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
            def bool_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
                return win_ddl.bool_shift(v, n, r)
            @staticmethod
            def bool_get_and_set(v: ctypes.c_void_p, n: ctypes.c_bool)->bool:
                return win_ddl.bool_get_and_set(v, n)
            @staticmethod
            def bool_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_bool)->bool:
                return win_ddl.bool_compare_and_set(v, e, n)

            @staticmethod
            def ubyte_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.ubyte_store(v, n)
            @staticmethod
            def ubyte_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
                return win_ddl.ubyte_shift(v, n, r)
            @staticmethod
            def ubyte_get_and_set(v: ctypes.c_void_p, n: ctypes.c_ubyte)->int:
                return int.from_bytes(win_ddl.ubyte_get_and_set(v, n.value).encode(encoding='latin1'), byteorder=sys.byteorder)
            @staticmethod
            def ubyte_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_ubyte)->bool:
                return win_ddl.ubyte_compare_and_set(v, e, n.value)

            @staticmethod
            def ubyte_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ubyte)->int:
                return int.from_bytes(win_ddl.ubyte_add_and_fetch(v, n.value).encode(encoding='latin1'), byteorder=sys.byteorder)
            @staticmethod
            def ubyte_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ubyte)->int:
                return int.from_bytes(win_ddl.ubyte_sub_and_fetch(v, n.value).encode(encoding='latin1'), byteorder=sys.byteorder)
            @staticmethod
            def ubyte_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ubyte)->int:
                return int.from_bytes(win_ddl.ubyte_and_and_fetch(v, n.value).encode(encoding='latin1'), byteorder=sys.byteorder)
            @staticmethod
            def ubyte_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ubyte)->int:
                return int.from_bytes(win_ddl.ubyte_or_and_fetch(v, n.value).encode(encoding='latin1'), byteorder=sys.byteorder)
            @staticmethod
            def ubyte_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ubyte)->int:
                return int.from_bytes(win_ddl.ubyte_xor_and_fetch(v, n.value).encode(encoding='latin1'), byteorder=sys.byteorder)
            @staticmethod
            def ubyte_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ubyte)->int:
                return int.from_bytes(win_ddl.ubyte_nand_and_fetch(v, n.value).encode(encoding='latin1'), byteorder=sys.byteorder)
            @staticmethod
            def ubyte_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_ubyte)->int:
                return int.from_bytes(win_ddl.ubyte_fetch_and_add(v, n.value).encode(encoding='latin1'), byteorder=sys.byteorder)
            @staticmethod
            def ubyte_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_ubyte)->int:
                return int.from_bytes(win_ddl.ubyte_fetch_and_sub(v, n.value).encode(encoding='latin1'), byteorder=sys.byteorder)
            @staticmethod
            def ubyte_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_ubyte)->int:
                return int.from_bytes(win_ddl.ubyte_fetch_and_and(v, n.value).encode(encoding='latin1'), byteorder=sys.byteorder)
            @staticmethod
            def ubyte_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_ubyte)->int:
                return int.from_bytes(win_ddl.ubyte_fetch_and_or(v, n.value).encode(encoding='latin1'), byteorder=sys.byteorder)
            @staticmethod
            def ubyte_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_ubyte)->int:
                return int.from_bytes(win_ddl.ubyte_fetch_and_xor(v, n.value).encode(encoding='latin1'), byteorder=sys.byteorder)
            @staticmethod
            def ubyte_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_ubyte)->int:
                return int.from_bytes(win_ddl.ubyte_fetch_and_nand(v, n.value).encode(encoding='latin1'), byteorder=sys.byteorder)


            @staticmethod
            def short_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.short_store(v, n)
            @staticmethod
            def short_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
                return win_ddl.short_shift(v, n, r)
            @staticmethod
            def short_get_and_set(v: ctypes.c_void_p, n: ctypes.c_short)->int:
                return win_ddl.short_get_and_set(v, n.value)
            @staticmethod
            def short_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_int)->bool:
                return win_ddl.short_compare_and_set(v, e, n.value)

            @staticmethod
            def short_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_short)->int:
                return win_ddl.short_add_and_fetch(v, n.value)
            @staticmethod
            def short_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_short)->int:
                return win_ddl.short_sub_and_fetch(v, n.value)
            @staticmethod
            def short_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_short)->int:
                return win_ddl.short_and_and_fetch(v, n.value)
            @staticmethod
            def short_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_short)->int:
                return win_ddl.short_or_and_fetch(v, n.value)
            @staticmethod
            def short_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_short)->int:
                return win_ddl.short_xor_and_fetch(v, n.value)
            @staticmethod
            def short_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_short)->int:
                return win_ddl.short_nand_and_fetch(v, n.value)
            @staticmethod
            def short_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_short)->int:
                return win_ddl.short_fetch_and_add(v, n.value)
            @staticmethod
            def short_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_short)->int:
                return win_ddl.short_fetch_and_sub(v, n.value)
            @staticmethod
            def short_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_short)->int:
                return win_ddl.short_fetch_and_and(v, n.value)
            @staticmethod
            def short_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_short)->int:
                return win_ddl.short_fetch_and_or(v, n.value)
            @staticmethod
            def short_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_short)->int:
                return win_ddl.short_fetch_and_xor(v, n.value)
            @staticmethod
            def short_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_short)->int:
                return win_ddl.short_fetch_and_nand(v, n.value)

            @staticmethod
            def ushort_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.ushort_store(v, n)
            @staticmethod
            def ushort_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
                return win_ddl.ushort_shift(v, n, r)
            @staticmethod
            def ushort_get_and_set(v: ctypes.c_void_p, n: ctypes.c_ushort)->int:
                return win_ddl.ushort_get_and_set(v, n.value)
            @staticmethod
            def ushort_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_ushort)->bool:
                return win_ddl.ushort_compare_and_set(v, e, n.value)


            @staticmethod
            def ushort_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ushort)->int:
                return win_ddl.ushort_add_and_fetch(v, n.value)
            @staticmethod
            def ushort_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ushort)->int:
                return win_ddl.ushort_sub_and_fetch(v, n.value)
            @staticmethod
            def ushort_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ushort)->int:
                return win_ddl.ushort_and_and_fetch(v, n.value)
            @staticmethod
            def ushort_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ushort)->int:
                return win_ddl.ushort_or_and_fetch(v, n.value)
            @staticmethod
            def ushort_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ushort)->int:
                return win_ddl.ushort_xor_and_fetch(v, n.value)
            @staticmethod
            def ushort_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ushort)->int:
                return win_ddl.ushort_nand_and_fetch(v, n.value)
            @staticmethod
            def ushort_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_ushort)->int:
                return win_ddl.ushort_fetch_and_add(v, n.value)
            @staticmethod
            def ushort_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_ushort)->int:
                return win_ddl.ushort_fetch_and_sub(v, n.value)
            @staticmethod
            def ushort_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_ushort)->int:
                return win_ddl.ushort_fetch_and_and(v, n.value)
            @staticmethod
            def ushort_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_ushort)->int:
                return win_ddl.ushort_fetch_and_or(v, n.value)
            @staticmethod
            def ushort_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_ushort)->int:
                return win_ddl.ushort_fetch_and_xor(v, n.value)
            @staticmethod
            def ushort_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_ushort)->int:
                return win_ddl.ushort_fetch_and_nand(v, n.value)

            @staticmethod
            def int_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.int_store(v, n)
            @staticmethod
            def int_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
                return win_ddl.int_shift(v, n, r)
            @staticmethod
            def int_get_and_set(v: ctypes.c_void_p, n: ctypes.c_int)->int:
                return win_ddl.int_get_and_set(v, n.value)
            @staticmethod
            def int_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_int)->bool:
                return win_ddl.int_compare_and_set(v, e, n.value)

            @staticmethod
            def int_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_int)->int:
                return win_ddl.int_add_and_fetch(v, n.value)
            @staticmethod
            def int_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_int)->int:
                return win_ddl.int_sub_and_fetch(v, n.value)
            @staticmethod
            def int_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_int)->int:
                return win_ddl.int_and_and_fetch(v, n.value)
            @staticmethod
            def int_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_int)->int:
                return win_ddl.int_or_and_fetch(v, n.value)
            @staticmethod
            def int_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_int)->int:
                return win_ddl.int_xor_and_fetch(v, n.value)
            @staticmethod
            def int_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_int)->int:
                return win_ddl.int_nand_and_fetch(v, n.value)
            @staticmethod
            def int_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_int)->int:
                return win_ddl.int_fetch_and_add(v, n.value)
            @staticmethod
            def int_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_int)->int:
                return win_ddl.int_fetch_and_sub(v, n.value)
            @staticmethod
            def int_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_int)->int:
                return win_ddl.int_fetch_and_and(v, n.value)
            @staticmethod
            def int_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_int)->int:
                return win_ddl.int_fetch_and_or(v, n.value)
            @staticmethod
            def int_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_int)->int:
                return win_ddl.int_fetch_and_xor(v, n.value)
            @staticmethod
            def int_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_int)->int:
                return win_ddl.int_fetch_and_nand(v, n.value)

            @staticmethod
            def uint_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.uint_store(v, n)
            @staticmethod
            def uint_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
                return win_ddl.uint_shift(v, n, r)
            @staticmethod
            def uint_get_and_set(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
                return win_ddl.uint_get_and_set(v, n.value)
            @staticmethod
            def uint_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_uint) -> bool:
                return win_ddl.uint_compare_and_set(v, e, n.value)

            @staticmethod
            def uint_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
                return win_ddl.uint_add_and_fetch(v, n.value)
            @staticmethod
            def uint_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
                return win_ddl.uint_sub_and_fetch(v, n.value)
            @staticmethod
            def uint_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
                return win_ddl.uint_and_and_fetch(v, n.value)
            @staticmethod
            def uint_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
                return win_ddl.uint_or_and_fetch(v, n.value)
            @staticmethod
            def uint_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
                return win_ddl.uint_xor_and_fetch(v, n.value)
            @staticmethod
            def uint_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
                return win_ddl.uint_nand_and_fetch(v, n.value)
            @staticmethod
            def uint_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
                return win_ddl.uint_fetch_and_add(v, n.value)
            @staticmethod
            def uint_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
                return win_ddl.uint_fetch_and_sub(v, n.value)
            @staticmethod
            def uint_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
                return win_ddl.uint_fetch_and_and(v, n.value)
            @staticmethod
            def uint_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
                return win_ddl.uint_fetch_and_or(v, n.value)
            @staticmethod
            def uint_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
                return win_ddl.uint_fetch_and_xor(v, n.value)
            @staticmethod
            def uint_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
                return win_ddl.uint_fetch_and_nand(v, n.value)


            @staticmethod
            def long_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.long_store(v, n)
            @staticmethod
            def long_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
                return win_ddl.long_shift(v, n, r)
            @staticmethod
            def long_get_and_set(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
                return win_ddl.long_get_and_set(v, n.value)
            @staticmethod
            def long_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_long) -> bool:
                return win_ddl.long_compare_and_set(v, e, n.value)


            @staticmethod
            def long_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
                return win_ddl.long_add_and_fetch(v, n.value)
            @staticmethod
            def long_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
                return win_ddl.long_sub_and_fetch(v, n.value)
            @staticmethod
            def long_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
                return win_ddl.long_and_and_fetch(v, n.value)
            @staticmethod
            def long_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
                return win_ddl.long_or_and_fetch(v, n.value)
            @staticmethod
            def long_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
                return win_ddl.long_xor_and_fetch(v, n.value)
            @staticmethod
            def long_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
                return win_ddl.long_nand_and_fetch(v, n.value)

            @staticmethod
            def long_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
                return win_ddl.long_fetch_and_add(v, n.value)
            @staticmethod
            def long_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
                return win_ddl.long_fetch_and_sub(v, n.value)
            @staticmethod
            def long_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
                return win_ddl.long_fetch_and_and(v, n.value)
            @staticmethod
            def long_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
                return win_ddl.long_fetch_and_or(v, n.value)
            @staticmethod
            def long_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
                return win_ddl.long_fetch_and_xor(v, n.value)
            @staticmethod
            def long_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
                return win_ddl.long_fetch_and_nand(v, n.value)

            @staticmethod
            def ulong_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.ulong_store(v, n)
            @staticmethod
            def ulong_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
                return win_ddl.ulong_shift(v, n, r)
            @staticmethod
            def ulong_get_and_set(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
                return win_ddl.ulong_get_and_set(v, n.value)
            @staticmethod
            def ulong_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_ulong) -> bool:
                return win_ddl.ulong_compare_and_set(v, e, n.value)

            @staticmethod
            def ulong_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
                return win_ddl.ulong_add_and_fetch(v, n.value)
            @staticmethod
            def ulong_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
                return win_ddl.ulong_sub_and_fetch(v, n.value)
            @staticmethod
            def ulong_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
                return win_ddl.ulong_and_and_fetch(v, n.value)
            @staticmethod
            def ulong_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
                return win_ddl.ulong_or_and_fetch(v, n.value)
            @staticmethod
            def ulong_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
                return win_ddl.ulong_xor_and_fetch(v, n.value)
            @staticmethod
            def ulong_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
                return win_ddl.ulong_nand_and_fetch(v, n.value)
            @staticmethod
            def ulong_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
                return win_ddl.ulong_fetch_and_add(v, n.value)
            @staticmethod
            def ulong_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
                return win_ddl.ulong_fetch_and_sub(v, n.value)
            @staticmethod
            def ulong_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
                return win_ddl.ulong_fetch_and_and(v, n.value)
            @staticmethod
            def ulong_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
                return win_ddl.ulong_fetch_and_or(v, n.value)
            @staticmethod
            def ulong_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
                return win_ddl.ulong_fetch_and_xor(v, n.value)
            @staticmethod
            def ulong_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
                return win_ddl.ulong_fetch_and_nand(v, n.value)

            @staticmethod
            def longlong_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.longlong_store(v, n)
            @staticmethod
            def longlong_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
                return win_ddl.longlong_shift(v, n, r)
            @staticmethod
            def longlong_get_and_set(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
                return win_ddl.longlong_get_and_set(v, n.value)
            @staticmethod
            def longlong_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_longlong) -> bool:
                return win_ddl.longlong_compare_and_set(v, e, n.value)

            @staticmethod
            def longlong_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
                return win_ddl.longlong_add_and_fetch(v, n.value)
            @staticmethod
            def longlong_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
                return win_ddl.longlong_sub_and_fetch(v, n.value)
            @staticmethod
            def longlong_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
                return win_ddl.longlong_and_and_fetch(v, n.value)
            @staticmethod
            def longlong_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
                return win_ddl.longlong_or_and_fetch(v, n.value)
            @staticmethod
            def longlong_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
                return win_ddl.longlong_xor_and_fetch(v, n.value)
            @staticmethod
            def longlong_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
                return win_ddl.longlong_nand_and_fetch(v, n.value)
            @staticmethod
            def longlong_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
                return win_ddl.longlong_fetch_and_add(v, n.value)
            @staticmethod
            def longlong_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
                return win_ddl.longlong_fetch_and_sub(v, n.value)
            @staticmethod
            def longlong_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
                return win_ddl.longlong_fetch_and_and(v, n.value)
            @staticmethod
            def longlong_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
                return win_ddl.longlong_fetch_and_or(v, n.value)
            @staticmethod
            def longlong_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
                return win_ddl.longlong_fetch_and_xor(v, n.value)
            @staticmethod
            def longlong_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
                return win_ddl.longlong_fetch_and_nand(v, n.value)


            @staticmethod
            def ulonglong_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.ulonglong_store(v, n)
            @staticmethod
            def ulonglong_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
                return win_ddl.ulonglong_shift(v, n, r)
            @staticmethod
            def ulonglong_get_and_set(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
                return win_ddl.ulonglong_get_and_set(v, n.value)
            @staticmethod
            def ulonglong_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_ulonglong) -> bool:
                return win_ddl.ulonglong_compare_and_set(v, e, n.value)

            @staticmethod
            def ulonglong_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
                return win_ddl.ulonglong_add_and_fetch(v, n.value)
            @staticmethod
            def ulonglong_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
                return win_ddl.ulonglong_sub_and_fetch(v, n.value)
            @staticmethod
            def ulonglong_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
                return win_ddl.ulonglong_and_and_fetch(v, n.value)
            @staticmethod
            def ulonglong_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
                return win_ddl.ulonglong_or_and_fetch(v, n.value)
            @staticmethod
            def ulonglong_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
                return win_ddl.ulonglong_xor_and_fetch(v, n.value)
            @staticmethod
            def ulonglong_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
                return win_ddl.ulonglong_nand_and_fetch(v, n.value)
            @staticmethod
            def ulonglong_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
                return win_ddl.ulonglong_fetch_and_add(v, n.value)
            @staticmethod
            def ulonglong_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
                return win_ddl.ulonglong_fetch_and_sub(v, n.value)
            @staticmethod
            def ulonglong_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
                return win_ddl.ulonglong_fetch_and_and(v, n.value)
            @staticmethod
            def ulonglong_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
                return win_ddl.ulonglong_fetch_and_or(v, n.value)
            @staticmethod
            def ulonglong_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
                return win_ddl.ulonglong_fetch_and_xor(v, n.value)
            @staticmethod
            def ulonglong_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
                return win_ddl.ulonglong_fetch_and_nand(v, n.value)

            @staticmethod
            def size_t_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.size_t_store(v, n)
            @staticmethod
            def size_t_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
                return win_ddl.size_t_shift(v, n, r)
            @staticmethod
            def size_t_get_and_set(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
                return win_ddl.size_t_get_and_set(v, n.value)
            @staticmethod
            def size_t_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_size_t) -> bool:
                return win_ddl.size_t_compare_and_set(v, e, n.value)

            @staticmethod
            def size_t_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
                return win_ddl.size_t_add_and_fetch(v, n.value)
            @staticmethod
            def size_t_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
                return win_ddl.size_t_sub_and_fetch(v, n.value)
            @staticmethod
            def size_t_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
                return win_ddl.size_t_and_and_fetch(v, n.value)
            @staticmethod
            def size_t_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
                return win_ddl.size_t_or_and_fetch(v, n.value)
            @staticmethod
            def size_t_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
                return win_ddl.size_t_xor_and_fetch(v, n.value)
            @staticmethod
            def size_t_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
                return win_ddl.size_t_nand_and_fetch(v, n.value)
            @staticmethod
            def size_t_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
                return win_ddl.size_t_fetch_and_add(v, n.value)
            @staticmethod
            def size_t_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
                return win_ddl.size_t_fetch_and_sub(v, n.value)
            @staticmethod
            def size_t_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
                return win_ddl.size_t_fetch_and_and(v, n.value)
            @staticmethod
            def size_t_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
                return win_ddl.size_t_fetch_and_or(v, n.value)
            @staticmethod
            def size_t_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
                return win_ddl.size_t_fetch_and_xor(v, n.value)
            @staticmethod
            def size_t_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
                return win_ddl.size_t_fetch_and_nand(v, n.value)



            @staticmethod
            def ssize_t_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
                win_ddl.ssize_t_store(v, n)
            @staticmethod
            def ssize_t_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
                return win_ddl.ssize_t_shift(v, n, r)
            @staticmethod
            def ssize_t_get_and_set(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
                return win_ddl.ssize_t_get_and_set(v, n.value)
            @staticmethod
            def ssize_t_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_ssize_t) -> bool:
                return win_ddl.ssize_t_compare_and_set(v, e, n.value)


            @staticmethod
            def ssize_t_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
                return win_ddl.ssize_t_add_and_fetch(v, n.value)
            @staticmethod
            def ssize_t_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
                return win_ddl.ssize_t_sub_and_fetch(v, n.value)
            @staticmethod
            def ssize_t_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
                return win_ddl.ssize_t_and_and_fetch(v, n.value)
            @staticmethod
            def ssize_t_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
                return win_ddl.ssize_t_or_and_fetch(v, n.value)
            @staticmethod
            def ssize_t_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
                return win_ddl.ssize_t_xor_and_fetch(v, n.value)
            @staticmethod
            def ssize_t_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
                return win_ddl.ssize_t_nand_and_fetch(v, n.value)
            @staticmethod
            def ssize_t_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
                return win_ddl.ssize_t_fetch_and_add(v, n.value)
            @staticmethod
            def ssize_t_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
                return win_ddl.ssize_t_fetch_and_sub(v, n.value)
            @staticmethod
            def ssize_t_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
                return win_ddl.ssize_t_fetch_and_and(v, n.value)
            @staticmethod
            def ssize_t_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
                return win_ddl.ssize_t_fetch_and_or(v, n.value)
            @staticmethod
            def ssize_t_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
                return win_ddl.ssize_t_fetch_and_xor(v, n.value)
            @staticmethod
            def ssize_t_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
                return win_ddl.ssize_t_fetch_and_nand(v, n.value)

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



from shared_atomic.atomic_bytearray import atomic_bytearray

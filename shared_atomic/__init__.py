import sys
import ctypes
from pathlib import Path
import sysconfig

def searchdll():
    result = None
    filepatten = {
        'darwin': {'PyPy': 'shared_atomic_.abi3.so',
                   '': 'shared_atomic_.abi3.so'},
        'linux': {'PyPy': 'shared_atomic_.abi3.so',
                  '': 'shared_atomic_.abi3.so'},
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
    return result

def loaddll():
    """
    function to load the dynamiclly linked library to scope

    :return: class with atomic operation functions as class method
    """

    if sys.platform in ('darwin', 'linux'):
        result = searchdll()

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
        from shared_atomic import win_dll
        return win_dll.ctypes_dll

    else:
        return

if sys.platform == 'win32':
    from shared_atomic import win_dll
    def load_wrapped_dll():
        return win_dll.native_dll


from shared_atomic.atomic_bytearray import atomic_bytearray
from shared_atomic.atomic_string import atomic_string
from shared_atomic.atomic_uint import atomic_uint
from shared_atomic.atomic_int import atomic_int
from shared_atomic.atomic_boolfloat import atomic_bool, atomic_float

from shared_atomic.atomic_uint import uint_store
from shared_atomic.atomic_uint import uint_shift
from shared_atomic.atomic_uint import uint_get_and_set
from shared_atomic.atomic_uint import uint_compare_and_set
from shared_atomic.atomic_uint import uint_add_and_fetch
from shared_atomic.atomic_uint import uint_sub_and_fetch
from shared_atomic.atomic_uint import uint_and_and_fetch
from shared_atomic.atomic_uint import uint_or_and_fetch
from shared_atomic.atomic_uint import uint_xor_and_fetch
from shared_atomic.atomic_uint import uint_nand_and_fetch
from shared_atomic.atomic_uint import uint_fetch_and_add
from shared_atomic.atomic_uint import uint_fetch_and_sub
from shared_atomic.atomic_uint import uint_fetch_and_and
from shared_atomic.atomic_uint import uint_fetch_and_or
from shared_atomic.atomic_uint import uint_fetch_and_xor
from shared_atomic.atomic_uint import uint_fetch_and_nand

from shared_atomic.atomic_int import int_store
from shared_atomic.atomic_int import int_shift
from shared_atomic.atomic_int import int_get_and_set
from shared_atomic.atomic_int import int_compare_and_set
from shared_atomic.atomic_int import int_add_and_fetch
from shared_atomic.atomic_int import int_sub_and_fetch
from shared_atomic.atomic_int import int_and_and_fetch
from shared_atomic.atomic_int import int_or_and_fetch
from shared_atomic.atomic_int import int_xor_and_fetch
from shared_atomic.atomic_int import int_nand_and_fetch
from shared_atomic.atomic_int import int_fetch_and_add
from shared_atomic.atomic_int import int_fetch_and_sub
from shared_atomic.atomic_int import int_fetch_and_and
from shared_atomic.atomic_int import int_fetch_and_or
from shared_atomic.atomic_int import int_fetch_and_xor
from shared_atomic.atomic_int import int_fetch_and_nand

from shared_atomic.atomic_boolfloat import bool_store
from shared_atomic.atomic_boolfloat import bool_shift
from shared_atomic.atomic_boolfloat import bool_get_and_set
from shared_atomic.atomic_boolfloat import bool_compare_and_set

from shared_atomic.atomic_boolfloat import float_store

try:
    import bitarray
    from shared_atomic.atomic_set import atomic_set
    from shared_atomic.atomic_list import atomic_list

except:
    ImportError
    pass

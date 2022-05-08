import ctypes
from pathlib import Path
import sys
import cppyy


win_dll = None

def signed2unsigned(input: int) -> int:
    return input if input >= 0 else input + 256

def unsigned2signed(input: int) -> int:
    return input if input < 128 else input - 256

def wchar2ushort(input: ctypes.c_wchar) -> int:
    return int.from_bytes(input.value.encode('utf-16-be'),
                          byteorder='big')
def ushort2wchar(input: int) -> str:
    return int.to_bytes(input, ctypes.sizeof(ctypes.c_wchar), byteorder='big').decode('utf-16-be')

def compile_win_dll():
    global win_dll
    if win_dll is None:
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
        win_dll = cppyy.gbl

class ctypes_dll:

    global win_dll
    if win_dll is None:
        compile_win_dll()
    @staticmethod
    def bool_load(v: ctypes.c_void_p):
        return win_dll.bool_load(v)

    @staticmethod
    def bool_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        win_dll.bool_store(v, n)

    @staticmethod
    def bool_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        return win_dll.bool_shift(v, n, r)

    @staticmethod
    def bool_get_and_set(v: ctypes.c_void_p, n: ctypes.c_bool) -> bool:
        return win_dll.bool_get_and_set(v, n)

    @staticmethod
    def bool_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_bool) -> bool:
        return win_dll.bool_compare_and_set(v, e, n)

    @staticmethod
    def byte_load(v: ctypes.c_void_p) -> int:
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ubyte))
        return unsigned2signed(int.from_bytes(
            win_dll.ubyte_load(v2).encode(encoding='latin1'),
            byteorder=sys.byteorder))

    @staticmethod
    def byte_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ubyte))
        n2 = ctypes.cast(n, ctypes.POINTER(ctypes.c_ubyte))
        win_dll.ubyte_store(v2, n2)

    @staticmethod
    def byte_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ubyte))
        n2 = ctypes.cast(n, ctypes.POINTER(ctypes.c_ubyte))
        r2 = ctypes.cast(r, ctypes.POINTER(ctypes.c_ubyte))
        return win_dll.ubyte_shift(v2, n2, r2)

    @staticmethod
    def byte_get_and_set(v: ctypes.c_void_p, n: ctypes.c_byte) -> int:
        unsigned = signed2unsigned(n.value)
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ubyte))
        return unsigned2signed(int.from_bytes(
            win_dll.ubyte_get_and_set(v2, unsigned).encode(encoding='latin1'),
            byteorder=sys.byteorder))

    @staticmethod
    def byte_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_byte) -> bool:
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ubyte))
        e2 = ctypes.cast(e, ctypes.POINTER(ctypes.c_ubyte))
        unsigned = signed2unsigned(n.value)
        return win_dll.ubyte_compare_and_set(v2, e2, unsigned)

    @staticmethod
    def byte_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_byte) -> int:
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ubyte))
        unsigned = signed2unsigned(n.value)
        return unsigned2signed(int.from_bytes(
            win_dll.ubyte_add_and_fetch(v2, unsigned).encode(encoding='latin1'),
            byteorder=sys.byteorder))

    @staticmethod
    def byte_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_byte) -> int:
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ubyte))
        unsigned = signed2unsigned(n.value)
        return unsigned2signed(int.from_bytes(
            win_dll.ubyte_sub_and_fetch(v2, unsigned).encode(encoding='latin1'),
            byteorder=sys.byteorder))

    @staticmethod
    def byte_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_byte) -> int:
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ubyte))
        unsigned = signed2unsigned(n.value)
        return unsigned2signed(int.from_bytes(
            win_dll.ubyte_and_and_fetch(v2, unsigned).encode(encoding='latin1'),
            byteorder=sys.byteorder))

    @staticmethod
    def byte_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_byte) -> int:
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ubyte))
        unsigned = signed2unsigned(n.value)
        return unsigned2signed(int.from_bytes(
            win_dll.ubyte_or_and_fetch(v2, unsigned).encode(encoding='latin1'),
            byteorder=sys.byteorder))

    @staticmethod
    def byte_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_byte) -> int:
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ubyte))
        unsigned = signed2unsigned(n.value)
        return unsigned2signed(int.from_bytes(
            win_dll.ubyte_xor_and_fetch(v2, unsigned).encode(encoding='latin1'),
            byteorder=sys.byteorder))

    @staticmethod
    def byte_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_byte) -> int:
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ubyte))
        unsigned = signed2unsigned(n.value)
        return unsigned2signed(int.from_bytes(
            win_dll.ubyte_nand_and_fetch(v2, unsigned).encode(encoding='latin1'),
            byteorder=sys.byteorder))

    @staticmethod
    def byte_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_byte) -> int:
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ubyte))
        unsigned = signed2unsigned(n.value)
        return unsigned2signed(int.from_bytes(
            win_dll.ubyte_fetch_and_add(v2, unsigned).encode(encoding='latin1'),
            byteorder=sys.byteorder))

    @staticmethod
    def byte_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_byte) -> int:
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ubyte))
        unsigned = signed2unsigned(n.value)
        return unsigned2signed(int.from_bytes(
            win_dll.ubyte_fetch_and_sub(v2, unsigned).encode(encoding='latin1'),
            byteorder=sys.byteorder))

    @staticmethod
    def byte_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_byte) -> int:
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ubyte))
        unsigned = signed2unsigned(n.value)
        return unsigned2signed(int.from_bytes(
            win_dll.ubyte_fetch_and_and(v2, unsigned).encode(encoding='latin1'),
            byteorder=sys.byteorder))

    @staticmethod
    def byte_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_ubyte) -> int:
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ubyte))
        unsigned = signed2unsigned(n.value)
        return unsigned2signed(int.from_bytes(
            win_dll.ubyte_fetch_and_or(v2, unsigned).encode(encoding='latin1'),
            byteorder=sys.byteorder))

    @staticmethod
    def byte_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_ubyte) -> int:
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ubyte))
        unsigned = signed2unsigned(n.value)
        return unsigned2signed(int.from_bytes(
            win_dll.ubyte_fetch_and_xor(v2, unsigned).encode(encoding='latin1'),
            byteorder=sys.byteorder))

    @staticmethod
    def byte_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_ubyte) -> int:
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ubyte))
        unsigned = signed2unsigned(n.value)
        return unsigned2signed(int.from_bytes(
            win_dll.ubyte_fetch_and_nand(v2, unsigned).encode(encoding='latin1'),
            byteorder=sys.byteorder))

    @staticmethod
    def ubyte_load(v: ctypes.c_void_p) -> int:
        return int.from_bytes(win_dll.ubyte_load(v).encode(encoding='latin1'), byteorder=sys.byteorder)

    @staticmethod
    def ubyte_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        win_dll.ubyte_store(v, n)

    @staticmethod
    def ubyte_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        return win_dll.ubyte_shift(v, n, r)

    @staticmethod
    def ubyte_get_and_set(v: ctypes.c_void_p, n: ctypes.c_ubyte) -> int:
        return int.from_bytes(win_dll.ubyte_get_and_set(v, n.value).encode(encoding='latin1'), byteorder=sys.byteorder)

    @staticmethod
    def ubyte_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_ubyte) -> bool:
        return win_dll.ubyte_compare_and_set(v, e, n.value)

    @staticmethod
    def ubyte_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ubyte) -> int:
        return int.from_bytes(win_dll.ubyte_add_and_fetch(v, n.value).encode(encoding='latin1'),
                              byteorder=sys.byteorder)

    @staticmethod
    def ubyte_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ubyte) -> int:
        return int.from_bytes(win_dll.ubyte_sub_and_fetch(v, n.value).encode(encoding='latin1'),
                              byteorder=sys.byteorder)

    @staticmethod
    def ubyte_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ubyte) -> int:
        return int.from_bytes(win_dll.ubyte_and_and_fetch(v, n.value).encode(encoding='latin1'),
                              byteorder=sys.byteorder)

    @staticmethod
    def ubyte_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ubyte) -> int:
        return int.from_bytes(win_dll.ubyte_or_and_fetch(v, n.value).encode(encoding='latin1'), byteorder=sys.byteorder)

    @staticmethod
    def ubyte_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ubyte) -> int:
        return int.from_bytes(win_dll.ubyte_xor_and_fetch(v, n.value).encode(encoding='latin1'),
                              byteorder=sys.byteorder)

    @staticmethod
    def ubyte_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ubyte) -> int:
        return int.from_bytes(win_dll.ubyte_nand_and_fetch(v, n.value).encode(encoding='latin1'),
                              byteorder=sys.byteorder)

    @staticmethod
    def ubyte_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_ubyte) -> int:
        return int.from_bytes(win_dll.ubyte_fetch_and_add(v, n.value).encode(encoding='latin1'),
                              byteorder=sys.byteorder)

    @staticmethod
    def ubyte_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_ubyte) -> int:
        return int.from_bytes(win_dll.ubyte_fetch_and_sub(v, n.value).encode(encoding='latin1'),
                              byteorder=sys.byteorder)

    @staticmethod
    def ubyte_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_ubyte) -> int:
        return int.from_bytes(win_dll.ubyte_fetch_and_and(v, n.value).encode(encoding='latin1'),
                              byteorder=sys.byteorder)

    @staticmethod
    def ubyte_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_ubyte) -> int:
        return int.from_bytes(win_dll.ubyte_fetch_and_or(v, n.value).encode(encoding='latin1'), byteorder=sys.byteorder)

    @staticmethod
    def ubyte_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_ubyte) -> int:
        return int.from_bytes(win_dll.ubyte_fetch_and_xor(v, n.value).encode(encoding='latin1'),
                              byteorder=sys.byteorder)

    @staticmethod
    def ubyte_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_ubyte) -> int:
        return int.from_bytes(win_dll.ubyte_fetch_and_nand(v, n.value).encode(encoding='latin1'),
                              byteorder=sys.byteorder)

    @staticmethod
    def wchar_load(v: ctypes.c_void_p) -> str:
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ushort))
        return ushort2wchar(win_dll.ushort_load(v2))

    @staticmethod
    def wchar_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ushort))
        n2 = ctypes.cast(n, ctypes.POINTER(ctypes.c_ushort))
        win_dll.ushort_store(v2, n2)

    @staticmethod
    def wchar_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ushort))
        n2 = ctypes.cast(n, ctypes.POINTER(ctypes.c_ushort))
        r2 = ctypes.cast(r, ctypes.POINTER(ctypes.c_ushort))
        return win_dll.ushort_shift(v2, n2, r2)

    @staticmethod
    def wchar_get_and_set(v: ctypes.c_void_p, n: ctypes.c_wchar) -> str:
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ushort))
        unsigned = wchar2ushort(n)
        return ushort2wchar(win_dll.ushort_get_and_set(v2, unsigned))

    @staticmethod
    def wchar_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_wchar) -> bool:
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ushort))
        e2 = ctypes.cast(e, ctypes.POINTER(ctypes.c_ushort))
        unsigned = wchar2ushort(n)
        return win_dll.ushort_compare_and_set(v2, e2, unsigned)

    @staticmethod
    def wchar_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_wchar) -> str:
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ushort))
        unsigned = wchar2ushort(n)
        return ushort2wchar(win_dll.ushort_add_and_fetch(v2, unsigned))

    @staticmethod
    def wchar_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_wchar) -> str:
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ushort))
        unsigned = wchar2ushort(n)
        return ushort2wchar(win_dll.ushort_sub_and_fetch(v2, unsigned))

    @staticmethod
    def wchar_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_wchar) -> str:
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ushort))
        unsigned = wchar2ushort(n)
        return ushort2wchar(win_dll.ushort_fetch_and_add(v2, unsigned))

    @staticmethod
    def wchar_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_wchar) -> str:
        v2 = ctypes.cast(v, ctypes.POINTER(ctypes.c_ushort))
        unsigned = wchar2ushort(n)
        return ushort2wchar(win_dll.ushort_fetch_and_sub(v2, unsigned))

    @staticmethod
    def short_load(v: ctypes.c_void_p) -> int:
        return win_dll.short_load(v)

    @staticmethod
    def short_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        win_dll.short_store(v, n)

    @staticmethod
    def short_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        return win_dll.short_shift(v, n, r)

    @staticmethod
    def short_get_and_set(v: ctypes.c_void_p, n: ctypes.c_short) -> int:
        return win_dll.short_get_and_set(v, n.value)

    @staticmethod
    def short_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_short) -> bool:
        return win_dll.short_compare_and_set(v, e, n.value)

    @staticmethod
    def short_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_short) -> int:
        return win_dll.short_add_and_fetch(v, n.value)

    @staticmethod
    def short_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_short) -> int:
        return win_dll.short_sub_and_fetch(v, n.value)

    @staticmethod
    def short_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_short) -> int:
        return win_dll.short_and_and_fetch(v, n.value)

    @staticmethod
    def short_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_short) -> int:
        return win_dll.short_or_and_fetch(v, n.value)

    @staticmethod
    def short_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_short) -> int:
        return win_dll.short_xor_and_fetch(v, n.value)

    @staticmethod
    def short_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_short) -> int:
        return win_dll.short_nand_and_fetch(v, n.value)

    @staticmethod
    def short_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_short) -> int:
        return win_dll.short_fetch_and_add(v, n.value)

    @staticmethod
    def short_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_short) -> int:
        return win_dll.short_fetch_and_sub(v, n.value)

    @staticmethod
    def short_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_short) -> int:
        return win_dll.short_fetch_and_and(v, n.value)

    @staticmethod
    def short_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_short) -> int:
        return win_dll.short_fetch_and_or(v, n.value)

    @staticmethod
    def short_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_short) -> int:
        return win_dll.short_fetch_and_xor(v, n.value)

    @staticmethod
    def short_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_short) -> int:
        return win_dll.short_fetch_and_nand(v, n.value)

    @staticmethod
    def ushort_load(v: ctypes.c_void_p) -> int:
        return win_dll.ushort_load(v)

    @staticmethod
    def ushort_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        win_dll.ushort_store(v, n)

    @staticmethod
    def ushort_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        return win_dll.ushort_shift(v, n, r)

    @staticmethod
    def ushort_get_and_set(v: ctypes.c_void_p, n: ctypes.c_ushort) -> int:
        return win_dll.ushort_get_and_set(v, n.value)

    @staticmethod
    def ushort_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_ushort) -> bool:
        return win_dll.ushort_compare_and_set(v, e, n.value)

    @staticmethod
    def ushort_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ushort) -> int:
        return win_dll.ushort_add_and_fetch(v, n.value)

    @staticmethod
    def ushort_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ushort) -> int:
        return win_dll.ushort_sub_and_fetch(v, n.value)

    @staticmethod
    def ushort_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ushort) -> int:
        return win_dll.ushort_and_and_fetch(v, n.value)

    @staticmethod
    def ushort_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ushort) -> int:
        return win_dll.ushort_or_and_fetch(v, n.value)

    @staticmethod
    def ushort_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ushort) -> int:
        return win_dll.ushort_xor_and_fetch(v, n.value)

    @staticmethod
    def ushort_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ushort) -> int:
        return win_dll.ushort_nand_and_fetch(v, n.value)

    @staticmethod
    def ushort_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_ushort) -> int:
        return win_dll.ushort_fetch_and_add(v, n.value)

    @staticmethod
    def ushort_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_ushort) -> int:
        return win_dll.ushort_fetch_and_sub(v, n.value)

    @staticmethod
    def ushort_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_ushort) -> int:
        return win_dll.ushort_fetch_and_and(v, n.value)

    @staticmethod
    def ushort_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_ushort) -> int:
        return win_dll.ushort_fetch_and_or(v, n.value)

    @staticmethod
    def ushort_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_ushort) -> int:
        return win_dll.ushort_fetch_and_xor(v, n.value)

    @staticmethod
    def ushort_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_ushort) -> int:
        return win_dll.ushort_fetch_and_nand(v, n.value)

    @staticmethod
    def int_load(v: ctypes.c_void_p) -> int:
        return win_dll.int_load(v)

    @staticmethod
    def int_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        win_dll.int_store(v, n)

    @staticmethod
    def int_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        return win_dll.int_shift(v, n, r)

    @staticmethod
    def int_get_and_set(v: ctypes.c_void_p, n: ctypes.c_int) -> int:
        return win_dll.int_get_and_set(v, n.value)

    @staticmethod
    def int_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_int) -> bool:
        return win_dll.int_compare_and_set(v, e, n.value)

    @staticmethod
    def int_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_int) -> int:
        return win_dll.int_add_and_fetch(v, n.value)

    @staticmethod
    def int_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_int) -> int:
        return win_dll.int_sub_and_fetch(v, n.value)

    @staticmethod
    def int_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_int) -> int:
        return win_dll.int_and_and_fetch(v, n.value)

    @staticmethod
    def int_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_int) -> int:
        return win_dll.int_or_and_fetch(v, n.value)

    @staticmethod
    def int_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_int) -> int:
        return win_dll.int_xor_and_fetch(v, n.value)

    @staticmethod
    def int_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_int) -> int:
        return win_dll.int_nand_and_fetch(v, n.value)

    @staticmethod
    def int_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_int) -> int:
        return win_dll.int_fetch_and_add(v, n.value)

    @staticmethod
    def int_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_int) -> int:
        return win_dll.int_fetch_and_sub(v, n.value)

    @staticmethod
    def int_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_int) -> int:
        return win_dll.int_fetch_and_and(v, n.value)

    @staticmethod
    def int_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_int) -> int:
        return win_dll.int_fetch_and_or(v, n.value)

    @staticmethod
    def int_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_int) -> int:
        return win_dll.int_fetch_and_xor(v, n.value)

    @staticmethod
    def int_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_int) -> int:
        return win_dll.int_fetch_and_nand(v, n.value)

    @staticmethod
    def uint_load(v: ctypes.c_void_p) -> int:
        return win_dll.uint_load(v)

    @staticmethod
    def uint_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        win_dll.uint_store(v, n)

    @staticmethod
    def uint_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        return win_dll.uint_shift(v, n, r)

    @staticmethod
    def uint_get_and_set(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
        return win_dll.uint_get_and_set(v, n.value)

    @staticmethod
    def uint_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_uint) -> bool:
        return win_dll.uint_compare_and_set(v, e, n.value)

    @staticmethod
    def uint_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
        return win_dll.uint_add_and_fetch(v, n.value)

    @staticmethod
    def uint_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
        return win_dll.uint_sub_and_fetch(v, n.value)

    @staticmethod
    def uint_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
        return win_dll.uint_and_and_fetch(v, n.value)

    @staticmethod
    def uint_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
        return win_dll.uint_or_and_fetch(v, n.value)

    @staticmethod
    def uint_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
        return win_dll.uint_xor_and_fetch(v, n.value)

    @staticmethod
    def uint_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
        return win_dll.uint_nand_and_fetch(v, n.value)

    @staticmethod
    def uint_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
        return win_dll.uint_fetch_and_add(v, n.value)

    @staticmethod
    def uint_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
        return win_dll.uint_fetch_and_sub(v, n.value)

    @staticmethod
    def uint_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
        return win_dll.uint_fetch_and_and(v, n.value)

    @staticmethod
    def uint_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
        return win_dll.uint_fetch_and_or(v, n.value)

    @staticmethod
    def uint_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
        return win_dll.uint_fetch_and_xor(v, n.value)

    @staticmethod
    def uint_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_uint) -> int:
        return win_dll.uint_fetch_and_nand(v, n.value)

    @staticmethod
    def long_load(v: ctypes.c_void_p) -> int:
        return win_dll.long_load(v)

    @staticmethod
    def long_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        win_dll.long_store(v, n)

    @staticmethod
    def long_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        return win_dll.long_shift(v, n, r)

    @staticmethod
    def long_get_and_set(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
        return win_dll.long_get_and_set(v, n.value)

    @staticmethod
    def long_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_long) -> bool:
        return win_dll.long_compare_and_set(v, e, n.value)

    @staticmethod
    def long_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
        return win_dll.long_add_and_fetch(v, n.value)

    @staticmethod
    def long_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
        return win_dll.long_sub_and_fetch(v, n.value)

    @staticmethod
    def long_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
        return win_dll.long_and_and_fetch(v, n.value)

    @staticmethod
    def long_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
        return win_dll.long_or_and_fetch(v, n.value)

    @staticmethod
    def long_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
        return win_dll.long_xor_and_fetch(v, n.value)

    @staticmethod
    def long_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
        return win_dll.long_nand_and_fetch(v, n.value)

    @staticmethod
    def long_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
        return win_dll.long_fetch_and_add(v, n.value)

    @staticmethod
    def long_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
        return win_dll.long_fetch_and_sub(v, n.value)

    @staticmethod
    def long_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
        return win_dll.long_fetch_and_and(v, n.value)

    @staticmethod
    def long_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
        return win_dll.long_fetch_and_or(v, n.value)

    @staticmethod
    def long_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
        return win_dll.long_fetch_and_xor(v, n.value)

    @staticmethod
    def long_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_long) -> int:
        return win_dll.long_fetch_and_nand(v, n.value)

    @staticmethod
    def ulong_load(v: ctypes.c_void_p) -> int:
        return win_dll.ulong_load(v)

    @staticmethod
    def ulong_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        win_dll.ulong_store(v, n)

    @staticmethod
    def ulong_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        return win_dll.ulong_shift(v, n, r)

    @staticmethod
    def ulong_get_and_set(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
        return win_dll.ulong_get_and_set(v, n.value)

    @staticmethod
    def ulong_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_ulong) -> bool:
        return win_dll.ulong_compare_and_set(v, e, n.value)

    @staticmethod
    def ulong_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
        return win_dll.ulong_add_and_fetch(v, n.value)

    @staticmethod
    def ulong_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
        return win_dll.ulong_sub_and_fetch(v, n.value)

    @staticmethod
    def ulong_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
        return win_dll.ulong_and_and_fetch(v, n.value)

    @staticmethod
    def ulong_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
        return win_dll.ulong_or_and_fetch(v, n.value)

    @staticmethod
    def ulong_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
        return win_dll.ulong_xor_and_fetch(v, n.value)

    @staticmethod
    def ulong_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
        return win_dll.ulong_nand_and_fetch(v, n.value)

    @staticmethod
    def ulong_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
        return win_dll.ulong_fetch_and_add(v, n.value)

    @staticmethod
    def ulong_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
        return win_dll.ulong_fetch_and_sub(v, n.value)

    @staticmethod
    def ulong_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
        return win_dll.ulong_fetch_and_and(v, n.value)

    @staticmethod
    def ulong_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
        return win_dll.ulong_fetch_and_or(v, n.value)

    @staticmethod
    def ulong_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
        return win_dll.ulong_fetch_and_xor(v, n.value)

    @staticmethod
    def ulong_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_ulong) -> int:
        return win_dll.ulong_fetch_and_nand(v, n.value)

    @staticmethod
    def longlong_load(v: ctypes.c_void_p) -> int:
        return win_dll.longlong_load(v)

    @staticmethod
    def longlong_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        win_dll.longlong_store(v, n)

    @staticmethod
    def longlong_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        return win_dll.longlong_shift(v, n, r)

    @staticmethod
    def longlong_get_and_set(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
        return win_dll.longlong_get_and_set(v, n.value)

    @staticmethod
    def longlong_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_longlong) -> bool:
        return win_dll.longlong_compare_and_set(v, e, n.value)

    @staticmethod
    def longlong_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
        return win_dll.longlong_add_and_fetch(v, n.value)

    @staticmethod
    def longlong_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
        return win_dll.longlong_sub_and_fetch(v, n.value)

    @staticmethod
    def longlong_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
        return win_dll.longlong_and_and_fetch(v, n.value)

    @staticmethod
    def longlong_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
        return win_dll.longlong_or_and_fetch(v, n.value)

    @staticmethod
    def longlong_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
        return win_dll.longlong_xor_and_fetch(v, n.value)

    @staticmethod
    def longlong_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
        return win_dll.longlong_nand_and_fetch(v, n.value)

    @staticmethod
    def longlong_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
        return win_dll.longlong_fetch_and_add(v, n.value)

    @staticmethod
    def longlong_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
        return win_dll.longlong_fetch_and_sub(v, n.value)

    @staticmethod
    def longlong_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
        return win_dll.longlong_fetch_and_and(v, n.value)

    @staticmethod
    def longlong_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
        return win_dll.longlong_fetch_and_or(v, n.value)

    @staticmethod
    def longlong_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
        return win_dll.longlong_fetch_and_xor(v, n.value)

    @staticmethod
    def longlong_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_longlong) -> int:
        return win_dll.longlong_fetch_and_nand(v, n.value)

    @staticmethod
    def ulonglong_load(v: ctypes.c_void_p) -> int:
        return win_dll.ulonglong_load(v)

    @staticmethod
    def ulonglong_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        win_dll.ulonglong_store(v, n)

    @staticmethod
    def ulonglong_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        return win_dll.ulonglong_shift(v, n, r)

    @staticmethod
    def ulonglong_get_and_set(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
        return win_dll.ulonglong_get_and_set(v, n.value)

    @staticmethod
    def ulonglong_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_ulonglong) -> bool:
        return win_dll.ulonglong_compare_and_set(v, e, n.value)

    @staticmethod
    def ulonglong_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
        return win_dll.ulonglong_add_and_fetch(v, n.value)

    @staticmethod
    def ulonglong_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
        return win_dll.ulonglong_sub_and_fetch(v, n.value)

    @staticmethod
    def ulonglong_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
        return win_dll.ulonglong_and_and_fetch(v, n.value)

    @staticmethod
    def ulonglong_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
        return win_dll.ulonglong_or_and_fetch(v, n.value)

    @staticmethod
    def ulonglong_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
        return win_dll.ulonglong_xor_and_fetch(v, n.value)

    @staticmethod
    def ulonglong_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
        return win_dll.ulonglong_nand_and_fetch(v, n.value)

    @staticmethod
    def ulonglong_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
        return win_dll.ulonglong_fetch_and_add(v, n.value)

    @staticmethod
    def ulonglong_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
        return win_dll.ulonglong_fetch_and_sub(v, n.value)

    @staticmethod
    def ulonglong_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
        return win_dll.ulonglong_fetch_and_and(v, n.value)

    @staticmethod
    def ulonglong_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
        return win_dll.ulonglong_fetch_and_or(v, n.value)

    @staticmethod
    def ulonglong_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
        return win_dll.ulonglong_fetch_and_xor(v, n.value)

    @staticmethod
    def ulonglong_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_ulonglong) -> int:
        return win_dll.ulonglong_fetch_and_nand(v, n.value)

    @staticmethod
    def size_t_load(v: ctypes.c_void_p) -> int:
        return win_dll.size_t_load(v)

    @staticmethod
    def size_t_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        win_dll.size_t_store(v, n)

    @staticmethod
    def size_t_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        return win_dll.size_t_shift(v, n, r)

    @staticmethod
    def size_t_get_and_set(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
        return win_dll.size_t_get_and_set(v, n.value)

    @staticmethod
    def size_t_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_size_t) -> bool:
        return win_dll.size_t_compare_and_set(v, e, n.value)

    @staticmethod
    def size_t_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
        return win_dll.size_t_add_and_fetch(v, n.value)

    @staticmethod
    def size_t_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
        return win_dll.size_t_sub_and_fetch(v, n.value)

    @staticmethod
    def size_t_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
        return win_dll.size_t_and_and_fetch(v, n.value)

    @staticmethod
    def size_t_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
        return win_dll.size_t_or_and_fetch(v, n.value)

    @staticmethod
    def size_t_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
        return win_dll.size_t_xor_and_fetch(v, n.value)

    @staticmethod
    def size_t_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
        return win_dll.size_t_nand_and_fetch(v, n.value)

    @staticmethod
    def size_t_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
        return win_dll.size_t_fetch_and_add(v, n.value)

    @staticmethod
    def size_t_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
        return win_dll.size_t_fetch_and_sub(v, n.value)

    @staticmethod
    def size_t_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
        return win_dll.size_t_fetch_and_and(v, n.value)

    @staticmethod
    def size_t_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
        return win_dll.size_t_fetch_and_or(v, n.value)

    @staticmethod
    def size_t_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
        return win_dll.size_t_fetch_and_xor(v, n.value)

    @staticmethod
    def size_t_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_size_t) -> int:
        return win_dll.size_t_fetch_and_nand(v, n.value)

    @staticmethod
    def ssize_t_load(v: ctypes.c_void_p) -> int:
        return win_dll.ssize_t_load(v)

    @staticmethod
    def ssize_t_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        win_dll.ssize_t_store(v, n)

    @staticmethod
    def ssize_t_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        return win_dll.ssize_t_shift(v, n, r)

    @staticmethod
    def ssize_t_get_and_set(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
        return win_dll.ssize_t_get_and_set(v, n.value)

    @staticmethod
    def ssize_t_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: ctypes.c_ssize_t) -> bool:
        return win_dll.ssize_t_compare_and_set(v, e, n.value)

    @staticmethod
    def ssize_t_add_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
        return win_dll.ssize_t_add_and_fetch(v, n.value)

    @staticmethod
    def ssize_t_sub_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
        return win_dll.ssize_t_sub_and_fetch(v, n.value)

    @staticmethod
    def ssize_t_and_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
        return win_dll.ssize_t_and_and_fetch(v, n.value)

    @staticmethod
    def ssize_t_or_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
        return win_dll.ssize_t_or_and_fetch(v, n.value)

    @staticmethod
    def ssize_t_xor_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
        return win_dll.ssize_t_xor_and_fetch(v, n.value)

    @staticmethod
    def ssize_t_nand_and_fetch(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
        return win_dll.ssize_t_nand_and_fetch(v, n.value)

    @staticmethod
    def ssize_t_fetch_and_add(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
        return win_dll.ssize_t_fetch_and_add(v, n.value)

    @staticmethod
    def ssize_t_fetch_and_sub(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
        return win_dll.ssize_t_fetch_and_sub(v, n.value)

    @staticmethod
    def ssize_t_fetch_and_and(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
        return win_dll.ssize_t_fetch_and_and(v, n.value)

    @staticmethod
    def ssize_t_fetch_and_or(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
        return win_dll.ssize_t_fetch_and_or(v, n.value)

    @staticmethod
    def ssize_t_fetch_and_xor(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
        return win_dll.ssize_t_fetch_and_xor(v, n.value)

    @staticmethod
    def ssize_t_fetch_and_nand(v: ctypes.c_void_p, n: ctypes.c_ssize_t) -> int:
        return win_dll.ssize_t_fetch_and_nand(v, n.value)

    @staticmethod
    def float_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        win_dll.float_store(v, n)

    @staticmethod
    def double_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        win_dll.double_store(v, n)

    @staticmethod
    def longdouble_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        win_dll.longdouble_store(v, n)

class native_dll:

    @staticmethod
    def bool_load(v: ctypes.c_void_p):
        ctypes_dll.bool_load(v)

    @staticmethod
    def bool_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        ctypes_dll.bool_store(v, n)

    @staticmethod
    def bool_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        ctypes_dll.bool_shift(v, n, r)

    @staticmethod
    def bool_get_and_set(v: ctypes.c_void_p, n: bool) -> bool:
        n = ctypes.c_bool(n)
        return ctypes_dll.bool_get_and_set(v, n)

    @staticmethod
    def bool_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: bool) -> bool:
        n = ctypes.c_bool(n)
        return ctypes_dll.bool_compare_and_set(v, e, n)

    @staticmethod
    def byte_load(v: ctypes.c_void_p) -> int:
        return ctypes_dll.byte_load(v)

    @staticmethod
    def byte_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        ctypes_dll.byte_store(v, n)

    @staticmethod
    def byte_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        ctypes_dll.byte_shift(v, n, r)

    @staticmethod
    def byte_get_and_set(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_byte(n)
        return ctypes_dll.byte_get_and_set(v, n)

    @staticmethod
    def byte_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: int) -> bool:
        n = ctypes.c_byte(n)
        return ctypes_dll.byte_compare_and_set(v, e, n)

    @staticmethod
    def byte_add_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_byte(n)
        return ctypes_dll.byte_add_and_fetch(v, n)

    @staticmethod
    def byte_sub_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_byte(n)
        return ctypes_dll.byte_sub_and_fetch(v, n)

    @staticmethod
    def byte_and_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_byte(n)
        return ctypes_dll.byte_and_and_fetch(v, n)

    @staticmethod
    def byte_or_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_byte(n)
        return ctypes_dll.byte_or_and_fetch(v, n)

    @staticmethod
    def byte_xor_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_byte(n)
        return ctypes_dll.byte_xor_and_fetch(v, n)

    @staticmethod
    def byte_nand_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_byte(n)
        return ctypes_dll.byte_nand_and_fetch(v, n)

    @staticmethod
    def byte_fetch_and_add(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_byte(n)
        return ctypes_dll.byte_fetch_and_add(v, n)

    @staticmethod
    def byte_fetch_and_sub(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_byte(n)
        return ctypes_dll.byte_fetch_and_sub(v, n)

    @staticmethod
    def byte_fetch_and_and(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_byte(n)
        return ctypes_dll.byte_fetch_and_and(v, n)

    @staticmethod
    def byte_fetch_and_or(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_byte(n)
        return ctypes_dll.byte_fetch_and_or(v, n)

    @staticmethod
    def byte_fetch_and_xor(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_byte(n)
        return ctypes_dll.byte_fetch_and_xor(v, n)

    @staticmethod
    def byte_fetch_and_nand(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_byte(n)
        return ctypes_dll.byte_fetch_and_nand(v, n)

    @staticmethod
    def ubyte_load(v: ctypes.c_void_p) -> int:
        return ctypes_dll.ubyte_load(v)

    @staticmethod
    def ubyte_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        ctypes_dll.ubyte_store(v, n)

    @staticmethod
    def ubyte_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        ctypes_dll.ubyte_shift(v, n, r)

    @staticmethod
    def ubyte_get_and_set(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ubyte(n)
        return ctypes_dll.ubyte_get_and_set(v, n)

    @staticmethod
    def ubyte_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: int) -> bool:
        n = ctypes.c_ubyte(n)
        return ctypes_dll.ubyte_compare_and_set(v, e, n)

    @staticmethod
    def ubyte_add_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ubyte(n)
        return ctypes_dll.ubyte_add_and_fetch(v, n)

    @staticmethod
    def ubyte_sub_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ubyte(n)
        return ctypes_dll.ubyte_sub_and_fetch(v, n)

    @staticmethod
    def ubyte_and_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ubyte(n)
        return ctypes_dll.ubyte_and_and_fetch(v, n)

    @staticmethod
    def ubyte_or_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ubyte(n)
        return ctypes_dll.ubyte_or_and_fetch(v, n)

    @staticmethod
    def ubyte_xor_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ubyte(n)
        return ctypes_dll.ubyte_xor_and_fetch(v, n)

    @staticmethod
    def ubyte_nand_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ubyte(n)
        return ctypes_dll.ubyte_nand_and_fetch(v, n)

    @staticmethod
    def ubyte_fetch_and_add(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ubyte(n)
        return ctypes_dll.ubyte_fetch_and_add(v, n)

    @staticmethod
    def ubyte_fetch_and_sub(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ubyte(n)
        return ctypes_dll.ubyte_fetch_and_sub(v, n)

    @staticmethod
    def ubyte_fetch_and_and(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ubyte(n)
        return ctypes_dll.ubyte_fetch_and_and(v, n)

    @staticmethod
    def ubyte_fetch_and_or(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ubyte(n)
        return ctypes_dll.ubyte_fetch_and_or(v, n)

    @staticmethod
    def ubyte_fetch_and_xor(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ubyte(n)
        return ctypes_dll.ubyte_fetch_and_xor(v, n)

    @staticmethod
    def ubyte_fetch_and_nand(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ubyte(n)
        return ctypes_dll.ubyte_fetch_and_nand(v, n)

    @staticmethod
    def wchar_load(v: ctypes.c_void_p) -> str:
        return ctypes_dll.wchar_load(v)

    @staticmethod
    def wchar_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        ctypes_dll.wchar_store(v, n)

    @staticmethod
    def wchar_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        ctypes_dll.wchar_shift(v, n, r)

    @staticmethod
    def wchar_get_and_set(v: ctypes.c_void_p, n: str) -> str:
        n = ctypes.c_wchar(n)
        return ctypes_dll.wchar_get_and_set(v, n)

    @staticmethod
    def wchar_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: str) -> bool:
        n = ctypes.c_wchar(n)
        return ctypes_dll.wchar_compare_and_set(v, e, n)

    @staticmethod
    def wchar_add_and_fetch(v: ctypes.c_void_p, n: str) -> str:
        n = ctypes.c_wchar(n)
        return ctypes_dll.wchar_add_and_fetch(v, n)

    @staticmethod
    def wchar_sub_and_fetch(v: ctypes.c_void_p, n: str) -> str:
        n = ctypes.c_wchar(n)
        return ctypes_dll.wchar_sub_and_fetch(v, n)

    @staticmethod
    def wchar_fetch_and_add(v: ctypes.c_void_p, n: str) -> str:
        n = ctypes.c_wchar(n)
        return ctypes_dll.wchar_fetch_and_add(v, n)

    @staticmethod
    def wchar_fetch_and_sub(v: ctypes.c_void_p, n: str) -> str:
        n = ctypes.c_wchar(n)
        return ctypes_dll.wchar_fetch_and_sub(v, n)

    @staticmethod
    def short_load(v: ctypes.c_void_p) -> int:
        return ctypes_dll.short_load(v)

    @staticmethod
    def short_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        ctypes_dll.short_store(v, n)

    @staticmethod
    def short_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        ctypes_dll.short_shift(v, n, r)

    @staticmethod
    def short_get_and_set(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_short(n)
        return ctypes_dll.short_get_and_set(v, n)

    @staticmethod
    def short_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: int) -> bool:
        n = ctypes.c_short(n)
        return ctypes_dll.short_compare_and_set(v, e, n)

    @staticmethod
    def short_add_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_short(n)
        return ctypes_dll.short_add_and_fetch(v, n)

    @staticmethod
    def short_sub_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_short(n)
        return ctypes_dll.short_sub_and_fetch(v, n)

    @staticmethod
    def short_and_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_short(n)
        return ctypes_dll.short_and_and_fetch(v, n)

    @staticmethod
    def short_or_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_short(n)
        return ctypes_dll.short_or_and_fetch(v, n)

    @staticmethod
    def short_xor_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_short(n)
        return ctypes_dll.short_xor_and_fetch(v, n)

    @staticmethod
    def short_nand_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_short(n)
        return ctypes_dll.short_nand_and_fetch(v, n)

    @staticmethod
    def short_fetch_and_add(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_short(n)
        return ctypes_dll.short_fetch_and_add(v, n)

    @staticmethod
    def short_fetch_and_sub(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_short(n)
        return ctypes_dll.short_fetch_and_sub(v, n)

    @staticmethod
    def short_fetch_and_and(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_short(n)
        return ctypes_dll.short_fetch_and_and(v, n)

    @staticmethod
    def short_fetch_and_or(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_short(n)
        return ctypes_dll.short_fetch_and_or(v, n)

    @staticmethod
    def short_fetch_and_xor(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_short(n)
        return ctypes_dll.short_fetch_and_xor(v, n)

    @staticmethod
    def short_fetch_and_nand(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_short(n)
        return ctypes_dll.short_fetch_and_nand(v, n)

    @staticmethod
    def ushort_load(v: ctypes.c_void_p) -> int:
        return ctypes_dll.ushort_load(v)

    @staticmethod
    def ushort_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        ctypes_dll.ushort_store(v, n)

    @staticmethod
    def ushort_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        ctypes_dll.ushort_shift(v, n, r)

    @staticmethod
    def ushort_get_and_set(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ushort(n)
        return ctypes_dll.ushort_get_and_set(v, n)

    @staticmethod
    def ushort_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: int) -> bool:
        n = ctypes.c_ushort(n)
        return ctypes_dll.ushort_compare_and_set(v, e, n)

    @staticmethod
    def ushort_add_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ushort(n)
        return ctypes_dll.ushort_add_and_fetch(v, n)

    @staticmethod
    def ushort_sub_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ushort(n)
        return ctypes_dll.ushort_sub_and_fetch(v, n)

    @staticmethod
    def ushort_and_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ushort(n)
        return ctypes_dll.ushort_and_and_fetch(v, n)

    @staticmethod
    def ushort_or_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ushort(n)
        return ctypes_dll.ushort_or_and_fetch(v, n)

    @staticmethod
    def ushort_xor_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ushort(n)
        return ctypes_dll.ushort_xor_and_fetch(v, n)

    @staticmethod
    def ushort_nand_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ushort(n)
        return ctypes_dll.ushort_nand_and_fetch(v, n)

    @staticmethod
    def ushort_fetch_and_add(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ushort(n)
        return ctypes_dll.ushort_fetch_and_add(v, n)

    @staticmethod
    def ushort_fetch_and_sub(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ushort(n)
        return ctypes_dll.ushort_fetch_and_sub(v, n)

    @staticmethod
    def ushort_fetch_and_and(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ushort(n)
        return ctypes_dll.ushort_fetch_and_and(v, n)

    @staticmethod
    def ushort_fetch_and_or(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ushort(n)
        return ctypes_dll.ushort_fetch_and_or(v, n)

    @staticmethod
    def ushort_fetch_and_xor(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ushort(n)
        return ctypes_dll.ushort_fetch_and_xor(v, n)

    @staticmethod
    def ushort_fetch_and_nand(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ushort(n)
        return ctypes_dll.ushort_fetch_and_nand(v, n)

    @staticmethod
    def int_load(v: ctypes.c_void_p) -> int:
        return ctypes_dll.int_load(v)

    @staticmethod
    def int_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        ctypes_dll.int_store(v, n)

    @staticmethod
    def int_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        ctypes_dll.int_shift(v, n, r)

    @staticmethod
    def int_get_and_set(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_int(n)
        return ctypes_dll.int_get_and_set(v, n)

    @staticmethod
    def int_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: int) -> bool:
        n = ctypes.c_int(n)
        return ctypes_dll.int_compare_and_set(v, e, n)

    @staticmethod
    def int_add_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_int(n)
        return ctypes_dll.int_add_and_fetch(v, n)

    @staticmethod
    def int_sub_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_int(n)
        return ctypes_dll.int_sub_and_fetch(v, n)

    @staticmethod
    def int_and_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_int(n)
        return ctypes_dll.int_and_and_fetch(v, n)

    @staticmethod
    def int_or_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_int(n)
        return ctypes_dll.int_or_and_fetch(v, n)

    @staticmethod
    def int_xor_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_int(n)
        return ctypes_dll.int_xor_and_fetch(v, n)

    @staticmethod
    def int_nand_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_int(n)
        return ctypes_dll.int_nand_and_fetch(v, n)

    @staticmethod
    def int_fetch_and_add(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_int(n)
        return ctypes_dll.int_fetch_and_add(v, n)

    @staticmethod
    def int_fetch_and_sub(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_int(n)
        return ctypes_dll.int_fetch_and_sub(v, n)

    @staticmethod
    def int_fetch_and_and(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_int(n)
        return ctypes_dll.int_fetch_and_and(v, n)

    @staticmethod
    def int_fetch_and_or(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_int(n)
        return ctypes_dll.int_fetch_and_or(v, n)

    @staticmethod
    def int_fetch_and_xor(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_int(n)
        return ctypes_dll.int_fetch_and_xor(v, n)

    @staticmethod
    def int_fetch_and_nand(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_int(n)
        return ctypes_dll.int_fetch_and_nand(v, n)

    @staticmethod
    def uint_load(v: ctypes.c_void_p) -> int:
        return ctypes_dll.uint_load(v)

    @staticmethod
    def uint_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        ctypes_dll.uint_store(v, n)

    @staticmethod
    def uint_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        ctypes_dll.uint_shift(v, n, r)

    @staticmethod
    def uint_get_and_set(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_uint(n)
        return ctypes_dll.uint_get_and_set(v, n)

    @staticmethod
    def uint_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: int) -> bool:
        n = ctypes.c_uint(n)
        return ctypes_dll.uint_compare_and_set(v, e, n)

    @staticmethod
    def uint_add_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_uint(n)
        return ctypes_dll.uint_add_and_fetch(v, n)

    @staticmethod
    def uint_sub_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_uint(n)
        return ctypes_dll.uint_sub_and_fetch(v, n)

    @staticmethod
    def uint_and_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_uint(n)
        return ctypes_dll.uint_and_and_fetch(v, n)

    @staticmethod
    def uint_or_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_uint(n)
        return ctypes_dll.uint_or_and_fetch(v, n)

    @staticmethod
    def uint_xor_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_uint(n)
        return ctypes_dll.uint_xor_and_fetch(v, n)

    @staticmethod
    def uint_nand_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_uint(n)
        return ctypes_dll.uint_nand_and_fetch(v, n)

    @staticmethod
    def uint_fetch_and_add(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_uint(n)
        return ctypes_dll.uint_fetch_and_add(v, n)

    @staticmethod
    def uint_fetch_and_sub(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_uint(n)
        return ctypes_dll.uint_fetch_and_sub(v, n)

    @staticmethod
    def uint_fetch_and_and(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_uint(n)
        return ctypes_dll.uint_fetch_and_and(v, n)

    @staticmethod
    def uint_fetch_and_or(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_uint(n)
        return ctypes_dll.uint_fetch_and_or(v, n)

    @staticmethod
    def uint_fetch_and_xor(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_uint(n)
        return ctypes_dll.uint_fetch_and_xor(v, n)

    @staticmethod
    def uint_fetch_and_nand(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_uint(n)
        return ctypes_dll.uint_fetch_and_nand(v, n)

    @staticmethod
    def long_load(v: ctypes.c_void_p) -> int:
        return ctypes_dll.long_load(v)

    @staticmethod
    def long_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        ctypes_dll.long_store(v, n)

    @staticmethod
    def long_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        ctypes_dll.long_shift(v, n, r)

    @staticmethod
    def long_get_and_set(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_long(n)
        return ctypes_dll.long_get_and_set(v, n)

    @staticmethod
    def long_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: int) -> bool:
        n = ctypes.c_long(n)
        return ctypes_dll.long_compare_and_set(v, e, n)

    @staticmethod
    def long_add_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_long(n)
        return ctypes_dll.long_add_and_fetch(v, n)

    @staticmethod
    def long_sub_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_long(n)
        return ctypes_dll.long_sub_and_fetch(v, n)

    @staticmethod
    def long_and_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_long(n)
        return ctypes_dll.long_and_and_fetch(v, n)

    @staticmethod
    def long_or_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_long(n)
        return ctypes_dll.long_or_and_fetch(v, n)

    @staticmethod
    def long_xor_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_long(n)
        return ctypes_dll.long_xor_and_fetch(v, n)

    @staticmethod
    def long_nand_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_long(n)
        return ctypes_dll.long_nand_and_fetch(v, n)

    @staticmethod
    def long_fetch_and_add(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_long(n)
        return ctypes_dll.long_fetch_and_add(v, n)

    @staticmethod
    def long_fetch_and_sub(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_long(n)
        return ctypes_dll.long_fetch_and_sub(v, n)

    @staticmethod
    def long_fetch_and_and(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_long(n)
        return ctypes_dll.long_fetch_and_and(v, n)

    @staticmethod
    def long_fetch_and_or(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_long(n)
        return ctypes_dll.long_fetch_and_or(v, n)

    @staticmethod
    def long_fetch_and_xor(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_long(n)
        return ctypes_dll.long_fetch_and_xor(v, n)

    @staticmethod
    def long_fetch_and_nand(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_long(n)
        return ctypes_dll.long_fetch_and_nand(v, n)

    @staticmethod
    def ulong_load(v: ctypes.c_void_p) -> int:
        return ctypes_dll.ulong_load(v)

    @staticmethod
    def ulong_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        ctypes_dll.ulong_store(v, n)

    @staticmethod
    def ulong_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        ctypes_dll.ulong_shift(v, n, r)

    @staticmethod
    def ulong_get_and_set(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulong(n)
        return ctypes_dll.ulong_get_and_set(v, n)

    @staticmethod
    def ulong_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: int) -> bool:
        n = ctypes.c_ulong(n)
        return ctypes_dll.ulong_compare_and_set(v, e, n)

    @staticmethod
    def ulong_add_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulong(n)
        return ctypes_dll.ulong_add_and_fetch(v, n)

    @staticmethod
    def ulong_sub_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulong(n)
        return ctypes_dll.ulong_sub_and_fetch(v, n)

    @staticmethod
    def ulong_and_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulong(n)
        return ctypes_dll.ulong_and_and_fetch(v, n)

    @staticmethod
    def ulong_or_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulong(n)
        return ctypes_dll.ulong_or_and_fetch(v, n)

    @staticmethod
    def ulong_xor_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulong(n)
        return ctypes_dll.ulong_xor_and_fetch(v, n)

    @staticmethod
    def ulong_nand_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulong(n)
        return ctypes_dll.ulong_nand_and_fetch(v, n)

    @staticmethod
    def ulong_fetch_and_add(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulong(n)
        return ctypes_dll.ulong_fetch_and_add(v, n)

    @staticmethod
    def ulong_fetch_and_sub(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulong(n)
        return ctypes_dll.ulong_fetch_and_sub(v, n)

    @staticmethod
    def ulong_fetch_and_and(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulong(n)
        return ctypes_dll.ulong_fetch_and_and(v, n)

    @staticmethod
    def ulong_fetch_and_or(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulong(n)
        return ctypes_dll.ulong_fetch_and_or(v, n)

    @staticmethod
    def ulong_fetch_and_xor(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulong(n)
        return ctypes_dll.ulong_fetch_and_xor(v, n)

    @staticmethod
    def ulong_fetch_and_nand(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulong(n)
        return ctypes_dll.ulong_fetch_and_nand(v, n)

    @staticmethod
    def longlong_load(v: ctypes.c_void_p) -> int:
        return ctypes_dll.longlong_load(v)

    @staticmethod
    def longlong_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        ctypes_dll.longlong_store(v, n)

    @staticmethod
    def longlong_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        ctypes_dll.longlong_shift(v, n, r)

    @staticmethod
    def longlong_get_and_set(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_longlong(n)
        return ctypes_dll.longlong_get_and_set(v, n)

    @staticmethod
    def longlong_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: int) -> bool:
        n = ctypes.c_longlong(n)
        return ctypes_dll.longlong_compare_and_set(v, e, n)

    @staticmethod
    def longlong_add_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_longlong(n)
        return ctypes_dll.longlong_add_and_fetch(v, n)

    @staticmethod
    def longlong_sub_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_longlong(n)
        return ctypes_dll.longlong_sub_and_fetch(v, n)

    @staticmethod
    def longlong_and_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_longlong(n)
        return ctypes_dll.longlong_and_and_fetch(v, n)

    @staticmethod
    def longlong_or_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_longlong(n)
        return ctypes_dll.longlong_or_and_fetch(v, n)

    @staticmethod
    def longlong_xor_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_longlong(n)
        return ctypes_dll.longlong_xor_and_fetch(v, n)

    @staticmethod
    def longlong_nand_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_longlong(n)
        return ctypes_dll.longlong_nand_and_fetch(v, n)

    @staticmethod
    def longlong_fetch_and_add(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_longlong(n)
        return ctypes_dll.longlong_fetch_and_add(v, n)

    @staticmethod
    def longlong_fetch_and_sub(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_longlong(n)
        return ctypes_dll.longlong_fetch_and_sub(v, n)

    @staticmethod
    def longlong_fetch_and_and(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_longlong(n)
        return ctypes_dll.longlong_fetch_and_and(v, n)

    @staticmethod
    def longlong_fetch_and_or(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_longlong(n)
        return ctypes_dll.longlong_fetch_and_or(v, n)

    @staticmethod
    def longlong_fetch_and_xor(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_longlong(n)
        return ctypes_dll.longlong_fetch_and_xor(v, n)

    @staticmethod
    def longlong_fetch_and_nand(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_longlong(n)
        return ctypes_dll.longlong_fetch_and_nand(v, n)

    @staticmethod
    def ulonglong_load(v: ctypes.c_void_p) -> int:
        return ctypes_dll.ulonglong_load(v)

    @staticmethod
    def ulonglong_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        ctypes_dll.ulonglong_store(v, n)

    @staticmethod
    def ulonglong_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        ctypes_dll.ulonglong_shift(v, n, r)

    @staticmethod
    def ulonglong_get_and_set(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulonglong(n)
        return ctypes_dll.ulonglong_get_and_set(v, n)

    @staticmethod
    def ulonglong_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: int) -> bool:
        n = ctypes.c_ulonglong(n)
        return ctypes_dll.ulonglong_compare_and_set(v, e, n)

    @staticmethod
    def ulonglong_add_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulonglong(n)
        return ctypes_dll.ulonglong_add_and_fetch(v, n)

    @staticmethod
    def ulonglong_sub_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulonglong(n)
        return ctypes_dll.ulonglong_sub_and_fetch(v, n)

    @staticmethod
    def ulonglong_and_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulonglong(n)
        return ctypes_dll.ulonglong_and_and_fetch(v, n)

    @staticmethod
    def ulonglong_or_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulonglong(n)
        return ctypes_dll.ulonglong_or_and_fetch(v, n)

    @staticmethod
    def ulonglong_xor_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulonglong(n)
        return ctypes_dll.ulonglong_xor_and_fetch(v, n)

    @staticmethod
    def ulonglong_nand_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulonglong(n)
        return ctypes_dll.ulonglong_nand_and_fetch(v, n)

    @staticmethod
    def ulonglong_fetch_and_add(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulonglong(n)
        return ctypes_dll.ulonglong_fetch_and_add(v, n)

    @staticmethod
    def ulonglong_fetch_and_sub(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulonglong(n)
        return ctypes_dll.ulonglong_fetch_and_sub(v, n)

    @staticmethod
    def ulonglong_fetch_and_and(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulonglong(n)
        return ctypes_dll.ulonglong_fetch_and_and(v, n)

    @staticmethod
    def ulonglong_fetch_and_or(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulonglong(n)
        return ctypes_dll.ulonglong_fetch_and_or(v, n)

    @staticmethod
    def ulonglong_fetch_and_xor(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulonglong(n)
        return ctypes_dll.ulonglong_fetch_and_xor(v, n)

    @staticmethod
    def ulonglong_fetch_and_nand(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ulonglong(n)
        return ctypes_dll.ulonglong_fetch_and_nand(v, n)

    @staticmethod
    def size_t_load(v: ctypes.c_void_p) -> int:
        return ctypes_dll.size_t_load(v)

    @staticmethod
    def size_t_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        ctypes_dll.size_t_store(v, n)

    @staticmethod
    def size_t_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        ctypes_dll.size_t_shift(v, n, r)

    @staticmethod
    def size_t_get_and_set(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_size_t(n)
        return ctypes_dll.size_t_get_and_set(v, n)

    @staticmethod
    def size_t_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: int) -> bool:
        n = ctypes.c_size_t(n)
        return ctypes_dll.size_t_compare_and_set(v, e, n)

    @staticmethod
    def size_t_add_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_size_t(n)
        return ctypes_dll.size_t_add_and_fetch(v, n)

    @staticmethod
    def size_t_sub_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_size_t(n)
        return ctypes_dll.size_t_sub_and_fetch(v, n)

    @staticmethod
    def size_t_and_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_size_t(n)
        return ctypes_dll.size_t_and_and_fetch(v, n)

    @staticmethod
    def size_t_or_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_size_t(n)
        return ctypes_dll.size_t_or_and_fetch(v, n)

    @staticmethod
    def size_t_xor_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_size_t(n)
        return ctypes_dll.size_t_xor_and_fetch(v, n)

    @staticmethod
    def size_t_nand_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_size_t(n)
        return ctypes_dll.size_t_nand_and_fetch(v, n)

    @staticmethod
    def size_t_fetch_and_add(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_size_t(n)
        return ctypes_dll.size_t_fetch_and_add(v, n)

    @staticmethod
    def size_t_fetch_and_sub(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_size_t(n)
        return ctypes_dll.size_t_fetch_and_sub(v, n)

    @staticmethod
    def size_t_fetch_and_and(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_size_t(n)
        return ctypes_dll.size_t_fetch_and_and(v, n)

    @staticmethod
    def size_t_fetch_and_or(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_size_t(n)
        return ctypes_dll.size_t_fetch_and_or(v, n)

    @staticmethod
    def size_t_fetch_and_xor(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_size_t(n)
        return ctypes_dll.size_t_fetch_and_xor(v, n)

    @staticmethod
    def size_t_fetch_and_nand(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_size_t(n)
        return ctypes_dll.size_t_fetch_and_nand(v, n)

    @staticmethod
    def ssize_t_load(v: ctypes.c_void_p) -> int:
        return ctypes_dll.ssize_t_load(v)

    @staticmethod
    def ssize_t_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        ctypes_dll.ssize_t_store(v, n)

    @staticmethod
    def ssize_t_shift(v: ctypes.c_void_p, n: ctypes.c_void_p, r: ctypes.c_void_p):
        ctypes_dll.ssize_t_shift(v, n, r)

    @staticmethod
    def ssize_t_get_and_set(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ssize_t(n)
        return ctypes_dll.ssize_t_get_and_set(v, n)

    @staticmethod
    def ssize_t_compare_and_set(v: ctypes.c_void_p, e: ctypes.c_void_p, n: int) -> bool:
        n = ctypes.c_ssize_t(n)
        return ctypes_dll.ssize_t_compare_and_set(v, e, n)

    @staticmethod
    def ssize_t_add_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ssize_t(n)
        return ctypes_dll.ssize_t_add_and_fetch(v, n)

    @staticmethod
    def ssize_t_sub_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ssize_t(n)
        return ctypes_dll.ssize_t_sub_and_fetch(v, n)

    @staticmethod
    def ssize_t_and_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ssize_t(n)
        return ctypes_dll.ssize_t_and_and_fetch(v, n)

    @staticmethod
    def ssize_t_or_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ssize_t(n)
        return ctypes_dll.ssize_t_or_and_fetch(v, n)

    @staticmethod
    def ssize_t_xor_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ssize_t(n)
        return ctypes_dll.ssize_t_xor_and_fetch(v, n)

    @staticmethod
    def ssize_t_nand_and_fetch(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ssize_t(n)
        return ctypes_dll.ssize_t_nand_and_fetch(v, n)

    @staticmethod
    def ssize_t_fetch_and_add(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ssize_t(n)
        return ctypes_dll.ssize_t_fetch_and_add(v, n)

    @staticmethod
    def ssize_t_fetch_and_sub(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ssize_t(n)
        return ctypes_dll.ssize_t_fetch_and_sub(v, n)

    @staticmethod
    def ssize_t_fetch_and_and(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ssize_t(n)
        return ctypes_dll.ssize_t_fetch_and_and(v, n)

    @staticmethod
    def ssize_t_fetch_and_or(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ssize_t(n)
        return ctypes_dll.ssize_t_fetch_and_or(v, n)

    @staticmethod
    def ssize_t_fetch_and_xor(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ssize_t(n)
        return ctypes_dll.ssize_t_fetch_and_xor(v, n)

    @staticmethod
    def ssize_t_fetch_and_nand(v: ctypes.c_void_p, n: int) -> int:
        n = ctypes.c_ssize_t(n)
        return ctypes_dll.ssize_t_fetch_and_nand(v, n)

    @staticmethod
    def float_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        ctypes_dll.float_store(v, n)

    @staticmethod
    def double_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        ctypes_dll.double_store(v, n)

    @staticmethod
    def longdouble_store(v: ctypes.c_void_p, n: ctypes.c_void_p):
        ctypes_dll.longdouble_store(v, n)

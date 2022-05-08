import sys
import tempfile
from ctypes import c_ssize_t
from typing import TypeVar

if sys.platform in ("linux", "darwin"):
    import shared_atomic_.lib
    from shared_atomic_ import ffi
    lib = shared_atomic_.lib
    pointer = ffi.CData

else:
    from shared_atomic import load_wrapped_dll
    lib = load_wrapped_dll()
    pointer = c_ssize_t

self_atomic_int = TypeVar("self_atomic_int", bound="atomic_int")

def int_store(v: pointer, n: pointer):
    """Store value atomically

     :param v: the pointer to set
     :param n: the pointer from value to set
     :return: None
     """
    lib.ssize_t_store(v, n)


def int_shift(v: pointer, n: pointer, r: pointer):
    """value exchange between 3 pointers in 2 groups atomically, store n in v after store v in r

    :param v: pointer of v
    :param n: pointer of n
    :param r: pointer of r
    :return: None
    """
    return lib.ssize_t_shift(v, n, r)


def int_get_and_set(v: pointer, n: int) -> int:
    """get and set atomically

    :param v: pointer of value to get and set
    :param n: value to set
    :return: original value
    """
    return lib.ssize_t_get_and_set(v, n)


def int_compare_and_set(v: pointer, e: pointer, n: int) -> bool:
    """Compare and set atomically. This compares the contents of v
            with the contents of e. If equal, the operation is a read-modify-write
            operation that writes n into self. If they are not equal,
            the operation is a read and the current contents of v are written into
            e.
                :param v: pointer of v
                :param e: pointer of e
                :param n: value to be set
                :return: whether the contents of v and contents of e is the same
                """
    return lib.ssize_t_compare_and_set(v, e, n)


def int_add_and_fetch(v: pointer, n: int) -> int:
    """increment and fetch atomically

    :param v: atomic_int to add to and get
    :param n: data to add
    :return: sum of the 2 values
    """
    return lib.ssize_t_add_and_fetch(v, n)


def int_sub_and_fetch(v: pointer, n: int) -> int:
    """sub and fetch atomically

    :param v: pointer of value to subtract and get
    :param n: data to subtract
    :return: difference of the 2 values
    """
    return lib.ssize_t_sub_and_fetch(v, n)


def int_and_and_fetch(v: pointer, n: int) -> int:
    """bitwise AND and fetch the result atomically

    :param v: pointer of value to AND to
    :param n: data to AND
    :return: resulted value
    """
    return lib.ssize_t_and_and_fetch(v, n)


def int_or_and_fetch(v: pointer, n: int) -> int:
    """bitwise XOR and fetch the result atomically

    :param v: pointer of value to XOR to
    :param n: data to XOR
    :return: resulted value
    """
    return lib.ssize_t_or_and_fetch(v, n)


def int_xor_and_fetch(v: pointer, n: int) -> int:
    """bitwise XOR and fetch the result atomically

    :param v: pointer of value to XOR to
    :param n: data to XOR
    :return: resulted value
    """
    return lib.ssize_t_xor_and_fetch(v, n)


def int_nand_and_fetch(v: pointer, n: int) -> int:
    """bitwise NAND and fetch the result atomically

    :param v: pointer of value to NAND to
    :param n: data to NAND
    :return: resulted value
    """
    return lib.ssize_t_nand_and_fetch(v, n)


def int_fetch_and_add(v: pointer, n: int) -> int:
    """increment and fetch atomically

    :param v: pointer of value to add to
    :param n: data to add
    :return: original value in v
    """
    return lib.ssize_t_fetch_and_add(v, n)


def int_fetch_and_sub(v: pointer, n: int) -> int:
    """subtract and fetch atomically

    :param v: pointer of value to subtract from
    :param n: data to subtract
    :param encoding: character set
    :return: original value in v
    """
    return lib.ssize_t_fetch_and_sub(v, n)


def int_fetch_and_and(v: pointer, n: int) -> int:
    """fetch then bitwise AND atomically

    :param v: pointer of value to AND to
    :param n: data to AND
    :return: the result
    """
    return lib.ssize_t_fetch_and_and(v, n)


def int_fetch_and_or(v: pointer, n: int) -> int:
    """fetch then bitwise OR atomically

    :param v: pointer of value to OR to
    :param n: data to OR
    :return: the result
    """
    return lib.ssize_t_fetch_and_or(v, n)


def int_fetch_and_xor(v: pointer, n: int) -> int:
    """fetch then bitwise XOR atomically

    :param v: pointer of value to XOR to
    :param n: data to XOR
    :return: the result
    """
    return lib.ssize_t_fetch_and_xor(v, n)


def int_fetch_and_nand(v: pointer, n: int) -> int:
    """fetch then bitwise NAND atomically

    :param v: pointer of value to NAND to
    :param n: data to NAND
    :return: the result
    """
    return lib.ssize_t_fetch_and_nand(v, n)

class atomic_int:

    def __init__(self, value: int, mode: str = 'singleprocessing'):
        if sys.platform in ('darwin','linux'):
            if mode in ('m', 'multiprocessing'):
                self.mode = 'm'
                self.array = tempfile.TemporaryFile()
                self.array.write(b'\0'* 8)
                self.array.flush()
                void_pointer = lib.mmap(ffi.NULL, 8, 3, 1, self.array.fileno(), 0)
                self.reference = ffi.cast("ssize_t *", void_pointer)
            elif mode in ('s', 'singleprocessing'):
                self.mode = 's'
                self.array = ffi.new("ssize_t *")
                self.reference = self.array
            self.set(value)
        elif sys.platform == 'win32':
            self.mode = 's'
            #value_bytes = int.to_bytes(value, byteorder='big', length=8)
            #data_all = b'\0'*(8-len(value)) + value

            self.array = c_ssize_t(value)
            self.reference = self.array

    if sys.platform in ('darwin','linux'):
        def __del__(self):
            if self.mode == 'm':
                self.array.close()
                lib.munmap(self.reference, 8)

    def get(self) -> int:
        return lib.ssize_t_load(self.reference)

    def set(self, value: int):
        lib.ssize_t_get_and_set(self.reference, value)

    def int_store(self, n: self_atomic_int):
        """Store value atomically

         :param v: the pointer to set
         :param n: the pointer from value to set
         :return: None
         """
        lib.ssize_t_store(self.reference, n.reference)

    def int_shift(self, n: self_atomic_int, r: self_atomic_int):
        """value exchange between 3 pointers in 2 groups atomically, store n in v after store v in r

        :param v: pointer of v
        :param n: pointer of n
        :param r: pointer of r
        :return: None
        """
        return lib.ssize_t_shift(self.reference, n.reference, r.reference)

    def int_get_and_set(self, n: int) -> int:
        """get and set atomically

        :param v: pointer of value to get and set
        :param n: value to set
        :return: original value
        """
        return lib.ssize_t_get_and_set(self.reference, n)

    def int_compare_and_set(self, e: self_atomic_int, n: int) -> bool:
        """Compare and set atomically. This compares the contents of v
                with the contents of e. If equal, the operation is a read-modify-write
                operation that writes n into self. If they are not equal,
                the operation is a read and the current contents of v are written into
                e.
                    :param v: pointer of v
                    :param e: pointer of e
                    :param n: value to be set
                    :return: whether the contents of v and contents of e is the same
                    """
        return lib.ssize_t_compare_and_set(self.reference, e.reference, n)

    def int_add_and_fetch(self, n: int) -> int:
        """increment and fetch atomically

        :param v: atomic_int to add to and get
        :param n: data to add
        :return: sum of the 2 values
        """
        return lib.ssize_t_add_and_fetch(self.reference, n)

    def int_sub_and_fetch(self, n: int) -> int:
        """sub and fetch atomically

        :param v: pointer of value to subtract and get
        :param n: data to subtract
        :return: difference of the 2 values
        """
        return lib.ssize_t_sub_and_fetch(self.reference, n)

    def int_and_and_fetch(self, n: int) -> int:
        """bitwise AND and fetch the result atomically

        :param v: pointer of value to AND to
        :param n: data to AND
        :return: resulted value
        """
        return lib.ssize_t_and_and_fetch(self.reference, n)

    def int_or_and_fetch(self, n: int) -> int:
        """bitwise XOR and fetch the result atomically

        :param v: pointer of value to XOR to
        :param n: data to XOR
        :return: resulted value
        """
        return lib.ssize_t_or_and_fetch(self.reference, n)

    def int_xor_and_fetch(self, n: int) -> int:
        """bitwise XOR and fetch the result atomically

        :param v: pointer of value to XOR to
        :param n: data to XOR
        :return: resulted value
        """
        return lib.ssize_t_xor_and_fetch(self.reference, n)

    def int_nand_and_fetch(self, n: int) -> int:
        """bitwise NAND and fetch the result atomically

        :param v: pointer of value to NAND to
        :param n: data to NAND
        :return: resulted value
        """
        return lib.ssize_t_nand_and_fetch(self.reference, n)

    def int_fetch_and_add(self, n: int) -> int:
        """increment and fetch atomically

        :param v: pointer of value to add to
        :param n: data to add
        :return: original value in v
        """
        return lib.ssize_t_fetch_and_add(self.reference, n)

    def int_fetch_and_sub(self, n: int) -> int:
        """subtract and fetch atomically

        :param v: pointer of value to subtract from
        :param n: data to subtract
        :param encoding: character set
        :return: original value in v
        """
        return lib.ssize_t_fetch_and_sub(self.reference, n)

    def int_fetch_and_and(self, n: int) -> int:
        """fetch then bitwise AND atomically

        :param v: pointer of value to AND to
        :param n: data to AND
        :return: the result
        """
        return lib.ssize_t_fetch_and_and(self.reference, n)

    def int_fetch_and_or(self, n: int) -> int:
        """fetch then bitwise OR atomically

        :param v: pointer of value to OR to
        :param n: data to OR
        :return: the result
        """
        return lib.ssize_t_fetch_and_or(self.reference, n)

    def int_fetch_and_xor(self, n: int) -> int:
        """fetch then bitwise XOR atomically

        :param v: pointer of value to XOR to
        :param n: data to XOR
        :return: the result
        """
        return lib.ssize_t_fetch_and_xor(self.reference, n)

    def int_fetch_and_nand(self, n: int) -> int:
        """fetch then bitwise NAND atomically

        :param v: pointer of value to NAND to
        :param n: data to NAND
        :return: the result
        """
        return lib.ssize_t_fetch_and_nand(self.reference, n)

    value = property(fget=get, fset=set)
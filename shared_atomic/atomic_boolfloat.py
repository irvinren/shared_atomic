import sys
from ctypes import c_bool, c_double
import tempfile
from typing import TypeVar


if sys.platform in ("linux", "darwin"):
    import shared_atomic_.lib
    from shared_atomic_ import ffi
    lib = shared_atomic_.lib
    bool_pointer = ffi.CData
    double_pointer = ffi.CData


else:
    from shared_atomic import load_wrapped_dll
    lib = load_wrapped_dll()
    bool_pointer = c_bool
    double_pointer =c_double

self_atomic_bool = TypeVar("self_atomic_bool", bound="atomic_bool")
self_atomic_float = TypeVar("self_atomic_float", bound="atomic_float")


def bool_store(v: bool_pointer, n: bool_pointer):
    """Store value atomically

    :param v: the pointer to set
    :param n: the pointer from value to set
    :return: None
    """
    lib.bool_store(v, n)


def bool_shift(v: bool_pointer, n: bool_pointer, r: bool_pointer):
    """value exchange between 3 pointers in 2 groups atomically, store n in v after store v in r

    :param v: pointer of v
    :param n: pointer of n
    :param r: pointer of r
    :return: None
    """
    lib.bool_shift(v, n, r)


def bool_get_and_set(v: bool_pointer, n: bool) -> bool:
    """get and set atomically

    :param v: pointer of value to get and set
    :param n: value to set
    :return: original value
    """
    return lib.bool_get_and_set(v, n)


def bool_compare_and_set(v: bool_pointer, e: bool_pointer, n: bool) -> bool:
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
    return lib.bool_compare_and_set(v, e, n)


def float_store(v: double_pointer, n: double_pointer):
    """Store value atomically

     :param v: the pointer to set
     :param n: the pointer from value to set
     :return: None
     """
    lib.double_store(v, n)


class atomic_bool:

    def __init__(self, value: bool, mode: str = 'singleprocessing'):
        r"""
        constructor to initialize the atomic_bool,
        the atomic_bool should be no longer than 8 bytes

        :param value: initial value of the bool.
        :param mode: the mode in which the bool will be shared. 'singleprocessing' or 's' for single process, 'multiprocessing' or 'm' for multiprocessing, on windows platform, only singleprocessing is supported, setting it to 'm' or 'multiprocessing' will be ignored.
        """
        if sys.platform in ('darwin','linux'):
            if mode in ('m', 'multiprocessing'):
                self.mode = 'm'
                self.array = tempfile.TemporaryFile()
                self.array.write(b'\0')
                self.array.flush()
                void_pointer = lib.mmap(ffi.NULL, 1, 3, 1, self.array.fileno(), 0)
                self.reference = ffi.cast("_Bool *", void_pointer)
            elif mode in ('s', 'singleprocessing'):
                self.mode = 's'
                self.array = ffi.new("_Bool *")
                self.reference = self.array
            self.set(value)
        elif sys.platform == 'win32':
            self.mode = 's'

            self.array = c_bool(value)
            #value_bytes = int.to_bytes(value, byteorder='big', length=1)
            #data_all = b'\0'*(8-len(value)) + value
            #self.array = bytearray(value_bytes)
            self.reference = self.array

    if sys.platform in ('darwin','linux'):
        def __del__(self):
            if self.mode == 'm':
                self.array.close()
                lib.munmap(self.reference, 1)

    def get(self) -> bool:
        """
        Get the value from atomic_bool,
        :return: the value

        """
        return lib.bool_load(self.reference)

    def set(self, value: bool):
        """
        set the value into atomic_bool
        :param value: target value of the bool.

        """
        lib.bool_get_and_set(self.reference, value)

    def bool_store(self, n: self_atomic_bool):
        """Store value atomically

        :param n: the atomic_bool to set
        :return: None
        """
        lib.bool_store(self.reference, n.reference)

    def bool_shift(self, n: self_atomic_bool, r: self_atomic_bool):
        """value exchange between 3 pointers in 2 groups atomically, store n in v after store v in r

        :param n: atomic_bool
        :param r: atomic_bool
        :return: None
        """
        lib.bool_shift(self.reference, n.reference, r.reference)

    def bool_get_and_set(self, n: bool) -> bool:
        """get and set atomically

        :param n: atomic_bool
        :return: original value
        """
        return lib.bool_get_and_set(self.reference, n)

    def bool_compare_and_set(self, e: self_atomic_bool, n: bool) -> bool:
        """Compare and set atomically. This compares the contents of v
        with the contents of e. If equal, the operation is a read-modify-write
        operation that writes n into self. If they are not equal,
        the operation is a read and the current contents of v are written into
        e.
        :param e: atomic_bool
        :param n: value to be set
        :return: whether the contents of v and contents of e is the same
        """
        return lib.bool_compare_and_set(self.reference, e.reference, n)

    value = property(fget=get, fset=set)

class atomic_float:

    def __init__(self, value: float, mode: str = 'singleprocessing'):
        r"""
        constructor to initialize the atomic_bool,
        the atomic_bool should be no longer than 8 bytes

        :param value: initial value of the float.
        :param mode: the mode in which the float will be shared. 'singleprocessing' or 's' for single process, 'multiprocessing' or 'm' for multiprocessing, on windows platform, only singleprocessing is supported, setting it to 'm' or 'multiprocessing' will be ignored.
        """
        if sys.platform in ('darwin','linux'):
            if mode in ('m', 'multiprocessing'):
                self.mode = 'm'
                self.array = tempfile.TemporaryFile()
                self.array.write(b'\0' * 8)
                self.array.flush()
                void_pointer = lib.mmap(ffi.NULL, 8, 3, 1, self.array.fileno(), 0)
                self.reference = ffi.cast("double *", void_pointer)
            elif mode in ('s', 'singleprocessing'):
                self.mode = 's'
                self.array = ffi.new("double *")
                self.reference = self.array
            self.set(value)
        elif sys.platform == 'win32':
            self.mode = 's'
            self.array = c_double(value)
            self.reference = self.array

    if sys.platform in ('darwin','linux'):
        def __del__(self):
            if self.mode == 'm':
                self.array.close()
                lib.munmap(self.reference, 8)

    if sys.platform in ('darwin','linux'):
        def get(self) -> float:
            pointer = ffi.new("double *",0.0)
            lib.double_store(pointer, self.reference)
            value = ffi.unpack(pointer, 1)[0]
            return value

    elif sys.platform in ('win32'):
        def get(self) -> float:
            pointer = c_double(0.0)
            lib.double_store(pointer, self.reference)
            return pointer.value

    if sys.platform in ('darwin','linux'):
        def set(self, value: float):
            pointer = ffi.new("double *", value)
            lib.double_store(self.reference, pointer)
    elif sys.platform in ('win32'):
        def set(self, value: float):
            pointer = c_double(value)
            lib.double_store(self.reference, pointer)

    def float_store(self, n: self_atomic_float):
        """Store value atomically

         :param n: the atomic_float from value to set
         """
        lib.double_store(self.reference, n.reference)

    value = property(fget=get, fset=set)

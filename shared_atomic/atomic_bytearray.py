import ctypes
from multiprocessing import Array
from shared_atomic import loaddll
import sys


class atomic_bytearray:

    def __init__(self, initial: bytes,
                 mode: str = 'singleprocessing',
                 length: int = None,
                 paddingdirection: str = 'right',
                 paddingbytes: bytes = b'\0',
                 trimming_direction: bool = 'right'):

        input_length = len(initial)

        if length is not None:
            if length > 8:
                raise ValueError("length is longer than expected, "
                                 "should be less than 9 bytes!")

        elif input_length > 8 and length is None:
            raise ValueError("input bytearray is longer than expected, "
                             "should be less than 9 bytes!")

        if length is not None:
            if input_length > length:
                if trimming_direction in('r', 'right'):
                    data = initial[:length]
                elif trimming_direction in ('l', 'left'):
                    data = initial[input_length - length:]

            elif input_length < length:
                devision , remaining = divmod(length - input_length, len(paddingbytes))
                padding = paddingbytes*devision + paddingbytes[:remaining]
                if paddingdirection in ('l', 'left'):
                    data = padding + initial
                elif paddingdirection in ('r', 'right'):
                    data = initial + padding
            else:
                data = initial
        else:
            data = initial

        atomic = loaddll()

        self.initial_length = len(data)
        if self.initial_length == 1:

            self.size = 1
            self.type = ctypes.c_ubyte
            self._array_store = atomic.ubyte_store
            self._array_get_and_set = atomic.ubyte_get_and_set
            self._array_shift = atomic.ubyte_shift
            self._array_compare_and_set = atomic.ubyte_compare_and_set
            self._array_add_and_fetch = atomic.ubyte_add_and_fetch
            self._array_sub_and_fetch = atomic.ubyte_sub_and_fetch
            self._array_and_and_fetch = atomic.ubyte_and_and_fetch
            self._array_or_and_fetch = atomic.ubyte_or_and_fetch
            self._array_xor_and_fetch = atomic.ubyte_xor_and_fetch
            self._array_nand_and_fetch = atomic.ubyte_nand_and_fetch
            self._array_fetch_and_add = atomic.ubyte_fetch_and_add
            self._array_fetch_and_sub = atomic.ubyte_fetch_and_sub
            self._array_fetch_and_and = atomic.ubyte_fetch_and_and
            self._array_fetch_and_or = atomic.ubyte_fetch_and_or
            self._array_fetch_and_xor = atomic.ubyte_fetch_and_xor
            self._array_fetch_and_nand = atomic.ubyte_fetch_and_nand

        elif self.initial_length == 2:
            self.size = 2
            self.type = ctypes.c_ushort
            self._array_store = atomic.ushort_store
            self._array_get_and_set = atomic.ushort_get_and_set
            self._array_shift = atomic.ushort_shift
            self._array_compare_and_set = atomic.ushort_compare_and_set
            self._array_add_and_fetch = atomic.ushort_add_and_fetch
            self._array_sub_and_fetch = atomic.ushort_sub_and_fetch
            self._array_and_and_fetch = atomic.ushort_and_and_fetch
            self._array_or_and_fetch = atomic.ushort_or_and_fetch
            self._array_xor_and_fetch = atomic.ushort_xor_and_fetch
            self._array_nand_and_fetch = atomic.ushort_nand_and_fetch
            self._array_fetch_and_add = atomic.ushort_fetch_and_add
            self._array_fetch_and_sub = atomic.ushort_fetch_and_sub
            self._array_fetch_and_and = atomic.ushort_fetch_and_and
            self._array_fetch_and_or = atomic.ushort_fetch_and_or
            self._array_fetch_and_xor = atomic.ushort_fetch_and_xor
            self._array_fetch_and_nand = atomic.ushort_fetch_and_nand

        elif self.initial_length <= 4:
            self.size = 4
            self.type = ctypes.c_uint
            self._array_store = atomic.uint_store
            self._array_get_and_set = atomic.uint_get_and_set
            self._array_shift = atomic.uint_shift
            self._array_compare_and_set = atomic.uint_compare_and_set
            self._array_add_and_fetch = atomic.uint_add_and_fetch
            self._array_sub_and_fetch = atomic.uint_sub_and_fetch
            self._array_and_and_fetch = atomic.uint_and_and_fetch
            self._array_or_and_fetch = atomic.uint_or_and_fetch
            self._array_xor_and_fetch = atomic.uint_xor_and_fetch
            self._array_nand_and_fetch = atomic.uint_nand_and_fetch
            self._array_fetch_and_add = atomic.uint_fetch_and_add
            self._array_fetch_and_sub = atomic.uint_fetch_and_sub
            self._array_fetch_and_and = atomic.uint_fetch_and_and
            self._array_fetch_and_or = atomic.uint_fetch_and_or
            self._array_fetch_and_xor = atomic.uint_fetch_and_xor
            self._array_fetch_and_nand = atomic.uint_fetch_and_nand


        else:
            self.size = 8
            self.type = ctypes.c_ulonglong
            self._array_store = atomic.ulonglong_store
            self._array_get_and_set = atomic.ulonglong_get_and_set
            self._array_shift = atomic.ulonglong_shift
            self._array_compare_and_set = atomic.ulonglong_compare_and_set
            self._array_add_and_fetch = atomic.ulonglong_add_and_fetch
            self._array_sub_and_fetch = atomic.ulonglong_sub_and_fetch
            self._array_and_and_fetch = atomic.ulonglong_and_and_fetch
            self._array_or_and_fetch = atomic.ulonglong_or_and_fetch
            self._array_xor_and_fetch = atomic.ulonglong_xor_and_fetch
            self._array_nand_and_fetch = atomic.ulonglong_nand_and_fetch
            self._array_fetch_and_add = atomic.ulonglong_fetch_and_add
            self._array_fetch_and_sub = atomic.ulonglong_fetch_and_sub
            self._array_fetch_and_and = atomic.ulonglong_fetch_and_and
            self._array_fetch_and_or = atomic.ulonglong_fetch_and_or
            self._array_fetch_and_xor = atomic.ulonglong_fetch_and_xor
            self._array_fetch_and_nand = atomic.ulonglong_fetch_and_nand

        if sys.platform in ('darwin','linux'):
            if mode in ('m', 'multiprocessing'):
                self.mode = 'm'
                self.array = Array(ctypes.c_ubyte, self.size, lock=False)
            elif mode in ('s', 'singleprocessing'):
                self.mode = 's'
                self.array = (ctypes.c_ubyte * self.size)()
            self.array_reference = ctypes.byref(self.array)
        if sys.platform == 'win32':
            self.mode = 's'
            data = b'\0'*(self.size-len(data)) + data
            self.array = bytearray(data)
            self.array_reference = memoryview(self.array)


        self.array_get_and_set(data)

    def get_int(self):
        result = self.type(0)
        self._array_store(ctypes.byref(result), self.array_reference)
        return result.value

    def get_bytes(self, trim=False):
        result = self.type(0)
        self._array_store(ctypes.byref(result), self.array_reference)
        if trim:
            result = int.to_bytes(result.value, length=self.size, byteorder='big').lstrip(b'\0')
        else:
            result = int.to_bytes(result.value, length=self.size, byteorder='big')
        return result

    def set_bytes(self, data: bytes):
        desiredlength = len(data)
        if 8 >= desiredlength > self.size:
            self.resize(desiredlength)
        elif desiredlength > 8:
            raise ValueError()
        integer = int.from_bytes(data, byteorder='big')
        self.initial_length = desiredlength
        ctype_integer = self.type(integer)
        self._array_store(self.array_reference, ctypes.byref(ctype_integer))

    def resize(self, newlength: int,
                 paddingdirection: str = 'right',
                 paddingbytes: bytes = b'\0',
                 trimming_direction:bool = 'right'):

        self.__init__(self.get_bytes(), mode=self.mode, length=newlength,
                                paddingdirection=paddingdirection,
                                paddingbytes=paddingbytes,
                                trimming_direction=trimming_direction)

    def array_store(self, data: bytes):
        self.set_bytes(data)

    def array_get_and_set(self, data: bytes):
        integer = int.from_bytes(data, byteorder='big')
        prev = int.to_bytes(self._array_get_and_set(self.array_reference, self.type(integer)),
                                                    length=self.size, byteorder='big')
        self.initial_length = len(data)
        return prev

    def array_shift(self, i, j):
        self._array_shift(self.array_reference,
                          i.array_reference, j.array_reference)
        self.initial_length = j.length

    def array_compare_and_set(self, i, n: bytes):
        integer = int.from_bytes(n, byteorder='big')
        result = self._array_compare_and_set(self.array_reference,
                                           i.array_reference, self.type(integer))
        if result:
            self.initial_length = len(n)

        return result

    def array_add_and_fetch(self, n: bytes, trim=True):
        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_add_and_fetch(self.array_reference, self.type(integer)),
                          length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result

    def array_sub_and_fetch(self, n: bytes, trim=True):
        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_sub_and_fetch(self.array_reference, self.type(integer)),
                            length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result


    def array_and_and_fetch(self, n: bytes, trim=True):
        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_and_and_fetch(self.array_reference, self.type(integer)),
                            length=self.size, byteorder='big').lstrip(b'\0')
        return result.lstrip(b'\0') if trim else result


    def array_or_and_fetch(self, n: bytes, trim=True):
        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_or_and_fetch(self.array_reference, self.type(integer)),
                            length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result

    def array_xor_and_fetch(self, n: bytes, trim=True):
        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_xor_and_fetch(self.array_reference, self.type(integer)),
                            length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result

    def array_nand_and_fetch(self, n: bytes, trim=True):
        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_nand_and_fetch(self.array_reference, self.type(integer)),
                            length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result


    def array_fetch_and_add(self, n: bytes, trim=True):
        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_fetch_and_add(self.array_reference, self.type(integer)),
                            length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result


    def array_fetch_and_sub(self, n: bytes, trim=True):
        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_fetch_and_sub(self.array_reference, self.type(integer)),
                            length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result


    def array_fetch_and_and(self, n: bytes, trim=True):
        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_fetch_and_and(self.array_reference, self.type(integer)),
                            length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result


    def array_fetch_and_or(self, n: bytes, trim=True):
        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_fetch_and_or(self.array_reference, self.type(integer)),
                                                     length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result

    def array_fetch_and_xor(self, n: bytes, trim=True):
        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_fetch_and_xor(self.array_reference, self.type(integer)),
                                                      length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result

    def array_fetch_and_nand(self, n: bytes, trim=True):
        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_fetch_and_nand(self.array_reference, self.type(integer)),
                                                       length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result

    def change_mode(self, newmode='m'):
        if newmode in ('m', 'multiprocessing'):
            if self.mode == 's':
                data = self.get_bytes()
                self.array = Array(ctypes.c_ubyte, self.size, lock=False)
                self.array_reference = ctypes.byref(self.array)
                self.set_bytes(data)

        elif newmode not in ('s', 'singleprocessing'):
            raise ValueError("newmode has the wrong value, should be 'm','s','multiprocessing' or 'singleprocessing'")

        elif self.mode == 'm':
            data = self.get_bytes()
            self.array = (ctypes.c_ubyte * self.size)()
            self.array_reference = ctypes.byref(self.array)
            self.set_bytes(data)
        self.mode = newmode



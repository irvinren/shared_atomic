import sys
import ctypes
from typing import Iterable
import math
from bitarray import bitarray
from bitarray.util import ba2hex, ba2int, int2ba

if sys.platform in ("linux", "darwin"):
    from shared_atomic_ import ffi
    import shared_atomic_.lib
    import tempfile

    lib = shared_atomic_.lib

elif sys.platform == "win32":
    from shared_atomic import load_wrapped_dll
    lib = load_wrapped_dll()

class atomic_list:
    """
    set provide atomic operations, the set should be no longer than 8 bytes
    """

    def __init__(self, initial: Iterable,
                 encoding='utf-8',
                 mode='singleprocessing'):
        r"""
        constructor to initialize the set,
        the set should be no longer than 8 bytes

        :param initial: initial value of the set, if the initial value is longer than 8 bytes, please specify the trimming target length, or else it would fail.
        :param mode: the mode in which the set will be shared. 'singleprocessing' or 's' for single process, 'multiprocessing' or 'm' for multiprocessing, on windows platform, only singleprocessing is supported, setting it to 'm' or 'multiprocessing' will be ignored.
        :param encoding: , character set, default 'utf-8'
        """


        self.encoding = encoding
        initial_list = list(initial)

        full_data, self.initial_length = self.encode(initial_list)


        if self.initial_length <= 4:
            if sys.platform in ('darwin', 'linux'):
                self.type = "unsigned int"
                self.size = 4
                self._array_load = lib.uint_load
                self._array_store = lib.uint_store
                self._array_get_and_set = lib.uint_get_and_set
                self._array_shift = lib.uint_shift
                self._array_compare_and_set = lib.uint_compare_and_set
                self._array_add_and_fetch = lib.uint_add_and_fetch
                self._array_sub_and_fetch = lib.uint_sub_and_fetch
                self._array_and_and_fetch = lib.uint_and_and_fetch
                self._array_or_and_fetch = lib.uint_or_and_fetch
                self._array_xor_and_fetch = lib.uint_xor_and_fetch
                self._array_nand_and_fetch = lib.uint_nand_and_fetch
                self._array_fetch_and_add = lib.uint_fetch_and_add
                self._array_fetch_and_sub = lib.uint_fetch_and_sub
                self._array_fetch_and_and = lib.uint_fetch_and_and
                self._array_fetch_and_or = lib.uint_fetch_and_or
                self._array_fetch_and_xor = lib.uint_fetch_and_xor
                self._array_fetch_and_nand = lib.uint_fetch_and_nand
            elif sys.platform == 'win32':
                self.type = ctypes.c_uint
                self.size = 4
                self._array_load = lib.uint_load
                self._array_store = lib.uint_store
                self._array_get_and_set = lib.uint_get_and_set
                self._array_shift = lib.uint_shift
                self._array_compare_and_set = lib.uint_compare_and_set
                self._array_add_and_fetch = lib.uint_add_and_fetch
                self._array_sub_and_fetch = lib.uint_sub_and_fetch
                self._array_and_and_fetch = lib.uint_and_and_fetch
                self._array_or_and_fetch = lib.uint_or_and_fetch
                self._array_xor_and_fetch = lib.uint_xor_and_fetch
                self._array_nand_and_fetch = lib.uint_nand_and_fetch
                self._array_fetch_and_add = lib.uint_fetch_and_add
                self._array_fetch_and_sub = lib.uint_fetch_and_sub
                self._array_fetch_and_and = lib.uint_fetch_and_and
                self._array_fetch_and_or = lib.uint_fetch_and_or
                self._array_fetch_and_xor = lib.uint_fetch_and_xor
                self._array_fetch_and_nand = lib.uint_fetch_and_nand
        elif self.initial_length <= 8:
            if sys.platform in ('darwin', 'linux'):
                self.type = "unsigned long long"
                self.size = 8
                self._array_load = lib.ulonglong_load
                self._array_store = lib.ulonglong_store
                self._array_get_and_set = lib.ulonglong_get_and_set
                self._array_shift = lib.ulonglong_shift
                self._array_compare_and_set = lib.ulonglong_compare_and_set
                self._array_add_and_fetch = lib.ulonglong_add_and_fetch
                self._array_sub_and_fetch = lib.ulonglong_sub_and_fetch
                self._array_and_and_fetch = lib.ulonglong_and_and_fetch
                self._array_or_and_fetch = lib.ulonglong_or_and_fetch
                self._array_xor_and_fetch = lib.ulonglong_xor_and_fetch
                self._array_nand_and_fetch = lib.ulonglong_nand_and_fetch
                self._array_fetch_and_add = lib.ulonglong_fetch_and_add
                self._array_fetch_and_sub = lib.ulonglong_fetch_and_sub
                self._array_fetch_and_and = lib.ulonglong_fetch_and_and
                self._array_fetch_and_or = lib.ulonglong_fetch_and_or
                self._array_fetch_and_xor = lib.ulonglong_fetch_and_xor
                self._array_fetch_and_nand = lib.ulonglong_fetch_and_nand
            elif sys.platform == 'win32':
                self.type = ctypes.c_ulonglong
                self.size = 8
                self._array_load = lib.ulonglong_load
                self._array_store = lib.ulonglong_store
                self._array_get_and_set = lib.ulonglong_get_and_set
                self._array_shift = lib.ulonglong_shift
                self._array_compare_and_set = lib.ulonglong_compare_and_set
                self._array_add_and_fetch = lib.ulonglong_add_and_fetch
                self._array_sub_and_fetch = lib.ulonglong_sub_and_fetch
                self._array_and_and_fetch = lib.ulonglong_and_and_fetch
                self._array_or_and_fetch = lib.ulonglong_or_and_fetch
                self._array_xor_and_fetch = lib.ulonglong_xor_and_fetch
                self._array_nand_and_fetch = lib.ulonglong_nand_and_fetch
                self._array_fetch_and_add = lib.ulonglong_fetch_and_add
                self._array_fetch_and_sub = lib.ulonglong_fetch_and_sub
                self._array_fetch_and_and = lib.ulonglong_fetch_and_and
                self._array_fetch_and_or = lib.ulonglong_fetch_and_or
                self._array_fetch_and_xor = lib.ulonglong_fetch_and_xor
                self._array_fetch_and_nand = lib.ulonglong_fetch_and_nand

        else:
            raise ValueError("Input set too long! It should be no more than 8 bytes!")

        if sys.platform in ('darwin', 'linux'):
            if mode in ('m', 'multiprocessing'):
                self.mode = 'm'
                # self.array = Value(self.type, lock=False)
                self.array = tempfile.TemporaryFile()
                self.array.write(b'\0' * self.size)
                self.array.flush()
                void_pointer = lib.mmap(ffi.NULL, self.size, 3, 1, self.array.fileno(), 0)
                self.array_reference = ffi.cast(self.type + " *", void_pointer)
            elif mode in ('s', 'singleprocessing'):
                self.mode = 's'
                self.array = ffi.new(self.type + " *")
                self.array_reference = self.array

            self._array_get_and_set(self.array_reference, full_data)

        elif sys.platform == 'win32':
            self.mode = 's'
            # data = full_data.to_bytes(length=ctypes.sizeof(self.type), byteorder='big')[::-1]
            data = full_data.to_bytes(length=self.size, byteorder='big')[::-1]
            self.array = bytearray(data)
            self.array_reference = memoryview(self.array)

    if sys.platform in ("linux", "darwin"):
        def __del__(self):
            if self.mode == 'm':
                lib.munmap(self.array_reference, self.size)
                self.array.close()

    def decode(self, bits_in_bytes: bytes) -> list:
        """Function to decode the bytes to set

        :param bits_in_bytes:  bytes needs to be decoded
        :param encoding: character encoding
        :return: the decoded set
        """
        bits = bitarray()
        bits.frombytes(bits_in_bytes)
        data_continue_flag = True
        i = 0


        meta_list = []
        while not bits[0]:
            bits <<= 1
        bits <<= 1
        while data_continue_flag:
            kind = ba2int(bits[i:i + 2])
            if kind != 0:
                length = ba2int(bits[i + 2:i + 5])
                meta_list.append({'length': length, 'kind': kind})
                if not bits[i + 5]:
                    data_continue_flag = False
                i += 6

            else:
                meta_list.append({'length': 1, 'kind': 0})
                if not bits[i + 2]:
                    data_continue_flag = False
                i += 3

        result = []

        for data_dict in meta_list:
            start_point = i
            kind = data_dict['kind']
            length = data_dict['length']

            if kind == 0:
                result.append(True if bits[start_point] else False)
                i += 1
            elif kind == 1:
                result.append(ba2int(bits[start_point:start_point + length]))
                i += length
            elif kind == 2:
                str_bytes = bytes.fromhex(ba2hex(bits[start_point:start_point + length * 8]))
                result.append(str_bytes.decode(self.encoding))
                i += length * 8
            elif kind == 3:
                result.append(bytes.fromhex(ba2hex(bits[start_point:start_point + length * 8])))
                i += length * 8
            else:
                raise ('Type not supported!')
        return result

    def encode(self, input_list: list) -> (int, int):
        """function to encode the input_set with specific character encoding

        :param input_list: input set
        :param encoding: character encoding
        :return: (data in integer representation, total length in bits)
        """
        accumulated_length = 0
        item_num = 0
        data_bitarray = bitarray()
        data_prefix = 1

        for i in input_list:
            hash(i)
            if item_num != 0:
                data_prefix += 1
            item_num += 1

            if isinstance(i, bool):
                length = 1
                data_prefix, accumulated_length = self.shift_and_add(data_prefix,
                                                                     accumulated_length,
                                                                     length, 0)
                data_bitarray += [i]
            elif isinstance(i, int):
                # length = uint(max(math.ceil(math.log2(i+1)),1))
                b = int2ba(i)
                length = len(b)
                data_prefix, accumulated_length = self.shift_and_add(data_prefix,
                                                                     accumulated_length,
                                                                     length, 1)

                # b.frombytes(i.to_bytes(length=max(math.ceil(length.value/8),1), byteorder='big'))
                # c = b[-length.value:]
                data_bitarray += b

            elif isinstance(i, str):
                input_bytes = i.encode(encoding=self.encoding)
                length = len(input_bytes)
                data_prefix, accumulated_length = self.shift_and_add(data_prefix,
                                                                     accumulated_length,
                                                                     length, 2)
                b = bitarray()
                b.frombytes(input_bytes)
                data_bitarray += b
            elif isinstance(i, bytes):
                length = len(i)
                data_prefix, accumulated_length = self.shift_and_add(data_prefix,
                                                                     accumulated_length,
                                                                     length, 3)
                b = bitarray()
                b.frombytes(i)
                data_bitarray += b
            else:
                raise ('Type not supported!')

        total_length = math.ceil((len(f'{data_prefix:b}') + accumulated_length) / 8)
        if total_length > 8:
            raise ValueError("Total Length exceeds 8 bytes!")
        # data_int = int.from_bytes(data_bitarray.tobytes(), byteorder='big')
        data_int = ba2int(data_bitarray)
        full_data = (data_prefix << len(data_bitarray)) + data_int
        return full_data, total_length

    def shift_and_add(self, data_prefix: int, accumulate_length: int,
                      input_length: int, kind: int) -> (int, int):
        """Function to finish the shift and add of the data prefix

        :param data_prefix: integer for the data_prefix
        :param accumulate_length: total data length in bits accumulated so far
        :param input_length: length of the data segment in bits
        :param kind: sorts of data
        :return: (data_prefix, accumulate_length)
        """

        if kind in (2, 3):
            accumulate_length += input_length * 8
        else:
            accumulate_length += input_length

        if kind != 0:
            data_prefix <<= 6
            data_prefix += (kind << 4) + (input_length << 1)
        else:
            data_prefix <<= 3
            # self.atomic.uint_add_and_fetch(byref(data_prefix),0)

        return data_prefix, accumulate_length

    def get_int(self) -> int:
        """
        Get the whole integer representation from the set,
        the whole set would be treated as a large integer

        :return: the integer representation
        """
        return self._array_load(self.array_reference)

    def set_int(self, integer: int):
        """
        Set the whole integer representation from the set,
        the whole set would be treated as a large integer

        :return: None
        """
        if sys.platform in ('darwin', 'linux'):
            newpointer = ffi.new(self.type + " *", integer)
        elif sys.platform == 'win32':
            newpointer = self.type(integer)
        self._array_store(self.array_reference, newpointer)

    def get_list(self) -> list:
        r"""
        Get the set atomically

        :return: the set
        """
        result = int.to_bytes(self._array_load(self.array_reference),
                              length=self.size, byteorder='big')
        return self.decode(result)

    def set_list(self, data: list):
        """
        Set the value in the set,
        if the new data is longer than the original size of the set.
        it will expand the set accordingly which would lose atomicy.
        the size of the set can be check with self.size

        :param data: input set
        :return: None
        """

        integer, desiredlength = self.encode(data)

        if 8 >= desiredlength > self.size:
            self.__init__({b'\0\0\0\0\0\0'}, mode=self.mode, encoding=self.encoding)
        if sys.platform in ('darwin', 'linux'):
            newpointer = ffi.new(self.type + " *", integer)
        elif sys.platform == 'win32':
            newpointer = self.type(integer)
        self._array_store(self.array_reference, newpointer)

    value = property(fget=get_list, fset=set_list, doc="same with get_list and set_list")
    int_value = property(fget=get_int, doc="same with get_int")

    def list_store(self, i):
        """
        Atomically store contents from another set to the this set,
        if the other set is different with this one in size , the function will fail.

        :param i: another set to store its value to self
        :return: None
        """
        if self.size != i.size:
            raise ValueError("Input set has different size!")
        self._array_store(self.array_reference, i.array_reference)

    def list_get_and_set(self, data: list) -> list:
        r"""
        Get and set atomically

        :param data: new data set
        :return: the original set
        """

        integer, length = self.encode(data)
        # if length > self.size:
        #    raise ValueError("Input data too long cannot be set atomically!")
        result = int.to_bytes(self._array_get_and_set(self.array_reference, integer),
                              length=self.size, byteorder='big')
        return self.decode(result)

    def list_shift(self, i, j):
        """
        Value exchange between 3 pointers in 2 groups atomically,
        store i in itself after store itself in j

        :param i: one atomic_set
        :param j: another atomic_set
        :return: None
        """
        if self.size != i.size:
            raise ValueError("Comparing set i has different size!")
        if self.size != j.size:
            raise ValueError("Comparing set j has different size!")
        self._array_shift(self.array_reference,
                          i.array_reference, j.array_reference)

    def list_compare_and_set(self, i, n: list) -> bool:
        """
        Compare and set atomically, This compares the contents of self
        with the contents of i. If equal, the operation is a read-modify-write
        operation that writes n into self. If they are not equal,
        the operation is a read and the current contents of itself are written into
        i.

        :param i: the set to be compared with
        :param n: another bytes to be ready to set to self if comparision return True
        :return: if self is equal to i return True, else return False
        """

        if self.size != i.size:
            raise ValueError("Comparing string has different size!")
        integer, length = self.encode(n)
        # if length > self.size:
        #    raise ValueError("Input data too large, cannot set atomically!")
        result = self._array_compare_and_set(self.array_reference,
                                             i.array_reference, integer)
        return result

    def reencode(self, newencode: str):
        """
        Change the encoding of the string, if the original size is not enough,
        it will elongate the string, if 8 bytes are not enough, it will fail.

        :param newencode: new encoding, such as 'utf-8', 'utf-16-le'
        :return: None
        """
        data = self.get_list()
        prev_encoding = self.encoding
        self.encoding = newencode
        try:
            self.set_list(data)
        except ValueError:
            self.encoding = prev_encoding
            self.set_list(data)
            raise ValueError("New encoding took larger space than 8 bytes, cannot elongate!")

    if sys.platform in ('darwin', 'linux'):
        def change_mode(self, newmode='m'):
            """
            Switch between singleprocessing mode and multiprocessing mode,
            the function doesn't exists on windows, since only single processing mode
            is supported on windows platform.
            the contents will be copied , other threads/processes would not be aware of the change.

            :param newmode: the mode to change to, 'm' or 'multiprocessing' for multiproessing, 's' or 'singleprocessing' for singleprocessing. default 'm'
            :return: None
            """
            if newmode in ('m', 'multiprocessing'):
                if self.mode == 's':
                    data = self.get_int()
                    # self.array = Value(ctypes.c_ubyte, self.size, lock=False)
                    # self.array_reference = byref(self.array)
                    self.array = tempfile.TemporaryFile()
                    self.array.write(b'\0' * self.size)
                    self.array.flush()
                    void_pointer = lib.mmap(ffi.NULL, self.size, 3, 1, self.array.fileno(), 0)
                    self.array_reference = ffi.cast(self.type + " *", void_pointer)

                    self.set_int(data)

            elif newmode not in ('s', 'singleprocessing'):
                raise ValueError(
                    "newmode has the wrong value, should be 'm','s','multiprocessing' or 'singleprocessing'")

            elif self.mode == 'm':
                data = self.get_int()
                # self.array = self.type(0)
                # self.array_reference = byref(self.array)
                self.array = ffi.new(self.type + " *")
                self.array_reference = self.array
                self.set_int(data)
            self.mode = newmode

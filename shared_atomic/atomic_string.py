import ctypes
from multiprocessing import Array
from shared_atomic import loaddll
import sys

class atomic_string:
    """
    string provide atomic operations, the string should be no longer than 8 bytes
    """

    def __init__(self, initial: str,
                 mode: str = 'singleprocessing',
                 length: int = None,
                 paddingdirection: str = 'right',
                 paddingstr: str = ' ',
                 trimming_direction: str = 'right',
                 encoding='utf-8'):
        r"""
        constructor to initialize the string,
        the string should be no longer than 8 bytes

        :param initial: initial value of the string, if the initial value is longer than 8 bytes, please specify the trimming target length, or else it would fail.
        :param mode: the mode in which the string will be shared. 'singleprocessing' or 's' for single process, 'multiprocessing' or 'm' for multiprocessing, on windows platform, only singleprocessing is supported, setting it to 'm' or 'multiprocessing' will be ignored.
        :param length: the expected length after padding/trimming for the input value, if not specified, no padding or trimming performed, use original value.
        :param paddingdirection: right, or left side the padding bytes would be added if not specified, pad to the right side, use 'right' or 'r' to specify right side, use 'left' or 'l' to specify the left side.
        :param paddingstr: string to pad to the original bytes, by default '\\0' can be multiple bytes like b'ab', will be padded to the original bytes in circulation until the expected length is reached.
        :param trimming_direction: if initial bytes are longer, on which side the bytes will be trimmed. By default, on the right side, use 'right' or 'r' to specify right side, use 'left' or 'l' to specify the left side.
        """

        self.encoding = encoding
        input_length = len(initial.encode(encoding=self.encoding))

        if length is not None:
            if length > 7:
                raise ValueError("length is longer than expected, "
                                 "should be less than 9 bytes!")

        elif input_length > 7 and length is None:
            raise ValueError("input string is longer than expected, "
                             "should be less than 9 bytes!")

        if length is not None:
            if input_length > length:
                if trimming_direction in('r', 'right'):
                    data = initial.encode(self.encoding)[:length].decode(self.encoding, 'ignore')
                elif trimming_direction in ('l', 'left'):
                    data = initial[::-1].encode(self.encoding)[:length].decode(self.encoding, 'ignore')[::-1]

            elif input_length < length:
                paddingbytes = paddingstr.encode(self.encoding)
                devision , remaining = divmod(length - input_length, len(paddingbytes))
                padding = paddingstr*devision + paddingstr[:remaining]
                if paddingdirection in ('l', 'left'):
                    data = (padding + initial)[::-1].encode(self.encoding)[:length].decode(self.encoding, 'ignore')[::-1]
                elif paddingdirection in ('r', 'right'):
                    data = (initial + padding).encode(self.encoding)[:length].decode(self.encoding, 'ignore')
            else:
                data = initial
        else:
            data = initial

        atomic = loaddll()

        data_byte = data.encode(self.encoding)
        self.initial_byte_length = len(data_byte)

        if self.initial_byte_length == 1:
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

        elif self.initial_byte_length <= 3:
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


        elif self.initial_byte_length <= 7:
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
        else:
            raise ValueError("Input String is longer than 8 bytes!")


        if sys.platform in ('darwin','linux'):
            if mode in ('m', 'multiprocessing'):
                self.mode = 'm'
                self.array = Array(ctypes.c_ubyte, self.size, lock=False)
            elif mode in ('s', 'singleprocessing'):
                self.mode = 's'
                self.array = (ctypes.c_ubyte * self.size)()
            self.array_reference = ctypes.byref(self.array)
            self._set_bytes(data_byte)
        elif sys.platform == 'win32':
            self.mode = 's'

            data_all = (int.to_bytes(self.initial_byte_length, length=1, byteorder='big') +
                        data_byte +b'\0' * (self.size - self.initial_byte_length - 1))[::-1]

            self.array = bytearray(data_all)
            self.array_reference = memoryview(self.array)



    def _str2int(self, input: str):
        r"""
        integer of input string padded with leading length and tailing '\\0'

        :param input: input string
        :return: the integer representation and the length
        """
        input_bytes = input.encode(self.encoding)
        integer = self._byte2int(input_bytes)
        return integer

    def _byte2int(self, input_bytes: bytes):
        """
        integer of input bytes padded with leading length and tailing b'\\0'

        :param input_bytes: input bytes
        :return: the integer representation and the length
        """
        result_bytes = len(input_bytes).to_bytes(length=1, byteorder='big') + self._rpad_zero(input_bytes)
        integer = int.from_bytes(result_bytes, byteorder='big')
        return integer


    def _rpad_zero(self, input: bytes)->bytes:
        r"""
        right pad zero to the input string
        :param input: input bytes

        :return: right padded bytes b'\\0' to self.size -1
        """
        input_length = len(input)
        if input_length < self.size-1:
            return input + (self.size-1-input_length) * b'\0'
        elif input_length > self.size-1:
            raise ValueError('input length longer than its size!')
        else:
            return input

    def _get_int(self):
        """
        Get the integer representation from the string atomically,
        the whole string would be treated as a large integer

        :return: the integer representation
        """
        result = self.type(0)
        self._array_store(ctypes.byref(result), self.array_reference)
        return result.value

    def _set_int(self, input: int):
        """
        Set the integer representation of the string atomically,
        the whole array would be treated as a large integer

        :return: None
        """
        result = self.type(input)
        self._array_store(self.array_reference, ctypes.byref(result))

    def get_string(self):
        r"""
        Get all the bytes from the string atomically

        :param trim: if True, the leading '\\0' would be trimmed, by default: True
        :return: all the bytes in the string
        """
        result = self.type(0)
        self._array_store(ctypes.byref(result), self.array_reference)
        
        result_bytes = int.to_bytes(result.value, length=self.size, byteorder='big')
        length = int.from_bytes(result_bytes[0:1], byteorder='big')
        
        result = int.to_bytes(result.value, length=self.size, byteorder='big')[1:length+1]

        return result.decode(self.encoding)

    def set_string(self, data: str):
        """
        Set the value in the string,
        if the new data is longer than the original size of the string.
        it will expand the string accordingly which would lose atomicy.
        the size of the string can be check with self.size

        :param data: input string
        :return: None
        """
        data_bytes = data.encode(self.encoding)
        self._set_bytes(data_bytes)

    def _set_bytes(self, data: bytes):
        """
        Set the bytes value in the string,
        if the new data is longer than the original size of the string.
        it will expand the string accordingly which would lose atomicy.
        the size of the string can be check with self.size

        :param data: input string
        :return: None
        """

        desiredlength = len(data)

        if 7 >= desiredlength > self.size-1:
            self.resize(desiredlength)
        elif desiredlength > 7:
            raise ValueError()

        integer = self._byte2int(data)
        self._set_int(integer)

        #ctype_integer = self.type(integer)
        #self._array_store(self.array_reference, ctypes.byref(ctype_integer))

    value = property(fget=get_string, fset=set_string, doc="same with get_string and set_string")

    def resize(self, newlength: int,
                 paddingdirection: str = 'right',
                 paddingstr: str = ' ',
                 trimming_direction: str = 'right'):
        r"""
        trim or pad the original contents in the string
        to a new length, the new length should be no longer than 8 bytes,
        the original string wll be replaced with new string, if the original
        string is shared between threads/processes, other threads/processes
        will wouldn't be aware of the change, still use the old string.

        :param newlength: the expected new length of the original bytes.
        :param paddingdirection: if longer than original, left or right sidethe original bytes should be padded, by default right side,use 'right' or 'r' to specify right side, use 'left' or 'l' to specify the left side.
        :param paddingstr: bytes to pad to the original bytes, by default '\\0' can be multiple bytes like b'ab', will be padded to the original bytes in circulation until the expected length is reached.
        :param trimming_direction: if shorted than original, left or right side the original bytes should be padded,use 'right' or 'r' to specify right side,use 'left' or 'l' to specify the left side.
        :return: None
        """

        self.__init__(self.get_string(), mode=self.mode, length=newlength,
                                paddingdirection=paddingdirection,
                                paddingstr=paddingstr,
                                trimming_direction=trimming_direction)

    def string_store(self, i):
        """
        Atomically store contents from another string to the this string,
        if the other string is different with this one in size , the function will fail.

        :param i: another string to store its value to self
        :return:
        """
        if self.size != i.size:
            raise ValueError("Input string has different size!")
        self._array_store(self.array_reference, i.array_reference)

    def string_get_and_set(self, data: str):
        r"""
        Get and set atomically

        :param data: new data
        :return: the original string
        """
        integer = self._str2int(data)
        result = int.to_bytes(self._array_get_and_set(self.array_reference, self.type(integer)),
                                                    length=self.size, byteorder='big')
        result_length = int.from_bytes(result[:1], byteorder='big')
        result_all = result[1:result_length+1]
        return result_all.decode(self.encoding)

    def string_shift(self, i, j):
        """
        Value exchange between 3 pointers in 2 groups atomically,
        the initial_length field will be updated but not atomically.
        store i in itself after store itself in j

        :param i: one atomic_string
        :param j: another atomic_string
        :return: None
        """
        if self.size != i.size:
            raise ValueError("Comparing string i has different size!")
        if self.size != j.size:
            raise ValueError("Comparing string j has different size!")
        self._array_shift(self.array_reference,
                          i.array_reference, j.array_reference)

    def string_compare_and_set(self, i, n: str) -> bool:
        """
        Compare and set atomically, this compares the contents of self
        with the contents of i. If equal, the operation is a read-modify-write
        operation that writes n into self. If they are not equal,
        the operation is a read and the current contents of itself are written into
        i.

        :param i: the string to be compared with
        :param n: another bytes to be ready to self if comparision return True
        :return: if self is equal to i return True, else return False
        """
        if self.size != i.size:
            raise ValueError("Comparing string has different size!")
        integer = self._str2int(n)
        return self._array_compare_and_set(self.array_reference,
                                           i.array_reference, self.type(integer))

    def reencode(self, newencode: str):
        """
        Change the encoding of the string, if the original size is not enough,
        it will elongate the string, if 7 bytes are not enough, it will fail.

        :param newencode: new encoding, such as 'utf-8', 'utf-16-le'
        :return: None
        """
        data = self.get_string()
        new_data = data.encode(newencode)
        self._set_bytes(new_data)
        self.encoding = newencode

    if sys.platform in ('darwin','linux'):
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
                    data = self._get_int()
                    self.array = Array(ctypes.c_ubyte, self.size, lock=False)
                    self.array_reference = ctypes.byref(self.array)
                    self._set_int(data)

            elif newmode not in ('s', 'singleprocessing'):
                raise ValueError("newmode has the wrong value, should be 'm','s','multiprocessing' or 'singleprocessing'")

            elif self.mode == 'm':
                data = self._get_int()
                self.array = (ctypes.c_ubyte * self.size)()
                self.array_reference = ctypes.byref(self.array)
                self._set_int(data)
            self.mode = newmode



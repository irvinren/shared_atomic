import sys
import ctypes

if sys.platform in ("linux", "darwin"):
    import shared_atomic_.lib
    from shared_atomic_ import ffi
    import tempfile
    lib = shared_atomic_.lib
elif sys.platform in ("win32"):
    from shared_atomic import load_wrapped_dll
    lib = load_wrapped_dll()

class atomic_bytearray:
    """
    bytearray provide atomic operations, the bytearray should be no longer than 8 bytes
    """

    def __init__(self, initial: bytes,
                 mode: str = 'singleprocessing',
                 length: int = None,
                 paddingdirection: str = 'right',
                 paddingbytes: bytes = b'\0',
                 trimming_direction: str = 'right'):
        r"""
        constructor to initialize the bytearray,
        the bytearray should be no longer than 8 bytes

        :param initial: initial value of the bytearray, if the initial value is longer than 8 bytes, please specify the trimming target length, or else it would fail.
        :param mode: the mode in which the bytearray will be shared. 'singleprocessing' or 's' for single process, 'multiprocessing' or 'm' for multiprocessing, on windows platform, only singleprocessing is supported, setting it to 'm' or 'multiprocessing' will be ignored.
        :param length: the expected length after padding/trimming for the input value, if not specified, no padding or trimming performed, use original value.
        :param paddingdirection: right, or left side the padding bytes would be added if not specified, pad to the right side, use 'right' or 'r' to specify right side, use 'left' or 'l' to specify the left side.
        :param paddingbytes: bytes to pad to the original bytes, by default b'\\0' can be multiple bytes like b'ab', will be padded to the original bytes in circulation until the expected length is reached.
        :param trimming_direction: if initial bytes are longer, on which side the bytes will be trimmed. By default, on the right side, use 'right' or 'r' to specify right side, use 'left' or 'l' to specify the left side.
        """

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
                if trimming_direction in ('r', 'right'):
                    data = initial[:length]
                elif trimming_direction in ('l', 'left'):
                    data = initial[input_length - length:]

            elif input_length < length:
                devision, remaining = divmod(length - input_length, len(paddingbytes))
                padding = paddingbytes * devision + paddingbytes[:remaining]
                if paddingdirection in ('l', 'left'):
                    data = padding + initial
                elif paddingdirection in ('r', 'right'):
                    data = initial + padding
            else:
                data = initial
        else:
            data = initial



        self.initial_length = len(data)
        if self.initial_length == 1:

            self.size = 1
            if sys.platform in ('darwin', 'linux'):
                self.type = "unsigned char"
                self._array_load = lib.ubyte_load
                self._array_store = lib.ubyte_store
                self._array_get_and_set = lib.ubyte_get_and_set
                self._array_shift = lib.ubyte_shift
                self._array_compare_and_set = lib.ubyte_compare_and_set
                self._array_add_and_fetch = lib.ubyte_add_and_fetch
                self._array_sub_and_fetch = lib.ubyte_sub_and_fetch
                self._array_and_and_fetch = lib.ubyte_and_and_fetch
                self._array_or_and_fetch = lib.ubyte_or_and_fetch
                self._array_xor_and_fetch = lib.ubyte_xor_and_fetch
                self._array_nand_and_fetch = lib.ubyte_nand_and_fetch
                self._array_fetch_and_add = lib.ubyte_fetch_and_add
                self._array_fetch_and_sub = lib.ubyte_fetch_and_sub
                self._array_fetch_and_and = lib.ubyte_fetch_and_and
                self._array_fetch_and_or = lib.ubyte_fetch_and_or
                self._array_fetch_and_xor = lib.ubyte_fetch_and_xor
                self._array_fetch_and_nand = lib.ubyte_fetch_and_nand
            elif sys.platform == 'win32':
                self.type = ctypes.c_ubyte
                self._array_load = lib.ubyte_load
                self._array_store = lib.ubyte_store
                self._array_get_and_set = lib.ubyte_get_and_set
                self._array_shift = lib.ubyte_shift
                self._array_compare_and_set = lib.ubyte_compare_and_set
                self._array_add_and_fetch = lib.ubyte_add_and_fetch
                self._array_sub_and_fetch = lib.ubyte_sub_and_fetch
                self._array_and_and_fetch = lib.ubyte_and_and_fetch
                self._array_or_and_fetch = lib.ubyte_or_and_fetch
                self._array_xor_and_fetch = lib.ubyte_xor_and_fetch
                self._array_nand_and_fetch = lib.ubyte_nand_and_fetch
                self._array_fetch_and_add = lib.ubyte_fetch_and_add
                self._array_fetch_and_sub = lib.ubyte_fetch_and_sub
                self._array_fetch_and_and = lib.ubyte_fetch_and_and
                self._array_fetch_and_or = lib.ubyte_fetch_and_or
                self._array_fetch_and_xor = lib.ubyte_fetch_and_xor
                self._array_fetch_and_nand = lib.ubyte_fetch_and_nand

        elif self.initial_length == 2:
            self.size = 2
            if sys.platform in ('darwin', 'linux'):
                self.type = "unsigned short"
                self._array_load = lib.ushort_load
                self._array_store = lib.ushort_store
                self._array_get_and_set = lib.ushort_get_and_set
                self._array_shift = lib.ushort_shift
                self._array_compare_and_set = lib.ushort_compare_and_set
                self._array_add_and_fetch = lib.ushort_add_and_fetch
                self._array_sub_and_fetch = lib.ushort_sub_and_fetch
                self._array_and_and_fetch = lib.ushort_and_and_fetch
                self._array_or_and_fetch = lib.ushort_or_and_fetch
                self._array_xor_and_fetch = lib.ushort_xor_and_fetch
                self._array_nand_and_fetch = lib.ushort_nand_and_fetch
                self._array_fetch_and_add = lib.ushort_fetch_and_add
                self._array_fetch_and_sub = lib.ushort_fetch_and_sub
                self._array_fetch_and_and = lib.ushort_fetch_and_and
                self._array_fetch_and_or = lib.ushort_fetch_and_or
                self._array_fetch_and_xor = lib.ushort_fetch_and_xor
                self._array_fetch_and_nand = lib.ushort_fetch_and_nand
            elif sys.platform == 'win32':
                self.type = ctypes.c_ushort
                self._array_load = lib.ushort_load
                self._array_store = lib.ushort_store
                self._array_get_and_set = lib.ushort_get_and_set
                self._array_shift = lib.ushort_shift
                self._array_compare_and_set = lib.ushort_compare_and_set
                self._array_add_and_fetch = lib.ushort_add_and_fetch
                self._array_sub_and_fetch = lib.ushort_sub_and_fetch
                self._array_and_and_fetch = lib.ushort_and_and_fetch
                self._array_or_and_fetch = lib.ushort_or_and_fetch
                self._array_xor_and_fetch = lib.ushort_xor_and_fetch
                self._array_nand_and_fetch = lib.ushort_nand_and_fetch
                self._array_fetch_and_add = lib.ushort_fetch_and_add
                self._array_fetch_and_sub = lib.ushort_fetch_and_sub
                self._array_fetch_and_and = lib.ushort_fetch_and_and
                self._array_fetch_and_or = lib.ushort_fetch_and_or
                self._array_fetch_and_xor = lib.ushort_fetch_and_xor
                self._array_fetch_and_nand = lib.ushort_fetch_and_nand

        elif self.initial_length <= 4:
            self.size = 4
            if sys.platform in ('darwin', 'linux'):
                self.type = "unsigned int"
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
            self.size = 8
            if sys.platform in ('darwin', 'linux'):
                self.type = "unsigned long long"
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
            raise ValueError("Input bytearray is longer than 8 bytes!")

        if sys.platform in ("linux", "darwin"):
            if mode in ('m', 'multiprocessing'):
                self.mode = 'm'
                # self.array = Array(ctypes.c_ubyte, self.size, lock=False)
                self.array = tempfile.TemporaryFile()
                self.array.write(b'\0' * self.size)
                self.array.flush()
                void_pointer = lib.mmap(ffi.NULL, self.size, 3, 1, self.array.fileno(), 0)
                self.array_reference = ffi.cast(self.type + " *", void_pointer)

            elif mode in ('s', 'singleprocessing'):
                self.mode = 's'
                self.array = ffi.new(self.type + " *")
                self.array_reference = self.array
            self.array_get_and_set(data)

        elif sys.platform in ("win32"):
            self.mode = 's'
            #data = b'\0' * (self.size - len(data)) + data
            #self.array = bytearray(data)
            self.array = int.from_bytes(data, byteorder='big')
            self.array_reference = self.type(self.array)

    if sys.platform in ("linux", "darwin"):
        def __del__(self):
            if self.mode == 'm':
                lib.munmap(self.array_reference, self.size)
                self.array.close()

    def get_int(self) -> int:
        """
        Get the integer representation from the bytearray,
        the whole array would be treated as a large integer

        :return: the integer representation
        """
        return self._array_load(self.array_reference)

    def get_bytes(self, trim=True) -> bytes:
        r"""
        Get all the bytes from the bytearray atomically
        :param trim: if True, the leading b'\\0' would be trimmed, by default: True

        :return: all the bytes in the bytearray
        """

        result = self._array_load(self.array_reference)
        if trim:
            result = int.to_bytes(result, length=self.size, byteorder='big').lstrip(b'\0')
        else:
            result = int.to_bytes(result, length=self.size, byteorder='big')
        return result

    def set_bytes(self, data: bytes):
        """
        Set the value in the bytearray,
        if the new data is longer than the original size of the array.
        it will expand the array accordingly which would lose atomicy.
        the size of the bytearray can be check with self.size

        :param data: input bytearray
        :return: None
        """


        desiredlength = len(data)
        if 8 >= desiredlength > self.size:
            self.resize(desiredlength)
        elif desiredlength > 8:
            raise ValueError()
        integer = int.from_bytes(data, byteorder='big')
        if sys.platform in ('darwin', 'linux'):
            newpointer = ffi.new(self.type + " *", integer)
        elif sys.platform == 'win32':
            newpointer = self.type(integer)
        self._array_store(self.array_reference, newpointer)
        self.initial_length = desiredlength

    def _get_full_bytes(self):
        return self.get_bytes(trim=False)

    value = property(fget=_get_full_bytes, fset=set_bytes, doc="same with get_bytes without trimming and set_bytes")
    int_value = property(fget=get_int, doc="same with get_int")

    def resize(self, newlength: int,
               paddingdirection: str = 'right',
               paddingbytes: bytes = b'\0',
               trimming_direction: str = 'right'):
        r"""
        trim or pad the original contents in the bytearray
        to a new length, the new length should be no longer than 8 bytes,
        the original array wll be replaced with new array, if the original
        array is shared between threads/processes, other threads/processes
        will wouldn't be aware of the change, still use the old bytearray.

        :param newlength: the expected new length of the original bytes.
        :param paddingdirection: if longer than original, left or right sidethe original bytes should be padded, by default right side,use 'right' or 'r' to specify right side, use 'left' or 'l' to specify the left side.
        :param paddingbytes: bytes to pad to the original bytes, by default b'\\0' can be multiple bytes like b'ab', will be padded to the original bytes in circulation until the expected length is reached.
        :param trimming_direction: if shorted than original, left or right side the original bytes should be padded,use 'right' or 'r' to specify right side,use 'left' or 'l' to specify the left side.
        :return: None
        """

        self.__init__(self.get_bytes(trim=False), mode=self.mode, length=newlength,
                      paddingdirection=paddingdirection,
                      paddingbytes=paddingbytes,
                      trimming_direction=trimming_direction)

    def array_store(self, i):
        """
        Atomically store contents from another bytearray to the this bytearray,
        if the other bytearray is different with this one in size , the function will fail.

        :param i: another bytearray to store its value to self
        :return:
        """
        if self.size != i.size:
            raise ValueError("Input bytearray has different size!")
        self._array_store(self.array_reference, i.array_reference)
        self.initial_length = i.initial_length

    def array_get_and_set(self, data: bytes, trim=True) -> bytes:
        r"""
        Get and set atomically

        :param data: new data
        :param trim: whether of not to trim the returning b'\\0' when get, default True

        :return: the original bytes
        """


        integer = int.from_bytes(data, byteorder='big')
        result = int.to_bytes(self._array_get_and_set(self.array_reference, integer),
                              length=self.size, byteorder='big')
        self.initial_length = len(data)
        return result.lstrip(b'\0') if trim else result

    def array_shift(self, i, j):
        """
        Value exchange between 3 pointers in 2 groups atomically,
        the initial_length field will be updated but not atomically.
        store i in itself after store itself in j

        :param i: one atomic_bytearray
        :param j: another atomic_bytearray
        :return: None
        """
        if self.size != i.size:
            raise ValueError("Comparing bytearray i has different size!")
        if self.size != j.size:
            raise ValueError("Comparing bytearray j has different size!")
        self._array_shift(self.array_reference,
                          i.array_reference, j.array_reference)
        j.initial_length = self.initial_length
        self.initial_length = i.initial_length

    def array_compare_and_set(self, i, n: bytes) -> bool:
        """
        Compare and set atomically,This compares the contents of self
        with the contents of i. If equal, the operation is a read-modify-write
        operation that writes n into self. If they are not equal,
        the operation is a read and the current contents of itself are written into
        i.

        :param i: the bytearray to be compared with
        :param n: another bytes to be ready to set to self if comparision return True
        :return: if self is equal to i return True, else return False
        """

        if self.size != i.size:
            raise ValueError("Comparing string has different size!")
        integer = int.from_bytes(n, byteorder='big')
        result = self._array_compare_and_set(self.array_reference,
                                             i.array_reference, integer)
        if result:
            self.initial_length = len(n)

        return result

    def array_add_and_fetch(self, n: bytes, trim=True) -> bytes:
        r"""
        Increment and fetch atomically

        :param n: bytes will be added to the array.
        :param trim: whether of not to trim the returning b'\\0' when fetch, default True
        :return: the contents of resulted bytearray
        """

        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_add_and_fetch(self.array_reference, integer),
                              length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result

    def array_sub_and_fetch(self, n: bytes, trim=True) -> bytes:
        r"""
        Decrement and fetch atomically

        :param n: bytes will be subtracted from the array.
        :param trim: whether of not to trim the returning b'\\0' when fetch, default True
        :return: the contents of resulted bytearray
        """

        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_sub_and_fetch(self.array_reference, integer),
                              length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result

    def array_and_and_fetch(self, n: bytes, trim=True) -> bytes:
        r"""
        Bitwise AND and fetch the result atomically

        :param n: the other operand of AND operation.
        :param trim: whether of not to trim the returning b'\\0' when fetch, default True
        :return: the contents of resulted bytearray
        """

        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_and_and_fetch(self.array_reference, integer),
                              length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result

    def array_or_and_fetch(self, n: bytes, trim=True) -> bytes:
        r"""
        bitsise OR and fetch the result atomically

        :param n: the other operand of OR operation
        :param trim: whether of not to trim the returning b'\\0' when fetch, default True
        :return: the contents of resulted bytearray
        """

        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_or_and_fetch(self.array_reference, integer),
                              length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result

    def array_xor_and_fetch(self, n: bytes, trim=True) -> bytes:
        r"""
        bitsise XOR and fetch the result atomically

        :param n: the other operand of XOR operation
        :param trim: whether of not to trim the returning b'\\0' when fetch, default True
        :return: the contents of resulted bytearray
        """

        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_xor_and_fetch(self.array_reference, integer),
                              length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result

    def array_nand_and_fetch(self, n: bytes, trim=True) -> bytes:
        r"""
        bitsise NAND(AND first then NOT) and fetch the result atomically

        :param n:the other operand of NAND operation
        :param trim: whether of not to trim the returning b'\\0' when fetch, default True
        :return: the contents of resulted bytearray
        """

        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_nand_and_fetch(self.array_reference, integer),
                              length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result

    def array_fetch_and_add(self, n: bytes, trim=True) -> bytes:
        r"""
        fetch and increment atomically

        :param n: the bytes will be added to the array
        :param trim: whether of not to trim the returning b'\\0' when fetch, default True

        :return: the original contents of the bytearray
        """

        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_fetch_and_add(self.array_reference, integer),
                              length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result

    def array_fetch_and_sub(self, n: bytes, trim=True) -> bytes:
        r"""
        fetch and decrement atomically

        :param n: the bytes will be substracted from the array
        :param trim: whether of not to trim the returning b'\\0' when fetch, default True
        :return: the original contents of the bytearray
        """

        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_fetch_and_sub(self.array_reference, integer),
                              length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result

    def array_fetch_and_and(self, n: bytes, trim=True) -> bytes:
        r"""
        Fetch then bitwise AND atomically

        :param n: the other operands of AND operation
        :param trim: whether of not to trim the returning b'\\0' when fetch, default True
        :return: the original contents of the bytearray
        """

        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_fetch_and_and(self.array_reference, integer),
                              length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result

    def array_fetch_and_or(self, n: bytes, trim=True) -> bytes:
        r"""
        Fetch then bitwise OR atomically

        :param n: the other operands of OR operation
        :param trim: whether of not to trim the returning b'\\0' when fetch, default True
        :return: the original contents of the bytearray
        """

        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_fetch_and_or(self.array_reference, integer),
                              length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result

    def array_fetch_and_xor(self, n: bytes, trim=True) -> bytes:
        r"""
        Fetch then bitwise XOR atomically

        :param n: the other operands of XOR operation
        :param trim: whether of not to trim the returning b'\\0' when fetch, default True
        :return: the original contents of the bytearray
        """

        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_fetch_and_xor(self.array_reference, integer),
                              length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result

    def array_fetch_and_nand(self, n: bytes, trim=True) -> bytes:
        r"""
        fetch then bitwise NAND(AND first then NOT) atomically

        :param n: the other operands of NAND operation
        :param trim: whether of not to trim the returning b'\\0' when fetch, default True
        :return: the original contents of the bytearray
        """

        integer = int.from_bytes(n, byteorder='big')
        result = int.to_bytes(self._array_fetch_and_nand(self.array_reference, integer),
                              length=self.size, byteorder='big')
        return result.lstrip(b'\0') if trim else result

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
                    data = self.get_bytes(trim=False)
                    # self.array = Array(ctypes.c_ubyte, self.size, lock=False)
                    # self.array_reference = ctypes.byref(self.array)

                    self.array = tempfile.TemporaryFile()
                    self.array.write(b'\0' * self.size)
                    self.array.flush()
                    void_pointer = lib.mmap(ffi.NULL, self.size, 3, 1, self.array.fileno(), 0)
                    self.array_reference = ffi.cast(self.type + " *", void_pointer)

                    self.set_bytes(data)

            elif newmode not in ('s', 'singleprocessing'):
                raise ValueError(
                    "newmode has the wrong value, should be 'm','s','multiprocessing' or 'singleprocessing'")

            elif self.mode == 'm':
                data = self.get_bytes(trim=False)
                # self.array = (ctypes.c_ubyte * self.size)()
                # self.array_reference = ctypes.byref(self.array)
                self.array = ffi.new(self.type + " *")
                self.array_reference = self.array
                self.set_bytes(data)
            self.mode = newmode

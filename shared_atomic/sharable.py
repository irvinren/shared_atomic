from typing import TypeVar, Generic
import mmap
import tempfile
import struct
from shared_atomic_ import ffi
from shared_atomic_ import lib


T = TypeVar('T')


class sharable64(Generic[T]):
    def __init__(self, value: T, encoding='utf-8'):
        self.encoding = encoding
        encoded_value, self.type, self.length = self.encode(value)
        self.tempfile = tempfile.TemporaryFile()
        self.tempfile.write(b'\0\0\0\0\0\0\0\0')
        self.tempfile.flush()
        void_pointer = lib.mmap(ffi.NULL, 8, 3, 1, self.tempfile.fileno(), 0)
        self.reference = ffi.cast("long long *", void_pointer)
        int_value = int.from_bytes(encoded_value, byteorder='big', signed=True)
        lib.longlong_get_and_set(self.reference, int_value)

    def decode(self, input: bytes) ->T:
        if self.type == 'int_s':
            return int.from_bytes(input, byteorder='big', signed=True)
        elif self.type == 'bool':
            return True if input[0] else False
        elif self.type == 'bytes':
            return input
        elif self.type == 'str':
            return input.decode(self.encoding)
        elif self.type == 'float':
            return struct.unpack('d',input)

    def encode(self, value: T)-> (bytes, str, int):
        if isinstance(value, int):
            result = int.to_bytes(value, length=8, byteorder='big', signed=True)
            return result, 'int_s', 8

        elif isinstance(value, bool):
            result = 1 if value else 0
            return result, 'bool', 1

        elif isinstance(value, bytes):
            length = len(T)
            if length > 8:
                raise ValueError("Input bytes too long!")
            return value, 'bytes', length

        elif isinstance(value, str):
            input_bytes = value.encode(self.encoding)
            length = len(input_bytes)
            if length > 8:
                raise ValueError("Input string too long!")
            return input_bytes, 'str', length

        elif isinstance(value, float):
            input_bytes = struct.pack('d',value)
            length = len(input_bytes)
            if length > 8:
                raise ValueError("Input string too long!")
            return input_bytes, 'float', length

        else:
            raise TypeError("Unsupported Type!")

    def get(self) -> T:
        result = lib.longlong_load(self.reference)
        bytes_value = int.to_bytes(result, self.length, byteorder='big', signed=True)
        return self.decode(bytes_value)

    def set(self, value: T):
        newbytes, newtype, newlength = self.encode(value)
        int_value = int.to_bytes(newbytes, newlength, byteorder='big', signed=True)
        lib.ulonglong_get_and_set(self.reference, int_value)



def test_sharable64():
    a = sharable64(2 ** 63-1)
    assert a.get() == 2 ** 63-1
from shared_atomic import atomic_bytearray
import ctypes

a = None

def setup_function():
    """
    pre function for pytest
    :return: None
    """
    global a
    # if sys.platform in ('darwin','linux'):
    #     dlltype = ctypes.CDLL
    #     os.chdir('/Users/philren/.local/share/virtualenvs/spark-examples--HrH57AW/lib/python3.6/site-packages')
    #     filename = 'shared_atomic.cpython-36m-darwin.so'
    # elif sys.platform == "win32":
    #     dlltype = ctypes.windll
    # else:
    #     return
    #atomic = ctypes.LibraryLoader(dlltype).LoadLibrary(filename)
    a = atomic_bytearray(b'ab1234567', length=7)

def teardown_function():
    pass

def test_init():
    a = atomic_bytearray(b'ab')
    assert a.get_bytes() == b'ab'
    a = atomic_bytearray(b'ab', length=7, paddingdirection='l', paddingbytes=b'012')
    assert a.get_bytes() == b'01201ab'
    a = atomic_bytearray(b'ab', length=7)
    assert a.get_bytes() == b'ab\0\0\0\0\0'
    a = atomic_bytearray(b'ab1234567', length=7, trimming_direction='l')
    assert a.get_bytes() == b'1234567'
    a = atomic_bytearray(b'ab1234567', length=7)
    assert a.get_bytes() == b'ab12345'


def test_resize():
    a.resize(8)
    assert a.get_bytes() == b'ab12345\0'
    a.resize(7)
    assert a.get_bytes() == b'ab12345'
    a.resize(8, paddingbytes=b'a', paddingdirection='l')
    assert a.get_bytes() == b'aab12345'
    a.resize(7, trimming_direction='l')
    assert a.get_bytes() == b'ab12345'
    a.resize(8, paddingbytes=b'a', paddingdirection='r')
    assert a.get_bytes() == b'ab12345a'

def test_bytes():
    a = atomic_bytearray(b'ab', length=7, paddingdirection='r', paddingbytes=b'012', mode='m')
    #a.array_get_and_set(ctypes.c_ulonglong(int.from_bytes(b'ab', byteorder='big')))
    a.get_bytes() == b'ab01201'
    a.set_bytes(b'abc')

    aa = atomic_bytearray(b'aa', length=7, paddingdirection='r', paddingbytes=b'012', mode='m')
    bb = atomic_bytearray(b'bb', length=7, paddingdirection='r', paddingbytes=b'012', mode='m')
    result =aa.array_compare_and_set(bb, b'ab')

    assert result == False
    assert bb.get_bytes() == aa.get_bytes()

    result = aa.array_compare_and_set(bb, b'ab')

    assert result == True
    assert aa.get_bytes(trim=True) == b'ab'

    result = aa.array_fetch_and_and(bytes.fromhex('ff01'))
    assert result == b'ab'
    assert aa.get_bytes(trim=True) == b'a\x00'

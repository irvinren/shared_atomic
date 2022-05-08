from shared_atomic import atomic_bytearray
import random
import sys
from threading import Thread
from multiprocessing import Process

a = None

inlist = (
         int.to_bytes(1, length=1, byteorder='big'),
         int.to_bytes(2**8+1, length=2, byteorder='big'),
         int.to_bytes(2**24+1, length=4, byteorder='big'),
         int.to_bytes(2**56+1, length=8, byteorder='big'),
)

inintlist = (
         1,
         2 ** 8 + 1,
         2 ** 24 + 1,
         2 ** 56 + 1,
)

exlist = (int.to_bytes(255, length=1, byteorder='big'),
          int.to_bytes(2 ** 16 - 1, length=2, byteorder='big'),
          int.to_bytes(2 ** 32 - 1, length=4, byteorder='big'),
          int.to_bytes(2 ** 64 - 1, length=8, byteorder='big'),
          )
exintlist = (255,
          2 ** 16 - 1,
          2 ** 32 - 1,
          2 ** 64 - 1,
          )

sublist = (
           int.to_bytes(100, length=1, byteorder='big'),
           int.to_bytes(100, length=2, byteorder='big'),
           int.to_bytes(100, length=4, byteorder='big'),
           int.to_bytes(100, length=8, byteorder='big'),
           )
subintlist = (100,100,100,100)

andlist = []
orlist = []
xorlist = []
nandlist = []
andintlist = []
orintlist = []
xorintlist = []
nandintlist = []

addlist = sublist
addintlist = subintlist

r = random.Random()

for i in range(4):
    andintlist.append(r.randrange(0, 128))
    andlist.append(int.to_bytes(andintlist[i],length=1, byteorder='big'))
    orintlist.append(r.randrange(0, 128))
    orlist.append(int.to_bytes(orintlist[i],length=1, byteorder='big'))
    xorintlist.append(r.randrange(0, 128))
    xorlist.append(int.to_bytes(xorintlist[i],length=1, byteorder='big'))
    nandintlist.append(r.randrange(0, 128))
    nandlist.append(int.to_bytes(nandintlist[i],length=1, byteorder='big'))


def signed2unsigned(input, i):
    if input < 0:
        return int.to_bytes(input + 2**((i+1)*8),length=i+1, byteorder='big').lstrip(b'\0')
    return int.to_bytes(input,length=2**i, byteorder='big').lstrip(b'\0')


def setup_function():
    """
    pre function for pytest
    :return: None
    """
    global a
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
    #a=atomic_bytearray()
    a.resize(8)
    assert a.get_bytes() == b'ab12345'
    a.resize(7, trimming_direction='l')
    assert a.get_bytes() == b'ab12345'
    a.resize(8, paddingbytes=b'a', paddingdirection='l')
    assert a.get_bytes() == b'ab12345'
    a.resize(7, trimming_direction='l')
    assert a.get_bytes() == b'ab12345'
    a.resize(8, paddingbytes=b'a', paddingdirection='r')
    assert a.get_bytes() == b'ab12345'

def test_bytes():
    a = atomic_bytearray(b'ab', length=7, paddingdirection='r', paddingbytes=b'012', mode='m')
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


def test_value_bytearray():
    """
    test single process single thread
    :return: None
    """
    i = 0
    result = None
    try:
        for i in range(4):
            a = atomic_bytearray(b'a'*(2**i))
            result=[]
            b = atomic_bytearray(inlist[i])
            a.array_store(b)
            assert a.get_bytes() == inlist[i]
            result.append(a.array_get_and_set(exlist[i]))
            assert result[-1] == inlist[i]
            assert a.get_bytes() == exlist[i]
            c = []
            c.append(atomic_bytearray(exlist[i]))
            result.append(a.array_compare_and_set(c[-1], inlist[i]))
            assert result[-1]
            assert a.get_bytes() == inlist[i]
            c.append(atomic_bytearray(inlist[i]))
            c.append(atomic_bytearray(exlist[i]))
            result.append(a.array_shift(c[-1], c[-2]))
            assert c[-1].get_bytes() == a.get_bytes()
            assert c[-2].get_bytes() == inlist[i]
            result.append(a.array_sub_and_fetch(sublist[i]))
            assert result[-1] == int.to_bytes(exintlist[i] - addintlist[i], length=2**i,byteorder='big')
            assert a.get_bytes() == result[-1]
            result.append(a.array_add_and_fetch(addlist[i]))
            assert result[-1] == exlist[i]
            assert a.get_bytes() == result[-1]
            result.append(a.array_and_and_fetch(andlist[i]))
            assert result[-1] == signed2unsigned(exintlist[i] & andintlist[i],i)
            assert a.get_bytes() == result[-1]
            result.append(a.array_or_and_fetch(orlist[i]))
            assert result[-1] == signed2unsigned((exintlist[i] & andintlist[i]) | orintlist[i],i)
            assert a.get_bytes() == result[-1]
            result.append(a.array_xor_and_fetch(xorlist[i]))
            assert result[-1] == signed2unsigned(((exintlist[i] & andintlist[i]) | orintlist[i]) ^ xorintlist[i],i)
            assert a.get_bytes() == result[-1]
            result.append(a.array_nand_and_fetch(nandlist[i]))
            assert result[-1] ==\
                   signed2unsigned(
                        ~((((exintlist[i] & andintlist[i]) | orintlist[i]) ^ xorintlist[i]) & nandintlist[i]),i
                   ).rjust(a.size, b'\xff')

            assert a.get_bytes() == result[-1]
            b = atomic_bytearray(exlist[i])
            a.array_store(b)
            result.append(a.array_fetch_and_sub(sublist[i]))
            assert result[-1] == exlist[i]
            assert a.get_bytes() == int.to_bytes(exintlist[i] - subintlist[i], length=2**i,byteorder='big')
            result.append(a.array_fetch_and_add(addlist[i]))
            assert result[-1] == int.to_bytes(exintlist[i] - subintlist[i], length=2**i,byteorder='big')
            assert a.get_bytes() == exlist[i]
            result.append(a.array_fetch_and_and(andlist[i]))
            assert result[-1] == exlist[i]
            assert a.get_bytes() == signed2unsigned(exintlist[i] & andintlist[i],i)
            result.append(a.array_fetch_and_or(orlist[i]))
            assert result[-1] == signed2unsigned(exintlist[i] & andintlist[i],i)
            assert a.get_bytes() == signed2unsigned((exintlist[i] & andintlist[i]) | orintlist[i],i)
            result.append(a.array_fetch_and_xor(xorlist[i]))
            assert result[-1] == signed2unsigned((exintlist[i] & andintlist[i]) | orintlist[i],i)
            assert a.get_bytes() == signed2unsigned(((exintlist[i] & andintlist[i]) | orintlist[i]) ^ xorintlist[i],i)
            result.append(a.array_fetch_and_nand(nandlist[i]))
            assert result[-1] == signed2unsigned(((exintlist[i] & andintlist[i]) | orintlist[i]) ^ xorintlist[i],i)
            assert a.get_bytes() == signed2unsigned(
                ~((((exintlist[i] & andintlist[i]) | orintlist[i]) ^ xorintlist[i]) & nandintlist[i]),i
            ).rjust(a.size, b'\xff')

            if sys.platform != 'win32':
                value = a.get_bytes(trim=False)
                a.change_mode('m')
                assert value == a.get_bytes(trim=False)
                assert a.mode == 'm'
                a.change_mode('s')
                assert value == a.get_bytes(trim=False)
                assert a.mode == 's'

            i += 1
    except Exception as e:
        print(e)
        print(i)
        raise e


def thread_run(a):
    a.array_sub_and_fetch(b'\x0F')


def test_thread_atomic():
    """
    test single process multiple threads
    :return: None
    """
    a = atomic_bytearray(b'ab', length=7, paddingdirection='r', paddingbytes=b'012', mode='s')

    threadlist=[]

    for i in range(10000):
        threadlist.append(Thread(target=thread_run, args=(a,)))

    for i in range(10000):
        threadlist[i].start()

    for i in range(10000):
        threadlist[i].join()

    assert a.value == int.to_bytes(27411031864108609,length=8,byteorder='big')


if sys.platform != "win32":
    def process_run(a):
        a.array_sub_and_fetch(b'\x0F')

    def test_process_atomic():
        """
        test multiple processes
        :return: None
        """
        a = atomic_bytearray(b'ab', length=7, paddingdirection='r', paddingbytes=b'012', mode='m')

        processlist = []
        for i in range(10000):
            processlist.append(Process(target=process_run, args=(a,)))

        for i in range(10000):
            processlist[i].start()

        for i in range(10000):
            processlist[i].join()

        assert a.value == int.to_bytes(27411031864108609,length=8,byteorder='big')


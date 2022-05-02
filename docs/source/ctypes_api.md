# ctypes API Referennce

There are 16 kinds of numeric ctypes that could be updated atomically, these types
are listed below:

|original ctypes | atomic functions |
| -------------- | ---------------- |
| c_bool         | bool_*           |
| c_byte         | byte_*           |
| c_wchar        | wchar_*          |
| c_ubyte        | ubyte_*          |
| c_short        | short_*          |
| c_ushort       | ushort_*         |
| c_int          | int_*            |
| c_uint         | uint_*           |
| c_long         | long_*           |
| c_ulong        | ulong_*          |
| c_longlong     | longlong_*       |
| c_ulonglong    | ulonglong_*      |
| c_size_t       | size_t_*         |
| c_ssize_t      | ssize_t_*        |
| c_float        | float_store      |
| c_double       | double_store     |
| c_longdouble   | longdouble_store |

## shared_atomic.loaddll()

```{eval-rst}
 .. automodule:: shared_atomic
    :members:
```

## Integer types support 17 kinds of APIs could be used to achieve atomic operations, 

- store value atomically

  *type*_store(*type* *, *type* *);

- get and set atomically

  *type* *type*_get_and_set(*type* *, *type*);

- compare and set atomically

  *type* *type*_compare_and_set(*type* *, *type* *, *type*);
  
- value exchange between 3 pointers in 2 groups atomically, store b in a after store a in c

  *type*_shift(*type* *a, *type* *b, *type* *c);

- increment and fetch atomically

  _Bool *type*_add_and_fetch(*type* *, *type*);

- decrement and fetch atomically

  *type* *type*_sub_and_fetch(*type* *, *type*);

- bitwise AND and fetch the result atomically

  *type* *type*_and_and_fetch(*type* *, *type*);
  
- bitsise OR and fetch the result atomically

  *type* *type*_or_and_fetch(*type* *, *type*);
  
- bitsise XOR and fetch the result atomically

  *type* *type*_xor_and_fetch(*type* *, *type*);
  
- bitsise NAND(AND first then NOT) and fetch the result atomically

  *type* *type*_nand_and_fetch(*type* *, *type*);
  
- fetch and increment atomically

  _Bool *type*_fetch_and_add(*type* *, *type*);

- fetch and decrement atomically

  *type* *type*_fetch_and_sub(*type* *, *type*);

- fetch then bitwise AND atomically

  *type* *type*_fetch_and_and(*type* *, *type*);
  
- fetch then bitwise OR atomically

  *type* *type*_fetch_and_or(*type* *, *type*);
  
- fetch then bitwise XOR atomically

  *type* *type*_fetch_and_xor(*type* *, *type*);
  
- fetch then bitwise NAND atomically

  *type* *type*_fetch_and_nand(*type* *, *type*);

floating types supports only 1 kind, 

- store value atomically

  *type*_store(*type* *, *type* *);

## bool atomic functions:

`void bool_store(_Bool *, _Bool *);`

`_Bool bool_get_and_set(_Bool *, _Bool);`

`_Bool bool_compare_and_set(_Bool *, _Bool *, _Bool);`

`void bool_shift(_Bool *v, _Bool *, _Bool *);`

## byte atomic functions:

`void byte_store(char *, char *);`

`char byte_get_and_set(char *, char);`

`void byte_shift(char *v, char *, char*);`

`_Bool byte_compare_and_set(char *, char *, char);`

`char byte_add_and_fetch(char *, char);`

`char byte_sub_and_fetch(char *, char);`

`char byte_and_and_fetch(char *, char);`

`char byte_or_and_fetch(char *, char);`

`char byte_xor_and_fetch(char *, char);`

`char byte_nand_and_fetch(char *, char);`

`char byte_fetch_and_add(char *, char);`

`char byte_fetch_and_sub(char *, char);`

`char byte_fetch_and_and(char *, char);`

`char byte_fetch_and_or(char *, char);`

`char byte_fetch_and_xor(char *, char);`

`char byte_fetch_and_nand(char *, char);`

## ubyte atomic functions:

`void ubyte_store(unsigned char *, unsigned char *);`

`unsigned char ubyte_get_and_set(unsigned char *, unsigned char);`

`void ubyte_shift(unsigned char *, unsigned char *, unsigned char *);`

`_Bool ubyte_compare_and_set(unsigned char *, unsigned char *, unsigned char);`

`unsigned char ubyte_add_and_fetch(unsigned char *, unsigned char);`

`unsigned char ubyte_sub_and_fetch(unsigned char *, unsigned char);`

`unsigned char ubyte_and_and_fetch(unsigned char *, unsigned char);`

`unsigned char ubyte_or_and_fetch(unsigned char *, unsigned char);`

`unsigned char ubyte_xor_and_fetch(unsigned char *, unsigned char);`

`unsigned char ubyte_nand_and_fetch(unsigned char *, unsigned char);`

`unsigned char ubyte_fetch_and_add(unsigned char *, unsigned char);`

`unsigned char ubyte_fetch_and_sub(unsigned char *, unsigned char);`

`unsigned char ubyte_fetch_and_and(unsigned char *, unsigned char);`

`unsigned char ubyte_fetch_and_or(unsigned char *, unsigned char);`

`unsigned char ubyte_fetch_and_xor(unsigned char *, unsigned char);`

`unsigned char ubyte_fetch_and_nand(unsigned char *, unsigned char);`


## short atomic functions:

`void short_store(short *, short *);`

`short short_get_and_set(short *, short);`

`void short_shift(short *v, short *, short *);`

`_Bool short_compare_and_set(short *, short *, short);`

`short short_add_and_fetch(short *, short);`

`short short_sub_and_fetch(short *, short);`

`short short_and_and_fetch(short *, short);`

`short short_or_and_fetch(short *, short);`

`short short_xor_and_fetch(short *, short);`

`short short_nand_and_fetch(short *, short);`

`short short_fetch_and_add(short *, short);`

`short short_fetch_and_sub(short *, short);`

`short short_fetch_and_and(short *, short);`

`short short_fetch_and_or(short *, short);`

`short short_fetch_and_xor(short *, short);`

`short short_fetch_and_nand(short *, short);`

## ushort atomic functions:

`void ushort_store(unsigned short *, unsigned short *);`

`unsigned short ushort_get_and_set(unsigned short *, unsigned short);`

`void ushort_shift(unsigned short *, unsigned short *, unsigned short *);`

`_Bool ushort_compare_and_set(unsigned short *, unsigned short *, unsigned short);`

`unsigned short ushort_add_and_fetch(unsigned short *, unsigned short);`

`unsigned short ushort_sub_and_fetch(unsigned short *, unsigned short);`

`unsigned short ushort_and_and_fetch(unsigned short *, unsigned short);`

`unsigned short ushort_or_and_fetch(unsigned short *, unsigned short);`

`unsigned short ushort_xor_and_fetch(unsigned short *, unsigned short);`

`unsigned short ushort_nand_and_fetch(unsigned short *, unsigned short);`

`unsigned short ushort_fetch_and_add(unsigned short *, unsigned short);`

`unsigned short ushort_fetch_and_sub(unsigned short *, unsigned short);`

`unsigned short ushort_fetch_and_and(unsigned short *, unsigned short);`

`unsigned short ushort_fetch_and_or(unsigned short *, unsigned short);`

`unsigned short ushort_fetch_and_xor(unsigned short *, unsigned short);`

`unsigned short ushort_fetch_and_nand(unsigned short *, unsigned short);`

## int atomic functions:

`void int_store(int *, int *);`

`int int_get_and_set(int *, int);`

`void int_shift(int *, int *, int* );`

`_Bool int_compare_and_set(int *, int *, int);`

`int int_add_and_fetch(int *, int);`

`int int_sub_and_fetch(int *, int);`

`int int_and_and_fetch(int *, int);`

`int int_or_and_fetch(int *, int);`

`int int_xor_and_fetch(int *, int);`

`int int_nand_and_fetch(int *, int);`

`int int_fetch_and_add(int *, int);`

`int int_fetch_and_sub(int *, int);`

`int int_fetch_and_and(int *, int);`

`int int_fetch_and_or(int *, int);`

`int int_fetch_and_xor(int *, int);`

`int int_fetch_and_nand(int *, int);`

## uint atomic functions:

`void uint_store(unsigned int *, unsigned int *);`

`unsigned int uint_get_and_set(unsigned int *, unsigned int);`

`void uint_shift(unsigned int *, unsigned int *, unsigned int *);`

`_Bool uint_compare_and_set(unsigned int *, unsigned int *, unsigned int);`

`unsigned int uint_add_and_fetch(unsigned int *, unsigned int);`

`unsigned int uint_sub_and_fetch(unsigned int *, unsigned int);`

`unsigned int uint_and_and_fetch(unsigned int *, unsigned int);`

`unsigned int uint_or_and_fetch(unsigned int *, unsigned int);`

`unsigned int uint_xor_and_fetch(unsigned int *, unsigned int);`

`unsigned int uint_nand_and_fetch(unsigned int *, unsigned int);`

`unsigned int uint_fetch_and_add(unsigned int *, unsigned int);`

`unsigned int uint_fetch_and_sub(unsigned int *, unsigned int);`

`unsigned int uint_fetch_and_and(unsigned int *, unsigned int);`

`unsigned int uint_fetch_and_or(unsigned int *, unsigned int);`

`unsigned int uint_fetch_and_xor(unsigned int *, unsigned int);`

`unsigned int uint_fetch_and_nand(unsigned int *, unsigned int);`

## wchar atomic functions:

`void wchar_store(wchar_t *, wchar_t *);`

`wchar_t wchar_get_and_set(wchar_t *, wchar_t);`

`void wchar_shift(wchar_t *, wchar_t *, wchar_t*);`

`_Bool wchar_compare_and_set(wchar_t *, wchar_t *, wchar_t);`

`wchar_t wchar_add_and_fetch(wchar_t *, wchar_t);`

`wchar_t wchar_sub_and_fetch(wchar_t *, wchar_t);`

`wchar_t wchar_fetch_and_add(wchar_t *, wchar_t);`

`wchar_t wchar_fetch_and_sub(wchar_t *, wchar_t);`

## long atomic functions(the size of long type is 64bit on Linux/MacOSX, 32bit on Windows):

`void long_store(long *, long *);`

`void long_shift(long *, long *, long*);`

`long long_get_and_set(long *, long);`

`_Bool long_compare_and_set(long *, long *, long);`

`long long_add_and_fetch(long *, long);`

`long long_sub_and_fetch(long *, long);`

`long long_and_and_fetch(long *, long);`

`long long_or_and_fetch(long *, long);`

`long long_xor_and_fetch(long *, long);`

`long long_nand_and_fetch(long *, long);`

`long long_fetch_and_add(long *, long);`

`long long_fetch_and_sub(long *, long);`

`long long_fetch_and_and(long *, long);`

`long long_fetch_and_or(long *, long);`

`long long_fetch_and_xor(long *, long);`

`long long_fetch_and_nand(long *, long);`

## ulong atomic functions:

`void ulong_store(unsigned long *, unsigned long *);`

`unsigned long ulong_get_and_set(unsigned long *, unsigned long );`

`void ulong_shift(unsigned long *, unsigned long *, unsigned long *);`

`_Bool ulong_compare_and_set(unsigned long *, unsigned long *, unsigned long);`

`unsigned long ulong_add_and_fetch(unsigned long *, unsigned long);`

`unsigned long ulong_sub_and_fetch(unsigned long *, unsigned long);`

`unsigned long ulong_and_and_fetch(unsigned long *, unsigned long);`

`unsigned long ulong_or_and_fetch(unsigned long *, unsigned long);`

`unsigned long ulong_xor_and_fetch(unsigned long *, unsigned long);`

`unsigned long ulong_nand_and_fetch(unsigned long *, unsigned long);`

`unsigned long ulong_fetch_and_add(unsigned long *, unsigned long);`

`unsigned long ulong_fetch_and_sub(unsigned long *, unsigned long);`

`unsigned long ulong_fetch_and_and(unsigned long *, unsigned long);`

`unsigned long ulong_fetch_and_or(unsigned long *, unsigned long);`

`unsigned long ulong_fetch_and_xor(unsigned long *, unsigned long);`

`unsigned long ulong_fetch_and_nand(unsigned long *, unsigned long);`

## size_t atomic functions:

`void size_t_store(size_t *, size_t *);`

`size_t size_t_get_and_set(size_t *, size_t);`

`void size_t_shift(size_t *v, size_t *, size_t *);`

`_Bool size_t_compare_and_set(size_t *, size_t *, size_t);`

`size_t size_t_add_and_fetch(size_t *, size_t);`

`size_t size_t_sub_and_fetch(size_t *, size_t);`

`size_t size_t_and_and_fetch(size_t *, size_t);`

`size_t size_t_or_and_fetch(size_t *, size_t);`

`size_t size_t_xor_and_fetch(size_t *, size_t);`

`size_t size_t_nand_and_fetch(size_t *, size_t);`

`size_t size_t_fetch_and_add(size_t *, size_t);`

`size_t size_t_fetch_and_sub(size_t *, size_t);`

`size_t size_t_fetch_and_and(size_t *, size_t);`

`size_t size_t_fetch_and_or(size_t *, size_t);`

`size_t size_t_fetch_and_xor(size_t *, size_t);`

`size_t size_t_fetch_and_nand(size_t *, size_t);`

## ssize_t atomic functions:

`void ssize_t_store(ssize_t *, ssize_t *);`

`ssize_t ssize_t_get_and_set(ssize_t *, ssize_t);`

`void ssize_t_shift(ssize_t *, ssize_t *, ssize_t *);`

`_Bool ssize_t_compare_and_set(ssize_t *, ssize_t *, ssize_t);`

`ssize_t ssize_t_add_and_fetch(ssize_t *, ssize_t);`

`ssize_t ssize_t_sub_and_fetch(ssize_t *, ssize_t);`

`ssize_t ssize_t_and_and_fetch(ssize_t *, ssize_t);`

`ssize_t ssize_t_or_and_fetch(ssize_t *, ssize_t);`

`ssize_t ssize_t_xor_and_fetch(ssize_t *, ssize_t);`

`ssize_t ssize_t_nand_and_fetch(ssize_t *, ssize_t);`

`ssize_t ssize_t_fetch_and_add(ssize_t *, ssize_t);`

`ssize_t ssize_t_fetch_and_sub(ssize_t *, ssize_t);`

`ssize_t ssize_t_fetch_and_and(ssize_t *, ssize_t);`

`ssize_t ssize_t_fetch_and_or(ssize_t *, ssize_t);`

`ssize_t ssize_t_fetch_and_xor(ssize_t *, ssize_t);`

`ssize_t ssize_t_fetch_and_nand(ssize_t *, ssize_t);`

## long long atomic functions:

`void longlong_store(long long *, long long *);`

`long long longlong_get_and_set(long long *, long long);`

`void longlong_shift(long long *, long long *, long long *);`

`_Bool longlong_compare_and_set(long long *, long long *, long long);`

`long long longlong_add_and_fetch(long long *, long long);`

`long long longlong_sub_and_fetch(long long *, long long);`

`long long longlong_and_and_fetch(long long *, long long);`

`long long longlong_or_and_fetch(long long *, long long);`

`long long longlong_xor_and_fetch(long long *, long long);`

`long long longlong_nand_and_fetch(long long *, long long);`

`long long longlong_fetch_and_add(long long *, long long);`

`long long longlong_fetch_and_sub(long long *, long long);`

`long long longlong_fetch_and_and(long long *, long long);`

`long long longlong_fetch_and_or(long long *, long long);`

`long long longlong_fetch_and_xor(long long *, long long);`

`long long longlong_fetch_and_nand(long long *, long long);`

## unsigned long long atomic functions:

`void ulonglong_store(unsigned long long *, unsigned long long *);`

`unsigned long long ulonglong_get_and_set(unsigned long long *, unsigned long long);`

`void ulonglong_shift(unsigned long long *, unsigned long long *, unsigned long long *);`

`_Bool ulonglong_compare_and_set(unsigned long long *, unsigned long long *, unsigned long long);`

`unsigned long long ulonglong_add_and_fetch(unsigned long long *, unsigned long long);`

`unsigned long long ulonglong_sub_and_fetch(unsigned long long *, unsigned long long);`

`unsigned long long ulonglong_and_and_fetch(unsigned long long *, unsigned long long);`

`unsigned long long ulonglong_or_and_fetch(unsigned long long *, unsigned long long);`

`unsigned long long ulonglong_xor_and_fetch(unsigned long long *, unsigned long long);`

`unsigned long long ulonglong_nand_and_fetch(unsigned long long *, unsigned long long);`

`unsigned long long ulonglong_fetch_and_add(unsigned long long *, unsigned long long);`

`unsigned long long ulonglong_fetch_and_sub(unsigned long long *, unsigned long long);`

`unsigned long long ulonglong_fetch_and_and(unsigned long long *, unsigned long long);`

`unsigned long long ulonglong_fetch_and_or(unsigned long long *, unsigned long long);`

`unsigned long long ulonglong_fetch_and_xor(unsigned long long *, unsigned long long);`

`unsigned long long ulonglong_fetch_and_nand(unsigned long long *, unsigned long long);`

## float atomic functions:

`void float_store(float *v, float *n);`

## double atomic functions:

`void double_store(double *v, double *n);`

## long double atomic functions:

`void longdouble_store(long double *v, long double *n);`
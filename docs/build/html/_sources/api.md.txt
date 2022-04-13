# API Referennce

There are 16 kinds of numeric ctypes that could be updated atomically, these types
are listed below:

|original ctypes | atomic functions |
| -------------- | ---------------- |
| c_bool         | bool_*           |
| c_char         | byte_*           |
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

Integer types support 5 kinds of APIs could be used to achieve atomic operations, 

- store value atomically

  *type*_store(type *, type *);

- increment and fetch atomically

  _Bool *type*_add_and_fetch(*type* *, *type*);

- substract and fetch atomically

  *type* *type*_sub_and_fetch(*type* *, *type*);

- get and set atomically

  *type* *type*_get_and_set(*type* *, *type*);

- compare and set atomically

  *type* *type*_compare_and_set(*type* *, *type* *, *type*);

floating types supports only 1 kind, 

- store value atomically

  *type*_store(type *, type *);

## bool atomic functions:

`void bool_store(_Bool *, _Bool *);`

`_Bool bool_add_and_fetch(_Bool *, _Bool);`

`_Bool bool_sub_and_fetch(_Bool *, _Bool);`

`_Bool bool_get_and_set(_Bool *, _Bool);`

`_Bool bool_compare_and_set(_Bool *, _Bool *, _Bool);`

## byte atomic functions:

`void byte_store(char *, char *);`

`char byte_add_and_fetch(char *, char);`

`char byte_sub_and_fetch(char *, char);`

`char byte_get_and_set(char *, char);`

`_Bool byte_compare_and_set(char *, char *, char);`

## ubyte atomic functions:

`void ubyte_store(unsigned char *, unsigned char *);`

`unsigned char ubyte_add_and_fetch(unsigned char *, unsigned char);`

`unsigned char ubyte_sub_and_fetch(unsigned char *, unsigned char);`

`unsigned char ubyte_get_and_set(unsigned char *, unsigned char);`

`_Bool ubyte_compare_and_set(unsigned char *, unsigned char *, unsigned char);`

## short atomic functions:

`void short_store(short *, short *);`

`short short_add_and_fetch(short *, short);`

`short short_sub_and_fetch(short *, short);`

`short short_get_and_set(short *, short);`

`_Bool short_compare_and_set(short *, short *, short);`

## ushort atomic functions:

`void ushort_store(unsigned short *, unsigned short *);`

`unsigned short ushort_add_and_fetch(unsigned short *, unsigned short);`

`unsigned short ushort_sub_and_fetch(unsigned short *, unsigned short);`

`unsigned short ushort_get_and_set(unsigned short *, unsigned short);`

`_Bool ushort_compare_and_set(unsigned short *, unsigned short *, unsigned short);`

## int atomic functions:

`void int_store(int *, int *);`

`int int_add_and_fetch(int *, int);`

`int int_sub_and_fetch(int *, int);`

`int int_get_and_set(int *, int);`

`_Bool int_compare_and_set(int *, int *, int);`

## uint atomic functions:

`void uint_store(unsigned int *, unsigned int *);`

`unsigned int uint_add_and_fetch(unsigned int *, unsigned int);`

`unsigned int uint_sub_and_fetch(unsigned int *, unsigned int);`

`unsigned int uint_get_and_set(unsigned int *, unsigned int);`

`_Bool uint_compare_and_set(unsigned int *, unsigned int *, unsigned int);`

## wchar atomic functions:

`void wchar_store(wchar_t *, wchar_t *);`

`wchar_t wchar_add_and_fetch(wchar_t *, wchar_t);`

`wchar_t wchar_sub_and_fetch(wchar_t *, wchar_t);`

`wchar_t wchar_get_and_set(wchar_t *, wchar_t);`

`_Bool wchar_compare_and_set(wchar_t *, wchar_t *, wchar_t);`

## long atomic functions:

`void long_store(long *, long *);`

`long long_add_and_fetch(long *, long);`

`long long_sub_and_fetch(long *, long);`

`long long_get_and_set(long *, long);`

`_Bool long_compare_and_set(long *, long *, long);`

## ulong atomic functions:

`void ulong_store(unsigned long *, unsigned long *);`

`unsigned long ulong_add_and_fetch(unsigned long *, unsigned long);`

`unsigned long ulong_sub_and_fetch(unsigned long *, unsigned long);`

`unsigned long ulong_get_and_set(unsigned long *, unsigned long);`

`_Bool ulong_compare_and_set(unsigned long *, unsigned long *, unsigned long);`

## size_t atomic functions:

`void size_t_store(size_t *, size_t *);`

`size_t size_t_add_and_fetch(size_t *, size_t);`

`size_t size_t_sub_and_fetch(size_t *, size_t);`

`size_t size_t_get_and_set(size_t *, size_t);`

`_Bool size_t_compare_and_set(size_t *, size_t *, size_t);`

## ssize_t atomic functions:

`void ssize_t_store(ssize_t *, ssize_t *);`

`ssize_t ssize_t_add_and_fetch(ssize_t *, ssize_t);`

`ssize_t ssize_t_sub_and_fetch(ssize_t *, ssize_t);`

`ssize_t ssize_t_get_and_set(ssize_t *, ssize_t);`

`_Bool ssize_t_compare_and_set(ssize_t *, ssize_t *, ssize_t);`

## long long atomic functions:

`void longlong_store(long long *, long long *);`

`long long longlong_add_and_fetch(long long *, long long);`

`long long longlong_sub_and_fetch(long long *, long long);`

`long long longlong_get_and_set(long long *, long long);`

`_Bool longlong_compare_and_set(long long *, long long *, long long);`

## unsigned long long atomic functions:

`void ulonglong_store(unsigned long long *, unsigned long long *);`

`unsigned long long ulonglong_add_and_fetch(unsigned long long *, unsigned long long);`

`unsigned long long ulonglong_sub_and_fetch(unsigned long long *, unsigned long long);`

`unsigned long long ulonglong_get_and_set(unsigned long long *, unsigned long long);`

`_Bool ulonglong_compare_and_set(unsigned long long *, unsigned long long *, unsigned long long);`

## float atomic functions:

`void float_store(float *v, float *n);`

## double atomic functions:

`void double_store(double *v, double *n);`

## long double atomic functions:

`void longdouble_store(long double *v, long double *n);`

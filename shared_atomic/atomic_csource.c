#include <stddef.h>
#include <sys/types.h>



void bool_store(_Bool *v, _Bool *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};

_Bool bool_get_and_set(_Bool *v, _Bool n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool bool_compare_and_set(_Bool *v, _Bool *e, _Bool n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

void byte_store(char *v, char *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
char byte_add_and_fetch(char *v, char i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
char byte_sub_and_fetch(char *v, char i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
char byte_get_and_set(char *v, char n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool byte_compare_and_set(char *v, char *e, char n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

void ubyte_store(unsigned char *v, unsigned char *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
unsigned char ubyte_add_and_fetch(unsigned char *v, unsigned char i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned char ubyte_sub_and_fetch(unsigned char *v, unsigned char i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned char ubyte_get_and_set(unsigned char *v, unsigned char n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool ubyte_compare_and_set(unsigned char *v, unsigned char *e, unsigned char n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

void short_store(short *v, short *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
short short_add_and_fetch(short *v, short i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
short short_sub_and_fetch(short *v, short i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
short short_get_and_set(short *v, short n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool short_compare_and_set(short *v, short *e, short n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

void ushort_store(unsigned short *v, unsigned short *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
unsigned short ushort_add_and_fetch(unsigned short *v, unsigned short i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned short ushort_sub_and_fetch(unsigned short *v, unsigned short i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned short ushort_get_and_set(unsigned short *v, unsigned short n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool ushort_compare_and_set(unsigned short *v, unsigned short *e, unsigned short n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

void wchar_store(wchar_t *v, wchar_t *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
wchar_t wchar_add_and_fetch(wchar_t *v, wchar_t i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
wchar_t wchar_sub_and_fetch(wchar_t *v, wchar_t i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
wchar_t wchar_get_and_set(wchar_t *v, wchar_t n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool wchar_compare_and_set(wchar_t *v, wchar_t *e, wchar_t n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

void int_store(int *v, int *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
int int_add_and_fetch(int *v, int i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
int int_sub_and_fetch(int *v, int i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
int int_get_and_set(int *v, int n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool int_compare_and_set(int *v, int *e, int n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

void uint_store(unsigned int *v, unsigned int *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
unsigned int uint_add_and_fetch(unsigned int *v, unsigned int i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned int uint_sub_and_fetch(unsigned int *v, unsigned int i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned int uint_get_and_set(unsigned int *v, unsigned int n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool uint_compare_and_set(unsigned int *v, unsigned int *e, unsigned int n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};


void long_store(long *v, long *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
long long_add_and_fetch(long *v, long i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
long long_sub_and_fetch(long *v, long i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
long long_get_and_set(long *v, long n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool long_compare_and_set(long *v, long *e, long n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

void ulong_store(unsigned long *v, unsigned long *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
unsigned long ulong_add_and_fetch(unsigned long *v, unsigned long i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned long ulong_sub_and_fetch(unsigned long *v, unsigned long i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned long ulong_get_and_set(unsigned long *v, unsigned long n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool ulong_compare_and_set(unsigned long *v, unsigned long *e, unsigned long n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

void size_t_store(size_t *v, size_t *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
size_t size_t_add_and_fetch(size_t *v, size_t i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
size_t size_t_sub_and_fetch(size_t *v, size_t i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
size_t size_t_get_and_set(size_t *v, size_t n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool size_t_compare_and_set(size_t *v, size_t *e, size_t n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

void ssize_t_store(ssize_t *v, ssize_t *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
ssize_t ssize_t_add_and_fetch(ssize_t *v, ssize_t i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
ssize_t ssize_t_sub_and_fetch(ssize_t *v, ssize_t i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
ssize_t ssize_t_get_and_set(ssize_t *v, ssize_t n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool ssize_t_compare_and_set(ssize_t *v, ssize_t *e, ssize_t n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

void longlong_store(long long *v, long long *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
long long longlong_add_and_fetch(long long *v, long long i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
long long longlong_sub_and_fetch(long long *v, long long i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
long long longlong_get_and_set(long long *v, long long n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool longlong_compare_and_set(long long *v, long long *e, long long n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

void ulonglong_store(unsigned long long *v, unsigned long long *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
unsigned long long ulonglong_add_and_fetch(unsigned long long *v, unsigned long long i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned long long ulonglong_sub_and_fetch(unsigned long long *v, unsigned long long i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned long long ulonglong_get_and_set(unsigned long long *v, unsigned long long n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool ulonglong_compare_and_set(unsigned long long *v, unsigned long long *e, unsigned long long n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};


void float_store(float *v, float *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
/*float float_add_and_fetch(float *v, float i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
float float_sub_and_fetch(float *v, float i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
float float_get_and_set(float *v, float n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool float_compare_and_set(float *v, float *e, float n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};*/

void double_store(double *v, double *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
/*double double_add_and_fetch(double *v, double i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
double double_sub_and_fetch(double *v, double i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
double double_get_and_set(double *v, double n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool double_compare_and_set(double *v, double *e, double n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};*/

void longdouble_store(long double *v, long double *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
/*long double longdouble_add_and_fetch(long double *v, long double i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
long double longdouble_sub_and_fetch(long double *v, long double i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
long double longdouble_get_and_set(long double *v, long double n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool longdouble_compare_and_set(long double *v, long double *e, long double n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};*/


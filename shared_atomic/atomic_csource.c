#include <stddef.h>
#include <sys/types.h>


_Bool bool_load(_Bool *ptr){
    return __atomic_load_n(ptr, __ATOMIC_SEQ_CST);
}
void bool_store(_Bool *v, _Bool *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
_Bool bool_get_and_set(_Bool *v, _Bool n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
void bool_shift(_Bool *v, _Bool *n, _Bool* r) {
    return __atomic_exchange(v, n, r,__ATOMIC_SEQ_CST);
};
_Bool bool_compare_and_set(_Bool *v, _Bool *e, _Bool n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

char byte_load(char *ptr){
    return __atomic_load_n(ptr, __ATOMIC_SEQ_CST);
}
void byte_store(char *v, char *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
char byte_get_and_set(char *v, char n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
void byte_shift(char *v, char *n, char* r) {
    return __atomic_exchange(v, n, r,__ATOMIC_SEQ_CST);
};
_Bool byte_compare_and_set(char *v, char *e, char n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

char byte_add_and_fetch(char *v, char i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
char byte_sub_and_fetch(char *v, char i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
char byte_and_and_fetch(char *v, char i) {
    return __atomic_and_fetch(v, i, __ATOMIC_SEQ_CST);
};
char byte_or_and_fetch(char *v, char i) {
    return __atomic_or_fetch(v, i, __ATOMIC_SEQ_CST);
};
char byte_xor_and_fetch(char *v, char i) {
    return __atomic_xor_fetch(v, i, __ATOMIC_SEQ_CST);
};
char byte_nand_and_fetch(char *v, char i) {
    return __atomic_nand_fetch(v, i, __ATOMIC_SEQ_CST);
};

char byte_fetch_and_add(char *v, char i) {
    return __atomic_fetch_add(v, i, __ATOMIC_SEQ_CST);
};
char byte_fetch_and_sub(char *v, char i) {
    return __atomic_fetch_sub(v, i, __ATOMIC_SEQ_CST);
};
char byte_fetch_and_and(char *v, char i) {
    return __atomic_fetch_and(v, i, __ATOMIC_SEQ_CST);
};
char byte_fetch_and_or(char *v, char i) {
    return __atomic_fetch_or(v, i, __ATOMIC_SEQ_CST);
};
char byte_fetch_and_xor(char *v, char i) {
    return __atomic_fetch_xor(v, i, __ATOMIC_SEQ_CST);
};
char byte_fetch_and_nand(char *v, char i) {
    return __atomic_fetch_nand(v, i, __ATOMIC_SEQ_CST);
};



unsigned char ubyte_load(unsigned char *ptr){
    return __atomic_load_n(ptr, __ATOMIC_SEQ_CST);
}
void ubyte_store(unsigned char *v, unsigned char *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
void ubyte_shift(unsigned char *v, unsigned char *n, unsigned char* r) {
    return __atomic_exchange(v, n, r,__ATOMIC_SEQ_CST);
};
unsigned char ubyte_get_and_set(unsigned char *v, unsigned char n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool ubyte_compare_and_set(unsigned char *v, unsigned char *e, unsigned char n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};


unsigned char ubyte_add_and_fetch(unsigned char *v, unsigned char i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned char ubyte_sub_and_fetch(unsigned char *v, unsigned char i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned char ubyte_and_and_fetch(unsigned char *v, unsigned char i) {
    return __atomic_and_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned char ubyte_or_and_fetch(unsigned char *v, unsigned char i) {
    return __atomic_or_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned char ubyte_xor_and_fetch(unsigned char *v, unsigned char i) {
    return __atomic_xor_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned char ubyte_nand_and_fetch(unsigned char *v, unsigned char i) {
    return __atomic_nand_fetch(v, i, __ATOMIC_SEQ_CST);
};

unsigned char ubyte_fetch_and_add(unsigned char *v, unsigned char i) {
    return __atomic_fetch_add(v, i, __ATOMIC_SEQ_CST);
};
unsigned char ubyte_fetch_and_sub(unsigned char *v, unsigned char i) {
    return __atomic_fetch_sub(v, i, __ATOMIC_SEQ_CST);
};
unsigned char ubyte_fetch_and_and(unsigned char *v, unsigned char i) {
    return __atomic_fetch_and(v, i, __ATOMIC_SEQ_CST);
};
unsigned char ubyte_fetch_and_or(unsigned char *v, unsigned char i) {
    return __atomic_fetch_or(v, i, __ATOMIC_SEQ_CST);
};
unsigned char ubyte_fetch_and_xor(unsigned char *v, unsigned char i) {
    return __atomic_fetch_xor(v, i, __ATOMIC_SEQ_CST);
};
unsigned char ubyte_fetch_and_nand(unsigned char *v, unsigned char i) {
    return __atomic_fetch_nand(v, i, __ATOMIC_SEQ_CST);
};

short short_load(short *ptr){
    return __atomic_load_n(ptr, __ATOMIC_SEQ_CST);
}
void short_store(short *v, short *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
void short_shift(short *v, short *n, short* r) {
    return __atomic_exchange(v, n, r,__ATOMIC_SEQ_CST);
};
short short_get_and_set(short *v, short n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool short_compare_and_set(short *v, short *e, short n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

short short_add_and_fetch(short *v, short i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
short short_sub_and_fetch(short *v, short i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
short short_and_and_fetch(short *v, short i) {
    return __atomic_and_fetch(v, i, __ATOMIC_SEQ_CST);
};
short short_or_and_fetch(short *v, short i) {
    return __atomic_or_fetch(v, i, __ATOMIC_SEQ_CST);
};
short short_xor_and_fetch(short *v, short i) {
    return __atomic_xor_fetch(v, i, __ATOMIC_SEQ_CST);
};
short short_nand_and_fetch(short *v, short i) {
    return __atomic_nand_fetch(v, i, __ATOMIC_SEQ_CST);
};

short short_fetch_and_add(short *v, short i) {
    return __atomic_fetch_add(v, i, __ATOMIC_SEQ_CST);
};
short short_fetch_and_sub(short *v, short i) {
    return __atomic_fetch_sub(v, i, __ATOMIC_SEQ_CST);
};
short short_fetch_and_and(short *v, short i) {
    return __atomic_fetch_and(v, i, __ATOMIC_SEQ_CST);
};
short short_fetch_and_or(short *v, short i) {
    return __atomic_fetch_or(v, i, __ATOMIC_SEQ_CST);
};
short short_fetch_and_xor(short *v, short i) {
    return __atomic_fetch_xor(v, i, __ATOMIC_SEQ_CST);
};
short short_fetch_and_nand(short *v, short i) {
    return __atomic_fetch_nand(v, i, __ATOMIC_SEQ_CST);
};


unsigned short ushort_load(unsigned short *ptr){
    return __atomic_load_n(ptr, __ATOMIC_SEQ_CST);
};

void ushort_store(unsigned short *v, unsigned short *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
void ushort_shift(unsigned short *v, unsigned short *n, unsigned short* r) {
    return __atomic_exchange(v, n, r,__ATOMIC_SEQ_CST);
};
unsigned short ushort_get_and_set(unsigned short *v, unsigned short n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool ushort_compare_and_set(unsigned short *v, unsigned short *e, unsigned short n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

unsigned short ushort_add_and_fetch(unsigned short *v, unsigned short i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned short ushort_sub_and_fetch(unsigned short *v, unsigned short i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned short ushort_and_and_fetch(unsigned short *v, unsigned short i) {
    return __atomic_and_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned short ushort_or_and_fetch(unsigned short *v, unsigned short i) {
    return __atomic_or_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned short ushort_xor_and_fetch(unsigned short *v, unsigned short i) {
    return __atomic_xor_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned short ushort_nand_and_fetch(unsigned short *v, unsigned short i) {
    return __atomic_nand_fetch(v, i, __ATOMIC_SEQ_CST);
};

unsigned short ushort_fetch_and_add(unsigned short *v, unsigned short i) {
    return __atomic_fetch_add(v, i, __ATOMIC_SEQ_CST);
};
unsigned short ushort_fetch_and_sub(unsigned short *v, unsigned short i) {
    return __atomic_fetch_sub(v, i, __ATOMIC_SEQ_CST);
};
unsigned short ushort_fetch_and_and(unsigned short *v, unsigned short i) {
    return __atomic_fetch_and(v, i, __ATOMIC_SEQ_CST);
};
unsigned short ushort_fetch_and_or(unsigned short *v, unsigned short i) {
    return __atomic_fetch_or(v, i, __ATOMIC_SEQ_CST);
};
unsigned short ushort_fetch_and_xor(unsigned short *v, unsigned short i) {
    return __atomic_fetch_xor(v, i, __ATOMIC_SEQ_CST);
};
unsigned short ushort_fetch_and_nand(unsigned short *v, unsigned short i) {
    return __atomic_fetch_nand(v, i, __ATOMIC_SEQ_CST);
};

wchar_t wchar_load(wchar_t *ptr){
    return __atomic_load_n(ptr, __ATOMIC_SEQ_CST);
};

void wchar_store(wchar_t *v, wchar_t *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
void wchar_shift(wchar_t *v, wchar_t *n, wchar_t* r) {
    return __atomic_exchange(v, n, r,__ATOMIC_SEQ_CST);
};
wchar_t wchar_get_and_set(wchar_t *v, wchar_t n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool wchar_compare_and_set(wchar_t *v, wchar_t *e, wchar_t n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

wchar_t wchar_add_and_fetch(wchar_t *v, wchar_t i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
wchar_t wchar_sub_and_fetch(wchar_t *v, wchar_t i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
wchar_t wchar_fetch_and_add(wchar_t *v, wchar_t i) {
    return __atomic_fetch_add(v, i, __ATOMIC_SEQ_CST);
};
wchar_t wchar_fetch_and_sub(wchar_t *v, wchar_t i) {
    return __atomic_fetch_sub(v, i, __ATOMIC_SEQ_CST);
};

int int_load(int *ptr){
    return __atomic_load_n(ptr, __ATOMIC_SEQ_CST);
};

void int_store(int *v, int *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
void int_shift(int *v, int *n, int* r) {
    return __atomic_exchange(v, n, r,__ATOMIC_SEQ_CST);
};
int int_get_and_set(int *v, int n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool int_compare_and_set(int *v, int *e, int n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

int int_add_and_fetch(int *v, int i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
int int_sub_and_fetch(int *v, int i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
int int_and_and_fetch(int *v, int i) {
    return __atomic_and_fetch(v, i, __ATOMIC_SEQ_CST);
};
int int_or_and_fetch(int *v, int i) {
    return __atomic_or_fetch(v, i, __ATOMIC_SEQ_CST);
};
int int_xor_and_fetch(int *v, int i) {
    return __atomic_xor_fetch(v, i, __ATOMIC_SEQ_CST);
};
int int_nand_and_fetch(int *v, int i) {
    return __atomic_nand_fetch(v, i, __ATOMIC_SEQ_CST);
};

int int_fetch_and_add(int *v, int i) {
    return __atomic_fetch_add(v, i, __ATOMIC_SEQ_CST);
};
int int_fetch_and_sub(int *v, int i) {
    return __atomic_fetch_sub(v, i, __ATOMIC_SEQ_CST);
};
int int_fetch_and_and(int *v, int i) {
    return __atomic_fetch_and(v, i, __ATOMIC_SEQ_CST);
};
int int_fetch_and_or(int *v, int i) {
    return __atomic_fetch_or(v, i, __ATOMIC_SEQ_CST);
};
int int_fetch_and_xor(int *v, int i) {
    return __atomic_fetch_xor(v, i, __ATOMIC_SEQ_CST);
};
int int_fetch_and_nand(int *v, int i) {
    return __atomic_fetch_nand(v, i, __ATOMIC_SEQ_CST);
};

unsigned int uint_load(unsigned int *ptr){
    return __atomic_load_n(ptr, __ATOMIC_SEQ_CST);
};
void uint_store(unsigned int *v, unsigned int *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
void uint_shift(unsigned int *v, unsigned int *n, unsigned int* r) {
    return __atomic_exchange(v, n, r,__ATOMIC_SEQ_CST);
};
unsigned int uint_get_and_set(unsigned int *v, unsigned int n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool uint_compare_and_set(unsigned int *v, unsigned int *e, unsigned int n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

unsigned int uint_add_and_fetch(unsigned int *v, unsigned int i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned int uint_sub_and_fetch(unsigned int *v, unsigned int i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned int uint_and_and_fetch(unsigned int *v, unsigned int i) {
    return __atomic_and_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned int uint_or_and_fetch(unsigned int *v, unsigned int i) {
    return __atomic_or_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned int uint_xor_and_fetch(unsigned int *v, unsigned int i) {
    return __atomic_xor_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned int uint_nand_and_fetch(unsigned int *v, unsigned int i) {
    return __atomic_nand_fetch(v, i, __ATOMIC_SEQ_CST);
};

unsigned int uint_fetch_and_add(unsigned int *v, unsigned int i) {
    return __atomic_fetch_add(v, i, __ATOMIC_SEQ_CST);
};
unsigned int uint_fetch_and_sub(unsigned int *v, unsigned int i) {
    return __atomic_fetch_sub(v, i, __ATOMIC_SEQ_CST);
};
unsigned int uint_fetch_and_and(unsigned int *v, unsigned int i) {
    return __atomic_fetch_and(v, i, __ATOMIC_SEQ_CST);
};
unsigned int uint_fetch_and_or(unsigned int *v, unsigned int i) {
    return __atomic_fetch_or(v, i, __ATOMIC_SEQ_CST);
};
unsigned int uint_fetch_and_xor(unsigned int *v, unsigned int i) {
    return __atomic_fetch_xor(v, i, __ATOMIC_SEQ_CST);
};
unsigned int uint_fetch_and_nand(unsigned int *v, unsigned int i) {
    return __atomic_fetch_nand(v, i, __ATOMIC_SEQ_CST);
};

long long_load(long *ptr){
    return __atomic_load_n(ptr, __ATOMIC_SEQ_CST);
};
void long_store(long *v, long *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
void long_shift(long *v, long *n, long* r) {
    return __atomic_exchange(v, n, r,__ATOMIC_SEQ_CST);
};
long long_get_and_set(long *v, long n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool long_compare_and_set(long *v, long *e, long n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

long long_add_and_fetch(long *v, long i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
long long_sub_and_fetch(long *v, long i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
long long_and_and_fetch(long *v, long i) {
    return __atomic_and_fetch(v, i, __ATOMIC_SEQ_CST);
};
long long_or_and_fetch(long *v, long i) {
    return __atomic_or_fetch(v, i, __ATOMIC_SEQ_CST);
};
long long_xor_and_fetch(long *v, long i) {
    return __atomic_xor_fetch(v, i, __ATOMIC_SEQ_CST);
};
long long_nand_and_fetch(long *v, long i) {
    return __atomic_nand_fetch(v, i, __ATOMIC_SEQ_CST);
};

long long_fetch_and_add(long *v, long i) {
    return __atomic_fetch_add(v, i, __ATOMIC_SEQ_CST);
};
long long_fetch_and_sub(long *v, long i) {
    return __atomic_fetch_sub(v, i, __ATOMIC_SEQ_CST);
};
long long_fetch_and_and(long *v, long i) {
    return __atomic_fetch_and(v, i, __ATOMIC_SEQ_CST);
};
long long_fetch_and_or(long *v, long i) {
    return __atomic_fetch_or(v, i, __ATOMIC_SEQ_CST);
};
long long_fetch_and_xor(long *v, long i) {
    return __atomic_fetch_xor(v, i, __ATOMIC_SEQ_CST);
};
long long_fetch_and_nand(long *v, long i) {
    return __atomic_fetch_nand(v, i, __ATOMIC_SEQ_CST);
};


unsigned long ulong_load(unsigned long *ptr){
    return __atomic_load_n(ptr, __ATOMIC_SEQ_CST);
};
void ulong_store(unsigned long *v, unsigned long *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
void ulong_shift(unsigned long *v, unsigned long *n, unsigned long* r) {
    return __atomic_exchange(v, n, r,__ATOMIC_SEQ_CST);
};
unsigned long ulong_get_and_set(unsigned long *v, unsigned long n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool ulong_compare_and_set(unsigned long *v, unsigned long *e, unsigned long n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

unsigned long ulong_add_and_fetch(unsigned long *v, unsigned long i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned long ulong_sub_and_fetch(unsigned long *v, unsigned long i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned long ulong_and_and_fetch(unsigned long *v, unsigned long i) {
    return __atomic_and_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned long ulong_or_and_fetch(unsigned long *v, unsigned long i) {
    return __atomic_or_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned long ulong_xor_and_fetch(unsigned long *v, unsigned long i) {
    return __atomic_xor_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned long ulong_nand_and_fetch(unsigned long *v, unsigned long i) {
    return __atomic_nand_fetch(v, i, __ATOMIC_SEQ_CST);
};

unsigned long ulong_fetch_and_add(unsigned long *v, unsigned long i) {
    return __atomic_fetch_add(v, i, __ATOMIC_SEQ_CST);
};
unsigned long ulong_fetch_and_sub(unsigned long *v, unsigned long i) {
    return __atomic_fetch_sub(v, i, __ATOMIC_SEQ_CST);
};
unsigned long ulong_fetch_and_and(unsigned long *v, unsigned long i) {
    return __atomic_fetch_and(v, i, __ATOMIC_SEQ_CST);
};
unsigned long ulong_fetch_and_or(unsigned long *v, unsigned long i) {
    return __atomic_fetch_or(v, i, __ATOMIC_SEQ_CST);
};
unsigned long ulong_fetch_and_xor(unsigned long *v, unsigned long i) {
    return __atomic_fetch_xor(v, i, __ATOMIC_SEQ_CST);
};
unsigned long ulong_fetch_and_nand(unsigned long *v, unsigned long i) {
    return __atomic_fetch_nand(v, i, __ATOMIC_SEQ_CST);
};

size_t size_t_load(size_t *ptr){
    return __atomic_load_n(ptr, __ATOMIC_SEQ_CST);
};
void size_t_store(size_t *v, size_t *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
void size_t_shift(size_t *v, size_t *n, size_t* r) {
    return __atomic_exchange(v, n, r,__ATOMIC_SEQ_CST);
};
size_t size_t_get_and_set(size_t *v, size_t n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool size_t_compare_and_set(size_t *v, size_t *e, size_t n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

size_t size_t_add_and_fetch(size_t *v, size_t i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
size_t size_t_sub_and_fetch(size_t *v, size_t i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
size_t size_t_and_and_fetch(size_t *v, size_t i) {
    return __atomic_and_fetch(v, i, __ATOMIC_SEQ_CST);
};
size_t size_t_or_and_fetch(size_t *v, size_t i) {
    return __atomic_or_fetch(v, i, __ATOMIC_SEQ_CST);
};
size_t size_t_xor_and_fetch(size_t *v, size_t i) {
    return __atomic_xor_fetch(v, i, __ATOMIC_SEQ_CST);
};
size_t size_t_nand_and_fetch(size_t *v, size_t i) {
    return __atomic_nand_fetch(v, i, __ATOMIC_SEQ_CST);
};

size_t size_t_fetch_and_add(size_t *v, size_t i) {
    return __atomic_fetch_add(v, i, __ATOMIC_SEQ_CST);
};
size_t size_t_fetch_and_sub(size_t *v, size_t i) {
    return __atomic_fetch_sub(v, i, __ATOMIC_SEQ_CST);
};
size_t size_t_fetch_and_and(size_t *v, size_t i) {
    return __atomic_fetch_and(v, i, __ATOMIC_SEQ_CST);
};
size_t size_t_fetch_and_or(size_t *v, size_t i) {
    return __atomic_fetch_or(v, i, __ATOMIC_SEQ_CST);
};
size_t size_t_fetch_and_xor(size_t *v, size_t i) {
    return __atomic_fetch_xor(v, i, __ATOMIC_SEQ_CST);
};
size_t size_t_fetch_and_nand(size_t *v, size_t i) {
    return __atomic_fetch_nand(v, i, __ATOMIC_SEQ_CST);
};

ssize_t ssize_t_load(ssize_t *ptr){
    return __atomic_load_n(ptr, __ATOMIC_SEQ_CST);
};

void ssize_t_store(ssize_t *v, ssize_t *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
void ssize_t_shift(ssize_t *v, ssize_t *n, ssize_t* r) {
    return __atomic_exchange(v, n, r,__ATOMIC_SEQ_CST);
};
ssize_t ssize_t_get_and_set(ssize_t *v, ssize_t n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool ssize_t_compare_and_set(ssize_t *v, ssize_t *e, ssize_t n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

ssize_t ssize_t_add_and_fetch(ssize_t *v, ssize_t i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
ssize_t ssize_t_sub_and_fetch(ssize_t *v, ssize_t i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
ssize_t ssize_t_and_and_fetch(ssize_t *v, ssize_t i) {
    return __atomic_and_fetch(v, i, __ATOMIC_SEQ_CST);
};
ssize_t ssize_t_or_and_fetch(ssize_t *v, ssize_t i) {
    return __atomic_or_fetch(v, i, __ATOMIC_SEQ_CST);
};
ssize_t ssize_t_xor_and_fetch(ssize_t *v, ssize_t i) {
    return __atomic_xor_fetch(v, i, __ATOMIC_SEQ_CST);
};
ssize_t ssize_t_nand_and_fetch(ssize_t *v, ssize_t i) {
    return __atomic_nand_fetch(v, i, __ATOMIC_SEQ_CST);
};

ssize_t ssize_t_fetch_and_add(ssize_t *v, ssize_t i) {
    return __atomic_fetch_add(v, i, __ATOMIC_SEQ_CST);
};
ssize_t ssize_t_fetch_and_sub(ssize_t *v, ssize_t i) {
    return __atomic_fetch_sub(v, i, __ATOMIC_SEQ_CST);
};
ssize_t ssize_t_fetch_and_and(ssize_t *v, ssize_t i) {
    return __atomic_fetch_and(v, i, __ATOMIC_SEQ_CST);
};
ssize_t ssize_t_fetch_and_or(ssize_t *v, ssize_t i) {
    return __atomic_fetch_or(v, i, __ATOMIC_SEQ_CST);
};
ssize_t ssize_t_fetch_and_xor(ssize_t *v, ssize_t i) {
    return __atomic_fetch_xor(v, i, __ATOMIC_SEQ_CST);
};
ssize_t ssize_t_fetch_and_nand(ssize_t *v, ssize_t i) {
    return __atomic_fetch_nand(v, i, __ATOMIC_SEQ_CST);
};

long long longlong_load(long long *ptr){
    return __atomic_load_n(ptr, __ATOMIC_SEQ_CST);
};
void longlong_store(long long *v, long long *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
void longlong_shift(long long *v, long long *n, long long* r) {
    return __atomic_exchange(v, n, r,__ATOMIC_SEQ_CST);
};
long long longlong_get_and_set(long long *v, long long n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool longlong_compare_and_set(long long *v, long long *e, long long n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

long long longlong_add_and_fetch(long long *v, long long i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
long long longlong_sub_and_fetch(long long *v, long long i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
long long longlong_and_and_fetch(long long *v, long long i) {
    return __atomic_and_fetch(v, i, __ATOMIC_SEQ_CST);
};
long long longlong_or_and_fetch(long long *v, long long i) {
    return __atomic_or_fetch(v, i, __ATOMIC_SEQ_CST);
};
long long longlong_xor_and_fetch(long long *v, long long i) {
    return __atomic_xor_fetch(v, i, __ATOMIC_SEQ_CST);
};
long long longlong_nand_and_fetch(long long *v, long long i) {
    return __atomic_nand_fetch(v, i, __ATOMIC_SEQ_CST);
};

long long longlong_fetch_and_add(long long *v, long long i) {
    return __atomic_fetch_add(v, i, __ATOMIC_SEQ_CST);
};
long long longlong_fetch_and_sub(long long *v, long long i) {
    return __atomic_fetch_sub(v, i, __ATOMIC_SEQ_CST);
};
long long longlong_fetch_and_and(long long *v, long long i) {
    return __atomic_fetch_and(v, i, __ATOMIC_SEQ_CST);
};
long long longlong_fetch_and_or(long long *v, long long i) {
    return __atomic_fetch_or(v, i, __ATOMIC_SEQ_CST);
};
long long longlong_fetch_and_xor(long long *v, long long i) {
    return __atomic_fetch_xor(v, i, __ATOMIC_SEQ_CST);
};
long long longlong_fetch_and_nand(long long *v, long long i) {
    return __atomic_fetch_nand(v, i, __ATOMIC_SEQ_CST);
};

unsigned long long ulonglong_load(unsigned long long *ptr){
    return __atomic_load_n(ptr, __ATOMIC_SEQ_CST);
};
void ulonglong_store(unsigned long long *v, unsigned long long *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};
void ulonglong_shift(unsigned long long *v, unsigned long long *n, unsigned long long* r) {
    return __atomic_exchange(v, n, r,__ATOMIC_SEQ_CST);
};
unsigned long long ulonglong_get_and_set(unsigned long long *v, unsigned long long n) {
    return __atomic_exchange_n(v, n, __ATOMIC_SEQ_CST);
};
_Bool ulonglong_compare_and_set(unsigned long long *v, unsigned long long *e, unsigned long long n) {
    return __atomic_compare_exchange_n(v, e, n, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
};

unsigned long long ulonglong_add_and_fetch(unsigned long long *v, unsigned long long i) {
    return __atomic_add_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned long long ulonglong_sub_and_fetch(unsigned long long *v, unsigned long long i) {
    return __atomic_sub_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned long long ulonglong_and_and_fetch(unsigned long long *v, unsigned long long i) {
    return __atomic_and_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned long long ulonglong_or_and_fetch(unsigned long long *v, unsigned long long i) {
    return __atomic_or_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned long long ulonglong_xor_and_fetch(unsigned long long *v, unsigned long long i) {
    return __atomic_xor_fetch(v, i, __ATOMIC_SEQ_CST);
};
unsigned long long ulonglong_nand_and_fetch(unsigned long long *v, unsigned long long i) {
    return __atomic_nand_fetch(v, i, __ATOMIC_SEQ_CST);
};

unsigned long long ulonglong_fetch_and_add(unsigned long long *v, unsigned long long i) {
    return __atomic_fetch_add(v, i, __ATOMIC_SEQ_CST);
};
unsigned long long ulonglong_fetch_and_sub(unsigned long long *v, unsigned long long i) {
    return __atomic_fetch_sub(v, i, __ATOMIC_SEQ_CST);
};
unsigned long long ulonglong_fetch_and_and(unsigned long long *v, unsigned long long i) {
    return __atomic_fetch_and(v, i, __ATOMIC_SEQ_CST);
};
unsigned long long ulonglong_fetch_and_or(unsigned long long *v, unsigned long long i) {
    return __atomic_fetch_or(v, i, __ATOMIC_SEQ_CST);
};
unsigned long long ulonglong_fetch_and_xor(unsigned long long *v, unsigned long long i) {
    return __atomic_fetch_xor(v, i, __ATOMIC_SEQ_CST);
};
unsigned long long ulonglong_fetch_and_nand(unsigned long long *v, unsigned long long i) {
    return __atomic_fetch_nand(v, i, __ATOMIC_SEQ_CST);
};

void float_store(float *v, float *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};


void double_store(double *v, double *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};


void longdouble_store(long double *v, long double *n) {
    __atomic_store(v, n, __ATOMIC_SEQ_CST);
};



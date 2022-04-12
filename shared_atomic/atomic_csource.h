
void bool_store(_Bool *, _Bool *);
_Bool bool_add_and_fetch(_Bool *, _Bool);
_Bool bool_sub_and_fetch(_Bool *, _Bool);
_Bool bool_get_and_set(_Bool *, _Bool);
_Bool bool_compare_and_set(_Bool *, _Bool *, _Bool);

void byte_store(char *, char *);
char byte_add_and_fetch(char *, char);
char byte_sub_and_fetch(char *, char);
char byte_get_and_set(char *, char);
_Bool byte_compare_and_set(char *, char *, char);

void ubyte_store(unsigned char *, unsigned char *);
unsigned char ubyte_add_and_fetch(unsigned char *, unsigned char);
unsigned char ubyte_sub_and_fetch(unsigned char *, unsigned char);
unsigned char ubyte_get_and_set(unsigned char *, unsigned char);
_Bool ubyte_compare_and_set(unsigned char *, unsigned char *, unsigned char);

void short_store(short *, short *);
short short_add_and_fetch(short *, short);
short short_sub_and_fetch(short *, short);
short short_get_and_set(short *, short);
_Bool short_compare_and_set(short *, short *, short);

void ushort_store(unsigned short *, unsigned short *);
unsigned short ushort_add_and_fetch(unsigned short *, unsigned short);
unsigned short ushort_sub_and_fetch(unsigned short *, unsigned short);
unsigned short ushort_get_and_set(unsigned short *, unsigned short);
_Bool ushort_compare_and_set(unsigned short *, unsigned short *, unsigned short);

void int_store(int *, int *);
int int_add_and_fetch(int *, int);
int int_sub_and_fetch(int *, int);
int int_get_and_set(int *, int);
_Bool int_compare_and_set(int *, int *, int);

void uint_store(unsigned int *, unsigned int *);
unsigned int uint_add_and_fetch(unsigned int *, unsigned int);
unsigned int uint_sub_and_fetch(unsigned int *, unsigned int);
unsigned int uint_get_and_set(unsigned int *, unsigned int);
_Bool uint_compare_and_set(unsigned int *, unsigned int *, unsigned int);


void wchar_store(wchar_t *, wchar_t *);
wchar_t wchar_add_and_fetch(wchar_t *, wchar_t);
wchar_t wchar_sub_and_fetch(wchar_t *, wchar_t);
wchar_t wchar_get_and_set(wchar_t *, wchar_t);
_Bool wchar_compare_and_set(wchar_t *, wchar_t *, wchar_t);


void long_store(long *, long *);
long long_add_and_fetch(long *, long);
long long_sub_and_fetch(long *, long);
long long_get_and_set(long *, long);
_Bool long_compare_and_set(long *, long *, long);

void ulong_store(unsigned long *, unsigned long *);
unsigned long ulong_add_and_fetch(unsigned long *, unsigned long);
unsigned long ulong_sub_and_fetch(unsigned long *, unsigned long);
unsigned long ulong_get_and_set(unsigned long *, unsigned long);
_Bool ulong_compare_and_set(unsigned long *, unsigned long *, unsigned long);

void size_t_store(size_t *, size_t *);
size_t size_t_add_and_fetch(size_t *, size_t);
size_t size_t_sub_and_fetch(size_t *, size_t);
size_t size_t_get_and_set(size_t *, size_t);
_Bool size_t_compare_and_set(size_t *, size_t *, size_t);

void ssize_t_store(ssize_t *, ssize_t *);
ssize_t ssize_t_add_and_fetch(ssize_t *, ssize_t);
ssize_t ssize_t_sub_and_fetch(ssize_t *, ssize_t);
ssize_t ssize_t_get_and_set(ssize_t *, ssize_t);
_Bool ssize_t_compare_and_set(ssize_t *, ssize_t *, ssize_t);

void longlong_store(long long *, long long *);
long long longlong_add_and_fetch(long long *, long long);
long long longlong_sub_and_fetch(long long *, long long);
long long longlong_get_and_set(long long *, long long);
_Bool longlong_compare_and_set(long long *, long long *, long long);

void ulonglong_store(unsigned long long *, unsigned long long *);
unsigned long long ulonglong_add_and_fetch(unsigned long long *, unsigned long long);
unsigned long long ulonglong_sub_and_fetch(unsigned long long *, unsigned long long);
unsigned long long ulonglong_get_and_set(unsigned long long *, unsigned long long);
_Bool ulonglong_compare_and_set(unsigned long long *, unsigned long long *, unsigned long long);

void float_store(float *v, float *n);
/*float float_add_and_fetch(float *v, float i);
float float_sub_and_fetch(float *v, float i);
float float_get_and_set(float *v, float n);
_Bool float_compare_and_set(float *v, float *e, float n);*/

void double_store(double *v, double *n);
/*double double_add_and_fetch(double *v, double i);
double double_sub_and_fetch(double *v, double i);
double double_get_and_set(double *v, double n);
_Bool double_compare_and_set(double *v, double *e, double n);*/


void longdouble_store(long double *v, long double *n);
/*long double longdouble_add_and_fetch(long double *v, long double i);
long double longdouble_sub_and_fetch(long double *v, long double i);
long double longdouble_get_and_set(long double *v, long double n);
_Bool longdouble_compare_and_set(long double *v, long double *e, long double n);*/

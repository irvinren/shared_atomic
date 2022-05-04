'''
Created on 28 Mar 2022

@author: philren
'''

import sys
import subprocess
import re
import os
from pathlib import Path
import cffi


ffi = cffi.FFI()

hfilepath = Path.joinpath(Path(__file__).parent, 'atomic_csource.h')
cfilepath = Path.joinpath(Path(__file__).parent, 'atomic_csource.c')

if sys.platform == 'linux':
    header = \
'typedef long int off_t;\
#define PROT_READ       0x1             /* page can be read */\
#define PROT_WRITE      0x2             /* page can be written */\
#define PROT_EXEC       0x4             /* page can be executed */\
#define PROT_SEM        0x8             /* page may be used for atomic ops */\
#define PROT_NONE       0x0             /* page can not be accessed */\
#define PROT_GROWSDOWN  0x01000000      /* mprotect flag: extend change to start of growsdown vma */\
#define PROT_GROWSUP    0x02000000      /* mprotect flag: extend change to end of growsup vma */\
\
#define MAP_SHARED      0x01            /* Share changes */\
#define MAP_PRIVATE     0x02            /* Changes are private */\
#define MAP_SHARED_VALIDATE 0x03        /* share + validate extension flags */\
#define MAP_TYPE        0x0f            /* Mask for type of mapping */\
#define MAP_FIXED       0x10            /* Interpret addr exactly */\
#define MAP_ANONYMOUS   0x20            /* don\'t use a file */'

elif sys.platform == 'darwin':
    header = 'typedef long long off_t;\n'

with hfilepath.open() as hfile:
        header += ''.join(hfile.readlines())

ffi.cdef(header)

if sys.platform in('darwin','linux'):
    result = subprocess.run('gcc -x c -v -E /dev/null'.split(),
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)

    result = bytes.decode(result.stderr).split("\n")

    start = result.index('#include <...> search starts here:')
    end = result.index('End of search list.')

    result_include = ["-I" + re.sub(r" *\(framework directory\)$", "", i).strip() for i in result[start + 1:end]]
else:
    result_include = ""

result_link = result_include + ["-latomic"] if sys.platform == 'linux' else result_include

ffi.set_source('shared_atomic_', """
    #include <stddef.h>
    #include <sys/types.h>
    """ + header,
               sources=[str(cfilepath)],
               extra_compile_args=result_include,
               extra_link_args=result_link,
               libraries=['c'])


def main():

    ffi.compile(verbose=True)

if __name__ == "__main__":
    main()

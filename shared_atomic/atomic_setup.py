'''
Created on 28 Mar 2022

@author: philren
'''

import cffi
import os
import sys
import subprocess
import re
from pathlib import Path

ffi = cffi.FFI()
path = Path

hfilepath = Path.joinpath(Path(__file__).parent, 'atomic_csource.h')
cfilepath = Path.joinpath(Path(__file__).parent, 'atomic_csource.c')

with hfilepath.open() as hfile:
        header = ''.join(hfile.readlines())
    
ffi.cdef(header)

if sys.platform in ('darwin','linux'):

    result = subprocess.run('gcc -x c -v -E /dev/null'.split(),
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)

    result = bytes.decode(result.stderr).split("\n")

    start = result.index('#include <...> search starts here:')
    end = result.index('End of search list.')

    result_include = ["-I" + re.sub(r" *\(framework directory\)$", "", i).strip() for i in result[start + 1:end]]

    ffi.set_source('shared_atomic', """
    #include <stddef.h>
    #include <sys/types.h>"""+header,
    sources=[str(cfilepath)],
    extra_compile_args=result_include,
    extra_link_args=result_include
    )
elif sys.platform == 'win32':

    result = subprocess.run('gcc -x c -v -E /dev/null'.split(),
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)

    result = bytes.decode(result.stderr).split("\n")

    start = result.index('#include <...> search starts here:')
    end = result.index('End of search list.')

    result_include = ["-I" + re.sub(r" *\(framework directory\)$", "", i).strip() for i in result[start + 1:end]]

    ffi.set_source('shared_atomic', """
    #include <stddef.h>
    #include <sys/types.h>
    #include """ + header,
    sources=[str(Path.joinpath(Path('shared_atomic'),'atomic_csource.c'))],
    extra_compile_args=result_include,
    extra_link_args=result_include
    )

def main():

    ffi.compile(verbose=True)

if __name__ == "__main__":
    main()

'''
Created on 28 Mar 2022

@author: philren
'''

import cffi
import os
import subprocess
import re

ffi = cffi.FFI()
with open(os.getcwd() + "/shared_atomic/atomic_csource.h", "r") as hfile:
        header = ''.join(hfile.readlines())
    
ffi.cdef(header)
    
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
#include \"""" + os.getcwd() + "/shared_atomic/atomic_csource.h\"",
sources=['shared_atomic/atomic_csource.c'],
extra_compile_args=result_include,
extra_link_args=result_include
)


def main():
    ffi.compile(verbose=True)

if __name__ == "__main__":
    main()

'''
Created on 28 Mar 2022

@author: philren
'''

import sys
import subprocess
import re
from pathlib import Path
import cffi


ffi = cffi.FFI()

hfilepath = Path.joinpath(Path(__file__).parent, 'atomic_csource.h')
cfilepath = Path.joinpath(Path(__file__).parent, 'atomic_csource.c')

with hfilepath.open() as hfile:
        header = ''.join(hfile.readlines())
    
ffi.cdef(header)

result = subprocess.run('gcc -x c -v -E /dev/null'.split(),
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)

result = bytes.decode(result.stderr).split("\n")

start = result.index('#include <...> search starts here:')
end = result.index('End of search list.')

result_include = ["-I" + re.sub(r" *\(framework directory\)$", "", i).strip() for i in result[start + 1:end]]

result_link = result_include + "-latomic" if sys.platform == 'linux' else result_include

ffi.set_source('shared_atomic', """
    #include <stddef.h>
    #include <sys/types.h>""" + header,
               sources=[str(cfilepath)],
               extra_compile_args=result_include,
               extra_link_args=result_link)


def main():

    ffi.compile(verbose=True)

if __name__ == "__main__":
    main()

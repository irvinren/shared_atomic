import sys
import sysconfig
from distutils.core import setup as distutils_setup
from setuptools import setup as setuptools_setup
from shared_atomic import atomic_setup

__version__="2.0.5"
__package_name__='shared_atomic'
__author__="Xiquan Ren"
__author_email__="xiquanren@yandex.com"
__description__="Shared atomicity with multiprocessing/multithreads shared ctypes"
__url__='https://github.com/irvinren/shared_atomic.git'
__packages__=['shared_atomic']

with open("readme.rst") as f:
    readme = f.read()

if sys.platform in('darwin','linux'):
    distutils_setup(
        name=__package_name__,
        version=__version__,
        author=__author__,
        author_email=__author_email__,
        description=__description__,
        url=__url__,
        long_description=readme,
        ext_modules=[atomic_setup.ffi.distutils_extension()],
        #cffi_modules=["shared_atomic/atomic_setup.py:ffi"],
        packages=__packages__,
        data_files=[('shared_atomic',['shared_atomic/atomic_csource.c',
                                        'shared_atomic/atomic_csource.h']),
                    ('', ['readme.rst','LICENSE'])]
    )
elif sys.platform == 'win32':
    if sysconfig.get_config_var('implementation') == 'PyPy':
        raise NotImplementedError('PyPy is not supported on Windows Platform!')
    setuptools_setup(
        name=__package_name__,
        version=__version__,
        author=__author__,
        author_email=__author_email__,
        description=__description__,
        url=__url__,
        long_description=readme,
        packages=__packages__,
        python_requires=">=3.0",
        install_requires=[
            'cppyy ==2.3.1',
        ],
		include_package_data=True
    )

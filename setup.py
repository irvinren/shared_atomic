import sys
from distutils.core import setup as distutils_setup
from setuptools import setup as setuptools_setup
from shared_atomic import atomic_setup


with open("readme.rst") as f:
    readme = f.read()

if sys.platform in('darwin','linux'):
    distutils_setup(
        name='shared_atomic',
        version="2.0.0",
        author="Xiquan Ren",
        author_email="xiquanren@yandex.com",
        description="Shared atomicity with multiprocessing/multithreads shared ctypes",
        url='https://github.com/irvinren/shared_atomic.git',
        long_description=readme,
        ext_modules=[atomic_setup.ffi.distutils_extension()],
        packages=['shared_atomic'],
        data_files=[('shared_atomic',['shared_atomic/atomic_csource.c',
                                        'shared_atomic/atomic_csource.h']),
                    ('', ['readme.rst','LICENSE'])]
    )
elif sys.platform == 'win32':
    setuptools_setup(
        name='shared_atomic',
        version="2.0.0",
        author="Xiquan Ren",
        author_email="xiquanren@yandex.com",
        description="Shared atomicity with multiprocessing/multithreads shared ctypes",
        packages=['shared_atomic'],
        python_requires=">=3.0",
        install_requires=[
            'cppyy ==2.3.1',
        ],
		include_package_data=True
    )

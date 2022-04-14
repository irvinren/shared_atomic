from distutils.core import setup
from shared_atomic import atomic_setup

with open("readme.rst") as f:
    readme = f.read()

setup(
    name='shared_atomic',
    version="1.0.20",
    author="Xiquan Ren",
    author_email="xiquanren@yandex.com",
    description="Shared atomicity with multiprocessing shared ctypes",
    url='https://github.com/irvinren/shared_atomic.git',
    long_description=readme,
    ext_modules=[atomic_setup.ffi.distutils_extension()],
    packages=['shared_atomic'],
    data_files=[('shared_atomic',['shared_atomic/atomic_csource.c',
                                    'shared_atomic/atomic_csource.h']),
                ('', ['readme.rst','LICENSE'])]
)


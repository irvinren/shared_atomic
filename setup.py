from distutils.core import setup
from shared_atomic import atomic_setup


with open("readme.rst") as f:
    readme = f.read()

setup(
    name='shared_atomic',
    version="1.0.10",
    author="Xiquan Ren",
    author_email="xiquanren@yandex.com",
    description="Shared atomicity with multiprocessing shared ctypes",
    long_description=readme,
    ext_modules=[atomic_setup.ffi.distutils_extension()],
    packages=['shared_atomic']
)


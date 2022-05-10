import sys
import sysconfig
from setuptools import setup

__version__="2.1.6"
__package_name__='shared_atomic'
__author__="Xiquan Ren"
__author_email__="xiquanren@yandex.com"
__description__="Shared atomicity for multiprocessing/multiple threads"
__url__='https://github.com/irvinren/shared_atomic.git'
__packages__=['shared_atomic']

with open("readme.rst") as f:
    readme = f.read()

if sys.platform in('darwin','linux'):

    setup(
        name=__package_name__,
        version=__version__,
        author=__author__,
        author_email=__author_email__,
        description=__description__,
        url=__url__,
        long_description=readme,
        packages=__packages__,
        python_requires=">=3.0",
        cffi_modules=["shared_atomic/atomic_setup.py:ffi"],
        install_requires=[
            'cffi>=1.0',
        ],
        zip_safe=False
    )
elif sys.platform == 'win32':

    if sysconfig.get_config_var('implementation') == 'PyPy':
        raise NotImplementedError('PyPy is not supported on Windows Platform!')

    setup(
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
            'cppyy >=1.5.0,<=2.3.1',
        ],
        include_package_data=True,
    )



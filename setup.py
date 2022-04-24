import sys
import os
import subprocess
from distutils.core import setup as distutils_setup
from setuptools import setup as setuptools_setup
from shared_atomic import atomic_setup


__version__="2.0.0"
__package_name__='shared_atomic'
__author__="Xiquan Ren"
__author_email__="xiquanren@yandex.com"
__description__="Shared atomicity with multiprocessing/multithreads shared ctypes"
__url__='https://github.com/irvinren/shared_atomic.git'
__packages__=['shared_atomic']

with open("readme.rst") as f:
    __readme__ = f.read()

if sys.platform in('linux'):
    distutils_setup(
        name=__package_name__,
        version=__version__,
        author=__author__,
        author_email=__author_email__,
        description=__description__,
        url=__url__,
        long_description=__readme__,
        ext_modules=[atomic_setup.ffi.distutils_extension()],
        packages=__packages__,
        data_files=[('shared_atomic',['shared_atomic/atomic_csource.c',
                                        'shared_atomic/atomic_csource.h']),
                    ('', ['readme.rst','LICENSE'])]
    )
if sys.platform == 'darwin':

    from setuptools import Extension
    from setuptools.command.build_ext import build_ext

    PLAT_TO_CMAKE = {
        "win32": "Win32",
        "win-amd64": "x64",
    }


    # A CMakeExtension needs a sourcedir instead of a file list.
    # The name must be the _single_ output extension from the CMake build.
    # If you need multiple extensions, see scikit-build.
    class CMakeExtension(Extension):
        def __init__(self, name, sourcedir=""):
            Extension.__init__(self, name, sources=[])
            self.sourcedir = os.path.abspath(sourcedir)


    class CMakeBuild(build_ext):
        def build_extension(self, ext):
            extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))

            # required for auto-detection & inclusion of auxiliary "native" libs
            if not extdir.endswith(os.path.sep):
                extdir += os.path.sep

            debug = int(os.environ.get("DEBUG", 0)) if self.debug is None else self.debug
            cfg = "Debug" if debug else "Release"

            # CMake lets you override the generator - we need to check this.
            # Can be set with Conda-Build, for example.
            cmake_generator = os.environ.get("CMAKE_GENERATOR", "")

            # Set Python_EXECUTABLE instead if you use PYBIND11_FINDPYTHON
            # EXAMPLE_VERSION_INFO shows you how to pass a value into the C++ code
            # from Python.
            cmake_args = [
                f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}",
                f"-DPYTHON_EXECUTABLE={sys.executable}",
                f"-DCMAKE_BUILD_TYPE={cfg}",  # not used on MSVC, but no harm
            ]
            build_args = []
            # Adding CMake arguments set as environment variable
            # (needed e.g. to build for ARM OSx on conda-forge)
            if "CMAKE_ARGS" in os.environ:
                #enviroments
                cmake_args += [item for item in os.environ["CMAKE_ARGS"].split(" ") if item]

                #platform
                cmake_args += ["-A", PLAT_TO_CMAKE[self.plat_name]]

                #outputdirectory
                cmake_args += [
                        f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{cfg.upper()}={extdir}"
                    ]
                build_args += ["--config", cfg]

            # Set CMAKE_BUILD_PARALLEL_LEVEL to control the parallel build level
            # across all generators.
            if "CMAKE_BUILD_PARALLEL_LEVEL" not in os.environ:
                # self.parallel is a Python 3 only way to set parallel jobs by hand
                # using -j in the build_ext call, not supported by pip or PyPA-build.
                if hasattr(self, "parallel") and self.parallel:
                    # CMake 3.12+ only.
                    build_args += [f"-j{self.parallel}"]

            build_temp = os.path.join(self.build_temp, ext.name)
            if not os.path.exists(build_temp):
                os.makedirs(build_temp)
            print(build_args, build_temp, ext.sourcedir)
            try:
                result = subprocess.run(["cmake", ext.sourcedir] + cmake_args,
                                      check=True,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.STDOUT,
                                      encoding=sys.getdefaultencoding(),
                                      cwd=build_temp)
                print(result.stdout)
                result = subprocess.run(["cmake", "--build", "."] + build_args,
                                   check=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   encoding=sys.getdefaultencoding(),
                                   cwd=ext.sourcedir)
                print(result.stdout)
            except subprocess.CalledProcessError as e:
                print(e.stdout)
                raise e

    setuptools_setup(
        name=__package_name__,
        version=__version__,
        author=__author__,
        author_email=__author_email__,
        description=__description__,
        packages=__packages__,
        ext_modules=[CMakeExtension("shared_atomic")
        ],
        cmdclass={"build_ext": CMakeBuild},
        python_requires=">=3.0",
        #install_requires=['cppyy ==2.3.1',],
        install_requires=['pybind11==2.9.2',],
        include_package_data=True,
    )




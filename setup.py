# Copyright 2023 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import glob

from setuptools import setup
from setuptools import Extension
from Cython.Build import cythonize
from setuptools.command.build_ext import build_ext

import numpy

class build_ext_with_args(build_ext):
    """Add compiler-specific compile/link flags."""

    extra_compile_args = {
        'msvc': ['/std:c++20'],
        'unix': ['-std=c++20', '-fopenmp'],
    }

    extra_link_args = {
        'msvc': ['/std:c++20'],
        'unix': ['-std=c++20', '-fopenmp'],
    }

    def build_extensions(self):
        compiler = self.compiler.compiler_type

        compile_args = self.extra_compile_args[compiler]
        for ext in self.extensions:
            ext.extra_compile_args = compile_args

        link_args = self.extra_link_args[compiler]
        for ext in self.extensions:
            ext.extra_compile_args = link_args

        super().build_extensions()


setup(
    cmdclass={'build_ext': build_ext_with_args},
    ext_modules=cythonize(
        [Extension('py_cpp_extension.cyutils',
                   sources=["py_cpp_extension/cyutils.pyx",
                            *glob.glob("py_cpp_extension/src/**/*.cpp", recursive=True)]),
         ],
        annotate=True,
        language_level=3,
        ),
    include_dirs=[
        numpy.get_include(),
        "py_cpp_extension/include/"
        ],
    # libraries=[library],
    )
# distutils: language = c++
# cython: language_level=3
# cython: linetrace=True

cimport cython
from py_cpp_extension.libcpp.cyutils cimport print_integer
from py_cpp_extension.libcpp.cyutils cimport openmp_test



__all__ = ["cyprint"]


def cyprint(n: int):

    cdef int _num = n

    with nogil:
        print_integer(_num)


def cyopenmp():

    with nogil:
        openmp_test()

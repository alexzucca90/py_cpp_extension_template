# distutils: language = c++
# cython: language_level=3
# cython: linetrace=True


cdef extern from "cpp_header.hpp" nogil:
    void print_integer(int n)
    void openmp_test()
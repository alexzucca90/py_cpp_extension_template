#include "cpp_header.hpp"
#include <omp.h>

void print_integer(int n){
    std::cout << "integer passed " << n << "\n";
}

void openmp_test(){
    std::cout << "Hello from process " << omp_get_thread_num() << "\n";
}
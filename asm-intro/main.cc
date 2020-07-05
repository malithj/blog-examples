#include <iostream>
#include <stdint.h>

extern "C" uint64_t inc_func(uint64_t x);

int main(int argc, char** argv) {
  for (uint64_t i = 0; i < 10; ++i) {
    std::cout << "iteration: " << i << " inc value: " << inc_func(i) << std::endl;
  }
  return 0;
}

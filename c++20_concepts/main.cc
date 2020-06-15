#include <stdio.h>

#include "buffer.h"
#include "non_trivial_type.h"

int main() {
  Buffer<ComplexType> buffer;
  ComplexType *ptr = buffer.allocate(10);
  std::free(ptr);
  return 0;
}

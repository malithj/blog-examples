#ifndef __BUFFER_H__
#define __BUFFER_H__

#include <memory>
#include <type_traits>

template <typename T> 
    requires (std::is_trivial<T>::value)
class Buffer {
  public:
    Buffer() = default;        // default constructor
    T* allocate(size_t size);  // allocate memory and ret ptr
    ~Buffer() = default;       // default destructor
};

// need to redeclare constraints
// otherwise the compiler throws 
// "clause differs in template redeclaration"
template <typename T>
    requires (std::is_trivial<T>::value)
T* Buffer<T>::allocate(size_t size) {
    T* ptr = static_cast<T*>(std::malloc(sizeof(T) * size));
    return ptr;
};

#endif

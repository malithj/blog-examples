#ifndef __NON_TRIIVAL_TYPE_H__
#define __NON_TRIIVAL_TYPE_H__

class ComplexType {
  private:
    uint64_t imaginary_part = 0;    
    uint64_t real_part = 0;

  public:
    ComplexType(uint64_t im, uint64_t re);
    ~ComplexType() = default;
};

ComplexType::ComplexType(uint64_t im, uint64_t re) {
    this->imaginary_part = im;
    this->real_part = re;
}

#endif

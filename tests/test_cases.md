# Test cases – FIT4012 Lab 1

Đánh dấu [x] khi đã chạy và kiểm tra kết quả.

## 1. Entropy / Redundancy

- [x] Input: `aaaa`  
  Expected: Entropy = 0, Redundancy ≈ 8

- [x] Input: `abcd`  
  Expected: Entropy ≈ 2, Redundancy ≈ 6

- [x] Input: `hello world`  
  Expected: Entropy ≈ 2.8 – 3.2, Redundancy ≈ 5 – 5.2

## 2. Modulo inverse

- [x] a = 3, m = 7  
  Expected: 5

- [x] a = 10, m = 17  
  Expected: 12

- [x] a = 6, m = 9  
  Expected: Không tồn tại nghịch đảo (return -1)

## 3. Ghi chú

- Các giá trị entropy có thể sai số nhỏ do số thực.
- Đã kiểm tra bằng chương trình C++.

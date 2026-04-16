[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/WTyCYlbL)
# FIT4012 – Lab 1: Entropy, Redundancy và Modular Inverse

## Giới thiệu
Bài lab này thực hiện:
- Tính entropy của một chuỗi ký tự
- Tính độ dư thừa thông tin (redundancy)
- Tìm nghịch đảo modulo bằng thuật toán Euclid mở rộng

---

## Cấu trúc thư mục

- src/entropy_redundancy.cpp: Tính entropy và redundancy
- src/mod_inverse.cpp: Tìm nghịch đảo modulo
- tests/test_cases.md: Các test case
- logs/run_log.md: Kết quả chạy thử
- report-page.md: Báo cáo 1 trang

---

## Cách chạy chương trình

### Compile

g++ src/entropy_redundancy.cpp -o entropy  
g++ src/mod_inverse.cpp -o mod_inverse  

### Run

./entropy  
./mod_inverse  

---

## Ví dụ

### Entropy

Input:
abcd

Output:
Entropy: 2  
Redundancy: 6  

---

### Modular inverse

Input:
a = 3, m = 7

Output:
Modular inverse: 5  

---

## Kết quả đạt được

- Hoàn thành Q1: Tính entropy
- Hoàn thành Q2: Tính redundancy
- Hoàn thành Q3: Modular inverse bằng Extended Euclid
- Viết test cases và run log đầy đủ

---

## Kiến thức sử dụng

- Entropy trong lý thuyết thông tin
- Logarithm cơ số 2
- Thuật toán Euclid mở rộng

---

## Ghi chú

- Kết quả entropy có thể sai số nhỏ do số thực
- Redundancy được tính theo công thức:
  R = log2(256) - H(X)

# Report 1 Page – FIT4012 Lab 1

## 1. Mục tiêu
Mục tiêu của bài lab là hiểu và cài đặt cách tính entropy của một chuỗi ký tự, từ đó tính độ dư thừa thông tin (redundancy), đồng thời áp dụng thuật toán Euclid mở rộng để tìm nghịch đảo modulo.

---

## 2. Cách làm
- Đọc hiểu chương trình tính entropy dựa trên xác suất xuất hiện của ký tự.
- Cài đặt hàm tính redundancy theo công thức: R = log2(256) - H(X).
- Cài đặt hàm mod_inverse() bằng thuật toán Euclid mở rộng.
- Kiểm tra chương trình với nhiều test case khác nhau.

---

## 3. Kết quả chính

### 3.1 Entropy và redundancy

| Input        | Entropy | Redundancy | Nhận xét |
|--------------|---------|------------|----------|
| aaaa         | 0       | 8          | Chuỗi lặp → entropy thấp |
| abcd         | 2       | 6          | Ký tự phân bố đều |
| hello world  | ~3.0    | ~5.0       | Phân bố không đều |

---

### 3.2 Modulo inverse

| a | m | Kết quả mong đợi | Kết quả chương trình |
|---|---|------------------|----------------------|
| 3 | 7 | 5                | 5                    |
| 10| 17| 12               | 12                   |
| 6 | 9 | Không tồn tại    | -1                   |

---

## 4. Kết luận

Qua bài lab, em hiểu rõ cách tính entropy dựa trên xác suất và ý nghĩa của độ dư thừa thông tin trong dữ liệu. Ngoài ra, em cũng nắm được cách hoạt động của thuật toán Euclid mở rộng để tìm nghịch đảo modulo. Khó khăn lớn nhất là hiểu cách chuyển đổi từ công thức toán học sang code, nhưng sau khi thực hành và kiểm thử, em đã hiểu rõ hơn bản chất của các thuật toán này.

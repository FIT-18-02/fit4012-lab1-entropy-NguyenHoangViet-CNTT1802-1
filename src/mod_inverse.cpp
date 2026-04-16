#include <iostream>
using namespace std;

int extended_euclid(int a, int b, int &x, int &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }

    int x1, y1;
    int g = extended_euclid(b, a % b, x1, y1);

    x = y1;
    y = x1 - (a / b) * y1;

    return g;
}

int mod_inverse(int a, int m) {
    int x, y;
    int g = extended_euclid(a, m, x, y);

    if (g != 1) {
        return -1;
    }

    // chuẩn hóa kết quả về [0, m-1]
    x = (x % m + m) % m;
    return x;
}

int main() {
    int a, m;
    cin >> a >> m;

    int inv = mod_inverse(a, m);

    if (inv == -1) {
        cout << -1 << endl;
    } else {
        cout << inv << endl;
    }

    return 0;
}

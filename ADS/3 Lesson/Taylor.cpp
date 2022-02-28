#include <iostream>
#include <cmath>

int main() {
    int n = 0;

    double eps = 0.00001;
    double x;

    std::cout << "[>] Enter X: ";
    std::cin >> x;

    double an = x;
    double y = 0.0;

    while (fabs(an) > eps) {
        y += an;
        n++;
        an *= -x * x / (2 * n * (2 * n + 1));
    }

    std::cout << "[>] Enter Y: " << y << std::endl;

    return 0;
}


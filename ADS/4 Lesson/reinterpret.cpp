#include <iostream>

int main() {
    double x = 1.1;

    std::cout << "[+] Start value: " << x << std::endl;
    std::cout << "[+] Static cast value: " << static_cast<int>(x) << std::endl;
    std::cout << "[+] Reinterpret cast value: " << *reinterpret_cast<int *>(&x) << std::endl;
}


#include <iostream>

int main() {
    bool flag = false;

    u_int32_t x;
    
    std::cout << "[>] Enter X: ";
    std::cin >> x;

    while (x != 0) {
        if (x % 10 == 7) {
            flag = true;
            break;
        }
        x /= 10;
    }

    if (flag) {
        std::cout << "[+] The number contains the digit 7" << std::endl;
    } else {
        std::cout << "[-] The number does not contain the digit 7" << std::endl;
    }

    return 0;
}


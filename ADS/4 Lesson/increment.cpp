#include <iostream>

void increment(int* number);

int main() {
    int a;

    std::cout << "[>] Enter number: ";
    std::cin >> a;

    increment(&a);

    return 0;
}

void increment(int* number) {
    std::cout << "[+] Start value: " << *number << std::endl;
    *number = *number + 1;
    std::cout << "[+] Incremented value: " << *number << std::endl;
}


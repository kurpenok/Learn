#include <iostream>

struct t_Pair {
    int a;
    int b;
};

t_Pair return_pair(int number);

void modify_pair(t_Pair *p);

int main() {
    int number;

    std::cout << "[>] Enter number: ";
    std::cin >> number;
    
    t_Pair result = return_pair(number);
    std::cout << "[+] TPair result A: " << result.a << std::endl;
    std::cout << "[+] TPair result B: " << result.b << std::endl;

    modify_pair(&result);
    std::cout << "[+] TPair modify result A: " << result.a << std::endl;
    std::cout << "[+] TPair modify result B: " << result.b << std::endl;
}

t_Pair return_pair(int number) {
    t_Pair result;

    result.a = number * number;
    result.b = number * number * number;

    return result;
}

void modify_pair(t_Pair *p) {
    p->a += 1;
    p->b += 10;
}


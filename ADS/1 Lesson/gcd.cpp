#include <iostream>

int gcd(int a, int b);

int main() {
	int a, b;

	std::cout << "[>] Enter A and B: ";
	std::cin >> a >> b;

	std::cout << "[+] GCD: " << gcd(a, b) << std::endl;
	
	return 0;
}

int gcd(int a, int b) {
	while (a != b) {
		if (a > b) {
			a -= b;
		} else {
			b -= a;
		}
	}
	return a;
}


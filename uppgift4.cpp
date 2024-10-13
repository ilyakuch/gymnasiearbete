#include <iostream>

unsigned long long factorial(int n) {
    if (n == 0)
        return 1;
    return n * factorial(n - 1);
}

int main() {
    unsigned long long result = factorial(1000); // Adjust this number for larger test
    std::cout << "C++ Factorial Result: " << result << std::endl;
    return 0;
}

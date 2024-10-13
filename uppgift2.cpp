#include <iostream>
#include <vector>
#include <algorithm>
#include <random>

std::vector<int> create_and_sort(int n) {
    std::vector<int> data(n);
    std::generate(data.begin(), data.end(), []() { return rand() % 1000000; });
    std::sort(data.begin(), data.end());
    return data;
}

int main() {
    auto sorted_data = create_and_sort(1000000);
    std::cout << "C++ Sorted Count: " << sorted_data.size() << std::endl;
    return 0;
}

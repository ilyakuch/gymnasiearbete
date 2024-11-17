#include <vector>
#include <iostream>

int quadratic(std::vector<int>& arr) {
    int pairs = 0;
    for (size_t i = 0; i < arr.size(); ++i) {
        for (size_t j = i + 1; j < arr.size(); ++j) {
            pairs++;
        }
    }
    return pairs;
}

int main() {
    std::vector<int> arrr = {1, 2, 3, 4, 5};
    quadratic(arrr);
    
    return 0;
}
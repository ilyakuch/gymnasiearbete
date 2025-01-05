#include <vector>
#include <iostream>
#include <chrono>
#include <utility>

void linear(int input_size) {
    for (size_t i = 0; i < input_size; ++i) {
        ;
    }
}

int main() {
    
    const int MAX_SIZE = 10000000;
    const int INCREMENT = 100000;
    const int MAX_RUNTIME = 10;
    
    int input_size = 0;
    std::vector<std::pair<int, double>> results;

    std::chrono::duration<double> measurment;
    

    while (input_size <= MAX_SIZE && measurment.count() <= MAX_RUNTIME) {
        

        auto start1 = std::chrono::high_resolution_clock::now();
        linear(input_size);
        auto end1 = std::chrono::high_resolution_clock::now();

        auto start2 = std::chrono::high_resolution_clock::now();
        linear(input_size);
        auto end2 = std::chrono::high_resolution_clock::now();

        measurment = ((end1 - start1) + (end2 - start2)/2);

        std::cout << std::fixed << input_size << "," << measurment.count()*1000 << std::endl;

        input_size += INCREMENT;

    }
    
    return 0;
}
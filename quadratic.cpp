#include <vector>
#include <iostream>
#include <chrono>
#include <utility>

void quadratic(int input_size) {
    for (size_t i = 0; i < input_size; ++i) {
        for (size_t j = i; j < input_size; ++j) {
            ;
        }
    }
}

int main() {
    
    const int MAX_SIZE = 10000000;
    const int INCREMENT = 1000;
    const int MAX_RUNTIME = 10;
    
    int input_size = 0;
    std::vector<std::pair<int, double>> results;

    std::chrono::duration<double> measurment;
    

    while (input_size <= MAX_SIZE && measurment.count() <= MAX_RUNTIME) {
        

        auto start = std::chrono::high_resolution_clock::now();
        quadratic(input_size);
        auto end = std::chrono::high_resolution_clock::now();

        measurment = end - start;

        std::cout << "Round: " << input_size << "  Time: " << measurment.count() << " s" << std::endl;

        results.push_back({input_size, measurment.count()});

        input_size += INCREMENT;

    }

    std::cout << "\n\nComplete\ncsv\n\nx,y" << std::endl;
    for (const auto& i : results) {
        std::cout << i.first << "," << i.second << std::endl;
    }
    
    return 0;
}
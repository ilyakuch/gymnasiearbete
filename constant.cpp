#include <vector>
#include <iostream>
#include <chrono>
#include <utility>

void constant(int input_size) {
    ;
}

int main() {
    
    const int MAX_SIZE = 10000000;
    const int INCREMENT = 100000;
    const int MAX_RUNTIME = 10;
    
    int input_size = 0;
    std::vector<std::pair<int, double>> results;

    std::chrono::duration<double> measurment;
    

    while (input_size <= MAX_SIZE && measurment.count() <= MAX_RUNTIME) {
        

        auto start = std::chrono::high_resolution_clock::now();
        constant(input_size);
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
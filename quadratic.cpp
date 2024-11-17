#include <vector>
#include <iostream>
#include <chrono>
#include <utility>

int quadratic(std::vector<int>& dataset) {
    int pairs = 0;
    for (size_t i = 0; i < dataset.size(); ++i) {
        for (size_t j = i + 1; j < dataset.size(); ++j) {
            pairs++;
        }
    }
    return pairs;
}

int main() {
    
    const int max_size = 100000;
    const int increment = 100;
    const int max_runtime = 60;
    
    int iteration = 1;
    std::vector<std::pair<int, int>> results;
    

    while (iteration < max_size) {

        std::vector<int> dataset;

        for (size_t i = 0; i < iteration; i++) {
            dataset.push_back(i);
        }

        auto start = std::chrono::high_resolution_clock::now();
        int iteration_return = quadratic(dataset);
        auto end = std::chrono::high_resolution_clock::now();

        std::chrono::duration<double> measurment = end - start;

        std::cout << measurment.count() << "Iteration: " << iteration << " --- Returned: " << iteration_return << std::endl;

        results.push_back({iteration, measurment.count()});

        iteration = iteration + increment;

    }

    for (const auto& i : results) {
        std::cout << i.first << ", " << i.second << std::endl;
    }
    
    return 0;
}
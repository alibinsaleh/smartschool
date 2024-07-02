#include <iostream>
#include <vector>
#include <algorithm>
#include <memory>

// Function to print a vector
void printVector(const std::vector<int>& vec) {
    for (int num : vec) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
}

int main() {
    // Create a vector of integers using modern initializer list syntax
    std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // Print the original vector
    std::cout << "Original vector: ";
    printVector(numbers);

    // Use a lambda expression to filter out even numbers
    std::vector<int> oddNumbers;
    std::copy_if(numbers.begin(), numbers.end(), std::back_inserter(oddNumbers), [](int num) {
        return num % 2 != 0;
    });

    // Print the filtered vector
    std::cout << "Filtered (odd) vector: ";
    printVector(oddNumbers);

    // Demonstrate the use of smart pointers
    std::unique_ptr<int[]> smartArray(new int[5]{10, 20, 30, 40, 50});
    std::cout << "Smart pointer array: ";
    for (int i = 0; i < 5; ++i) {
        std::cout << smartArray[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}


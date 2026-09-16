/* Converting LARGEST & SMALLEST python alg to CPP */
#include <iostream> 
#include <vector>

/* BLOCK 2 *//////////////////////////////////////////////////////////////////

// void largestAndSmallest(const std::vector<int>& integerLst){
//     int largest = integerLst[0];
//     int smallest = integerLst[0];
//     int lstSize = static_cast<int>(integerLst.size());

//     for (int i = 0; i < lstSize; i++){
//         if (integerLst[i] > largest) {
//             largest = integerLst[i];
//         }
//         else if (integerLst[i] < smallest){
//             smallest = integerLst[i];
//         }
//     }
//     // return largest, smallest
//     std::cout << "Largest: " << largest << " SMALLEST: " << smallest << "\n";
// }

// int main(){
//     std::vector<int> numbers = {50, 20, 30};
//     largestAndSmallest(numbers);
//     return 0;
// }

/* BLOCK 3 */////////////////////////////////////////////////////////////////

// Because this uses a reference, we are referencing to the value at that location
// which will end up being changed.
// the & means x refers to the original number, so changes affect number
// void change(int& x){
//     x = 100; 
// }

// int main(){
//     int number = 5;
//     change(number);
//     std::cout << number << "\n";
// }

// Here, because the x variable is being changed, the value number from main() remains unchanged
// x starts as a copy of number, changing x does not change number
// void change(int x){
//     x = 100; 
// }

// int main(){
//     int number = 5;
//     change(number);
//     std::cout << number << "\n";
// }

/* BLOCK 4 *////////////////////////////////////////////////////////
void moveZeros(std::vector<int>& intList){
    int write = 0; // the next location where a nonzero value belongs
    int lstSize = static_cast<int>(intList.size());
    for (int i = 0; i < lstSize; i++){
        if (intList[i] != 0){
            intList[write] = intList[i];
            write += 1;
        }
    }
    while (write < lstSize){
        intList[write] = 0;
        write += 1;
    }
}

void printList(const std::vector<int>& numbers){
    std::cout << "[";
    for(std::size_t i = 0; i < numbers.size(); i++){
        std::cout << numbers[i];
        if (i < numbers.size() - 1){
            std::cout << ", ";
        }
    }
    std::cout << "]\n";
}

int main(){
    std::vector<int> inp = {1, 0, 0, 3, 4};
    moveZeros(inp);
    printList(inp);
    return 0;
}
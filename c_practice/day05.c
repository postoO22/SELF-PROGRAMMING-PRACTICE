// #include <stdio.h>
// #include <stdlib.h>

// int buyAndSellStock(int stockPrices[], int size) {
//     // Empty input?
//     if(size == 0) {
//         return 0;
//     }

//     // Initialize minPrice
//     int minPrice = stockPrices[0];

//     // Initialize maxProfit
//     int maxProfit = 0;

//     // Traverse prices
//     for (int i = 0; i < size; i++)
//     {
//         // Current price?
//         int *value = stockPrices;

//         // Found cheaper buying price?
//         if (minPrice > *(value + i)) {
//             minPrice = *(value + i);
//         }

//         // Otherwise, could selling today improve maxProfit?
//         else if ((*(value + i) - minPrice) > maxProfit) {
//             maxProfit = (*(value + i) - minPrice);
//         }
//     }

//     return maxProfit;
// }


// int main(void) {
//     int prices[] = {7, 1, 5, 3, 6, 4};
//     int size = 6;
//     int result = buyAndSellStock(prices, size);
//     printf("%d\n", result);
//     return 0;
// }

// // A pointer stores a memory address 
// // Dereferencing means to get the value stored at the memory address pointed to by the pointer
// // array[i] is equivalent to *(array + i)


////////// DAY 06 /////////////
// int main(void)
// {
//     // allocate space for 5 ints
//     int *ptr = malloc(5 * sizeof(int));

//     // Check if malloc succeeded 
//     if (ptr == NULL) {
//         return 1;
//     }
//     // fill the spaces
//     for (int i = 0; i < 5; i++){
//         *(ptr + i) = 20 + i;
//         // print them
//         printf("%d\n", ptr[i]);
//     }
//     // free the memory PROPERLY
//     free(ptr);
//     ptr = NULL;
//     return 0;
// }

// #include <stdio.h>
// #include <stdlib.h>

// int main(void)
// {
//     int count;

//     printf("How many integers? ");
//     scanf("%d", &count);

//     if (count <= 0){
//         return 1;
//     }
//     // TODO 1:
//     // Allocate enough heap memory for `count` integers.
//     int *ptr = malloc(count * sizeof(int));
//     // TODO 2:
//     // Check whether malloc failed.
//     if (ptr == NULL) {
//         return 1;
//     }
//     // TODO 3:
//     // Fill the allocated memory with values.
//     // For now, you can store:
//     // 10, 11, 12, 13, ...
//     for (int i = 0; i < count; i++) {
//         ptr[i] = 10 + i;
//         // TODO 4:
//         // Print every value.
//         printf("%d\n", ptr[i]);
//     }
//     // TODO 5:
//     // Free the memory and set the pointer to NULL.
//     free(ptr);
//     ptr = NULL;

//     return 0;
// }

//// STRUCTS PRACTICE REDOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO ////

// #include <stdio.h>
// #include <stdlib.h>

// struct Student {
//     int id;
//     int score;
// };

// int main(void)
// {
//     // TODO 1:
//     // Dynamically allocate enough heap memory
//     // for ONE struct Student.
//     //
//     // What type should ptr be?
//     // What should go inside malloc()?
    
//     struct Student *ptr = malloc(sizeof(struct Student));


//     // TODO 2:
//     // Check whether allocation succeeded.

//     if (ptr == NULL) {
//         return 1;
//     }

//     // TODO 3:
//     // Through ptr, set:
//     // id = 42
//     // score = 88
//     //
//     // Try using -> rather than (*ptr).field
//     ptr->id = 42;
//     ptr->score = 88;

//     // TODO 4:
//     // Print both fields through ptr.
//     printf("%d\n", ptr->id);
//     printf("%d\n", ptr->score);

//     // TODO 5:
//     // Properly release the heap allocation.
//     free(ptr);
//     ptr = NULL;

//     return 0;
// }

/* Move Zeroes */

// Hint: i examines elements, second position could represent where next opening/zero place is.

#include <stdio.h>

void moveZeroes(int numList[], int size) {
    int write = 0;
    for(int read = 0; read < size; read++){
        if (numList[read] != 0) {
            numList[write] = numList[read];
            write += 1;
        }
    }
    while (write < size) {
        numList[write] = 0;
        write += 1;
    }
}

int main(void) {
    int nums[] = {7, 1, 5, 0, 1, 2}; 
    // Reminder: when array is passed to function, an arragy arg is automatically
    // converted to a pointer to its first element.
    // so we call moveZeroes to directly manipulate the list as needed.

    // size found with sizeof(nums) = 6 * 4 = 24 / sizeof(nums[0] = 1 * 4 = 4) 24/4 = 6
    int size = sizeof(nums) / sizeof(nums[0]);
    moveZeroes(nums, size);
    for (int i = 0; i < size; i++) {
        printf("%d ", nums[i]);
    }
    printf("\n");
    return 0;
}

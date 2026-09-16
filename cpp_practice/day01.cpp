/* PROBLEM 1 */
// #include <iostream> 
// int main() {
//     int total = 0;
//     int n;
//     std::cout << "Enter a number: ";
//     std::cin >> n;

//     if (n == 0){
//         std::cout << "Your number is zero.\n";
//     }
//     else if (n > 0){
//         std::cout << "Your number is positive.\n";
//         if (n % 2 == 0){
//             std::cout << "Your number is even.\n";
//             for (int i = 0; i <= n; i++){
//                 total += i;
//             }
//         }
//         else {
//             std:: cout << "Your number is odd.\n";
//             for (int i = 0; i <= n; i++){
//                 total += i;
//             }
//         }
//     }
//     if (n < 0) {
//         std::cout << "Your number is negative.\n";
//         if (n % 2 == 0) {
//             std::cout << "Your number is even.\n";
//         }
//         else{
//             std::cout << "Your number is odd.\n";
//         }
//     }
//     std::cout << "Your total sum is: " << total << "\n";
//     return 0; 
// }

/* CHALLENGE */

// #include <iostream>

// int main() {
//     int num;
//     int reversed = 0;
//     int removedNum;
//     int tail;
//     std::cout << "Enter a number: ";
//     std::cin >> num;
//     tail = num;

//     if (num < 0){
//         std::cout << "Not a palindrome.\n";
//         return 0;
//     }
//     while (tail > 0){
//         removedNum = tail % 10;
//         reversed *= 10;
//         reversed += removedNum;
//         tail /= 10;
//     }
//     reversed += tail;
//     if (reversed == num){
//         std::cout << "Palindrome: " << reversed << "\n";
//     }
//     else { 
//         std::cout << num << " is not a palindrome.\n";
//     }
//     return 0;
// }
//-------------------------------------------------------
// What remained identical between Python and C++?
    // A lot of the flow is the same (taking in inputs and when to do what kind of 
    // math to get the last int to add to the reverse variable and how to get the tail)
// What changed?
    // Instead of '//' dividing in Python, we use '/' just one in CPP. 
// Which changes were syntax?
    // The semicolons in CPP and code blocks.
    // And console outputs (print vs std::cout)
// Which changes were caused by the languages behaving differently?
    // One that I can think of is declaring variables (static typing vs dynamic in CPP vs Python accordingly.)
    

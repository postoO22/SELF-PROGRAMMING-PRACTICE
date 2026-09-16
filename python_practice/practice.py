############################
# Given a number, determine whether
# it is positive/negative/zero
# and even/odd
############################

# def number_type(number):
#         # number = input("Enter a number or type 'quit': ")
#     number = int(number)
#     if number == 0:
#         return 0
#     elif number > 0:
#         if number % 2 == 0:
#             return "Positive, even number"
#         else:
#             return "Positive, odd number"

#     else:
#         if number % 2 == 0:
#             return "Negative, even number"
#         else: 
#             return "Negative, odd number"


# def main():
#     # repeatedly ask user for input
#     inp = input("Enter a number or type 'quit': ")
#     while inp != 'quit':
#         number = int(inp)
#         result = number_type(number)
#         print(result)
#         inp = input("Enter a number or type 'quit': ")

# if __name__ == "__main__":
#     main()


############################
# Print every number from 1-100 divisible by 3 but not 5
############################


# for num in range(1,111):
#     if num % 3 == 0 and num % 5 != 0:
#         print(num)


############################
# Repeatedly remove the last digit from an integer and print each digit
############################

# def remove_last(number):
#     num = str(number)
#     digits = list(num)
#     for digit in range(len(digits)):
#         print(digits.pop())
        

# def main():
#     inp = input("enter a number: ")
#     while inp != 'quit':
#         number = inp
#         remove_last(number)
#         inp = input("enter a number: ")

# if __name__ == "__main__":
#     main()

## OR ## COME BACK TO THIS-----------------------------------------------

# def remove_last(number):
#     # Remove last digit with % 10
#     # Remove last digit from number with // 10
#     # Keep doing until we get to the final digit
#     length = 0
#     while length < len(number) +1:
#         last_dig = number % 10 
#         number = number // 10
#         print(last_dig)
        

# def main():
#     inp = input("enter a number: ")
#     while inp != 'quit':
#         number = inp
#         remove_last(number)
#         inp = input("enter a number: ")

# if __name__ == "__main__":
#     main()

#------------------------------------------------------------------------------

# DAY 1 Practice:

# TODO: write a program that asks for an integer, determines whether it is positive
# negative, or zero; determines whether it is even or odd; prints every integer
# from 1 to that number if positive; calculates their sum.

###################################################
# INPUT: (int) number
# OUTPUT: Prints each integer from 1 to the number if positive, calculates their sum
# SPECIAL CASES: If positive, print every integer from 1 through that number and 
#       calculates their sum.
# STEPS:
#   1. Take in int
#   2. Determine if positive (> 0), negative (< 0), or zero (== 0)
#   3. Determine if even (% 2 == 0), or odd (%2 != 0)
#   4. if positive, print every int from 1 through that number.
#   5. if positive and print every int from 1 through that number, simultaneously
#       calculate the sum with each number added from 1 to that number.
#       return the sum, otherwise return (if zero or negative number), return either 0
#       or -1 respectfully.
####################################################

# def number_characteristics(number):
#     sum = 0
#     if number > 0:
#         if number % 2 == 0:
#             print("Even, positive number.")
#             for integer in range(1, number+1):
#                 print(integer)
#                 sum = sum + integer
#             print("Sum: ")
#             return sum
#         else:
#             print("Odd, positive number.")
#             for integer in range(1, number+1):
#                 print(integer)
#                 sum = sum + integer
#             print("Sum: ")
#             return sum
#     elif number == 0:
#         print("Number is zero")
#         return 0

#     else:
#         if number % 2 == 0:
#             print("Even, negative number.")
#             return -1
#         else:
#             print("Odd, negative number.")
#             return -1

# def main():
#     inp = input("Enter a number or type 'quit': ")
#     while inp != 'quit':
#         num = int(inp)
#         result = number_characteristics(num)
#         print(result)
#         inp = input("Enter a number or type 'quit': ")

# if __name__ == "__main__":
#     main()


#################### DAY 1 6 PROGRAMS:#####################

###################################################
# INTEGER PALINDROME CHECKER: 
#   Complete with arithmetic/digit-removal approach
####################################################

# def palindrome_check(number):
#     ## BASIC OUTLINE: 
#     # Negative numbers instantly ruled out (personal choice)
#     # get last digit in number
#     # next_dig = number % 10
#     # make int holder, first val will be last digit of number
#     # reversed_num = next_dig
#     # get remaining with //
#     # Keep doing while there's one more number left!

#     reversed_num = 0
#     remaining = number
#     if number < 0:
#         return False
#     while remaining // 10 != 0:
#         next_dig = remaining % 10
#         reversed_num = reversed_num + next_dig
#         reversed_num = reversed_num * 10
#         remaining = remaining // 10 
#     # Now at last one (where remaining // 10 == 0)
#     # Add to reversed_num
#     reversed_num = reversed_num + remaining
#     # Check if equivalent to number
#     if reversed_num == number:
#         return True
#     else:
#         return False
        
# def main():
#     inp = int(input("Enter a number: "))
#     result = palindrome_check(inp)
#     print(result)

# if __name__ == "__main__":
#     main()

###################################################
# FREQUENCY COUNTER:
#   Output the frequency count of each element in a list
# O(n^2) complexity worst case
####################################################
# def frequency_counter(word_list):
#     # Input: list of words
#     # Output: each word and their frequency (key-value pair)
#     # Create a dictionary with the list of words
#     # Each value will increase for each instance of the word
#     # Then go through each key-value pair and print them out
#     count = 0
#     freq_dict = {word_list[i] : count for i in range(0, len(word_list))}
#     for word in freq_dict.keys():
#         freq_dict[word] = word_list.count(word)
#     return freq_dict

# def main():
#     inp = ["apple", "apple", "banana", "carrot"] # Used to test
#     result = frequency_counter(inp)
#     for k, v in result.items():
#         print(k,": ",v)

# if __name__ == "__main__":
#     main()

###################################################
# FREQUENCY COUNTER:
#   Output the frequency count of each element in a list
# O(n) complexity (better)
####################################################
# def frequency_counter(word_list):
#     freq_dict = {}
#     for word in word_list:
#         if word in freq_dict:
#             freq_dict[word] += 1
#         else:
#             freq_dict[word] = 1
#     return freq_dict
# def main():
#     inp = ["apple", "apple", "banana", "carrot"] # Used to test
#     result = frequency_counter(inp)
#     for k, v in result.items():
#         print(k,": ",v)

# if __name__ == "__main__":
#     main()

###################################################
# REMOVE DUPLICATES:
#   Given a list, return its unique values.
#   Then answer: why might a set be useful?
#       1. Sets are useful because they do not contain duplicate
#           elements, but not like a dictionary since we don't
#           need any associated values for this problem.
#   And what changes if original order must be preserved?
#       2. If original order must be preserved, we might need
#           to use a list and other operations to get rid
#           of the duplicates (might make things a bit more
#           complex or take more time to complete.)
####################################################
# def remove_dupes(val_list):
#     unique_set = {val_list[i] for i in range(0,len(val_list))}
#     unique_list = list(unique_set) # Just to practice turning to list
#     return unique_list

# def main():
#     inp = ["apple", "apple", "banana", "carrot"]
#     result = remove_dupes(inp)
#     print(result)

# if __name__ == "__main__":
#     main()

###################################################
# SECOND-LARGET NUMBER:
#   Write def second_largest(numbers): 
#   DO NOT sort the list. Think about what info you actually
#   need to remember while traversing it
####################################################
# def second_largest(numbers):
#     largest = numbers[0]
#     second_l = numbers[0]
#     if len(numbers) < 2:
#         return None
#     for number in numbers:
#         if number > largest and number > second_l:
#             second_l = largest
#             largest = number
#         elif number < largest and number > second_l:
#             second_l = number
#     return second_l

# def main():
#     inp = [1, 5, 6, 6, 8, 3 ,9] # should be 8
#     result = second_largest(inp)
#     print(result)

# if __name__ == "__main__":
#     main()



###################################################
# STUDENT ANALYZER:
#   Given a dictionary of students, write seperate functions 
#   to calculate one student's average; find the student with 
#   highest average; determine a letter grade; and print a report
#   for everyone. 
#
# Exp input:
# students = {
#     "Maya": [91, 88, 94],
#     "Leo": [72, 85, 79],
#     "Sam": [98, 95, 99]
# }
####################################################
# def average_calc(grade_list):
#     # calculate's one student's avg
#     total = 0
#     for grade in grade_list:
#         total = total + grade
#     avg = round(total / len(grade_list)) 
#     # Because yes, we will round up and be nice teachers if close to a higher letter grade
#     return avg

# def highest_avg_student(avg_grade_dict):
#     # finds student with highest average
#     highest_student = next(iter(avg_grade_dict))
#     highest_val = avg_grade_dict[highest_student]
#     for k, v in avg_grade_dict.items():
#         if v > highest_val:
#             highest_student = k
#             highest_val = v
#     return highest_student

# def letter_grade(avg_grade):
#     # determine letter grade
#     letter = ""
#     if avg_grade <= 100 and avg_grade >= 94:
#         letter = "A"
#     elif avg_grade <= 93 and avg_grade >= 90:
#         letter = "A-"
#     elif avg_grade <= 89 and avg_grade >= 87:
#         letter = "B+"
#     elif avg_grade <= 86 and avg_grade >= 83:
#         letter = "B"
#     elif avg_grade <= 82 and avg_grade >= 80:
#         letter = "B-"
#     elif avg_grade <= 79 and avg_grade >= 77:
#         letter = "C+"
#     elif avg_grade <= 76 and avg_grade >= 73:
#         letter = "C"
#     elif avg_grade <= 72 and avg_grade >= 70:
#         letter = "C-"
#     elif avg_grade <= 69 and avg_grade >= 67:
#         letter = "D+"
#     elif avg_grade <= 66 and avg_grade >= 60:
#         letter = "D"
#     else:
#         letter = "F"
#     return letter

# def print_report(student, student_grades):
#     # printing report for everyone
#     # We'll print one student's individual grades,
#     # their average grade, and resulting letter grade
#     print(student,"'S GRADES: ")
#     print(student_grades)
#     average_grade = average_calc(student_grades)
#     print("AVERAGE: ", average_grade)
#     letter = letter_grade(average_grade)
#     print("LETTER GRADE: ", letter)
#     print("END REPORT")

# def main():
#     student_dict = {'Kyle': [93, 92, 92, 99],
#                     'Zachary': [99, 99, 34, 98],
#                     'Anna': [92, 94, 96, 99],
#                     'Madeline': [97, 98, 98, 99],
#                     'Matilda': [85, 77, 87,44]}
#     student_list = list(student_dict.keys())
#     highest_avg_grade_dict = {}
#     for student in student_list:
#         print_report(student, student_dict[student])
#         avg_grade = average_calc(student_dict[student])
#         highest_avg_grade_dict[student] = avg_grade
#     highest_student = highest_avg_student(highest_avg_grade_dict)
#     print("Student with highest average: ", highest_student)

# if __name__ == "__main__":
#     main()

###################################################
# MINI INVENTORY SYSTEM:
#   Store items with quantities. Program must support
#   conceptually: add_item(), remove_item(), change_quantity(),
#   find_item() and show_inventory(). You decide representation
#   Write the following:
#       What info exists? - we know what items the user wants to work with and that we need
#           the quantity of each item.
#       What operations exist? - we know how to get key and values, how to delete keys,
#           how to make key, val pairs.
#       Which data structure represents the information naturally? - Dictionaries!
####################################################
# inventory = {}

# def add_item(item):
#     if item in inventory:
#         inventory[item] += 1
#     else:
#         inventory[item] = 1

# def remove_item(item):
#     if item in inventory and inventory.get(item) > 1:
#         inventory[item] -= 1
#     elif item in inventory and inventory.get(item) == 1:
#         del inventory[item]
#     else:
#         print("Item not in list.")

# def change_quantity(item, quantity):
#     inventory[item] = quantity

# def find_item(item):
#     if item in inventory:
#         print(item, " found! You have: ", inventory.get(item))
#     else:
#         print(item, " not found.")

# def show_inventory():
#     print("INVENTORY: ", inventory)

# def main():
#     # First thing you can do is add an item
#     # inventory = {}
#     inp = input("Add an item to inventory: ")
#     add_item(inp)
#     show_inventory()
#     inp = input("'add', 'remove', 'change' quantity, 'find' items, 'show' inventory or 'quit': ")
#     while inp != "quit":
#         if inp == "add":
#             show_inventory()
#             inp_item = input("Add an item to inventory: ")
#             add_item(inp_item)
#             print("Updated inventory: ", inventory)
#         elif inp == "remove":
#             show_inventory()
#             inp_item = input("Remove an item from inventory: ")
#             remove_item(inp_item)
#             print("Updated inventory: ", inventory)
#         elif inp == "change":
#             show_inventory()
#             inp_item = input("What item would you like to change? ")
#             quantity = input("How much do you want? ")
#             change_quantity(inp_item, quantity)
#             print("Updated inventory: ", inventory)
#         elif inp == "find":
#             inp_item = input("What are you looking for? ")
#             find_item(inp_item)
#         else:
#             show_inventory()
#         inp = input("'add', 'remove', 'change' quantity, 'find' items, 'show' inventory or 'quit': ")

# if __name__ == "__main__":
#     main()

###################################################
# Paragraph Analysis:
#
# INPUT: A paragraph
# DESIRED OUTPUT: total words, unique words, most frequent words, frequency of word, average word length, longest word. No punctuation marks counted.
# EXAMPLE: "I made a dog bark." Total words: 5, unique words: 'I', 'made', 'a', 'dog', 'bark', most frequent words: None, frequency of word: I = 1, made = 1, a = 1, dog = 1, bark = 1
#     # average word length: 2.6 (I'll round to be 3). Longest word = 'made' (choosing first with the longest length).
# WHAT DATA MUST I TRACK? length of words, frequency of words, longest word, number of words.
# POSSIBLE DATA STRUCTURES: List, dictionary
# SUBPROBLEMS: 
# PSEUDOCODE: (will be in each function)
# IMPLEMENTATION: (Each funciton above)
# TESTS: Making sure punctuations are stripped from paragraph. (Printing out to see). Checking if there are ties between words.
# COMPLEXITY:(Not sure how to do this)
####################################################

# def clean_paragraph(paragraph):
#     # Clean the paragraph, then split each word as elements in a list
#     exclude = set(',.!?:;')
#     cleaned = ''.join(char for char in paragraph if char not in exclude)
#     # Make all words lowercase so computer doesn't think that 
#     # a word is not the same simply because one has a capital letter:
#     cleaned = cleaned.lower()
#     return cleaned

# def total_words(paragraph): 
#     # Output: Will return the list and length of list
#     # Make list of all the words in the paragraph
#     lst_of_words = paragraph.split(" ")
#     # Now we have each word in the paragraph (including possible repeats), total words
#     # will include number of words (even repeats, here)
#     length = len(lst_of_words)
#     return lst_of_words, length

# def unique_words(word_list):
#     # Output: a set of unique words from the word list
#     word_set = set(word_list)
#     # Find number of unique words:
#     num_unique = len(word_set)
#     return num_unique, word_set

# def most_freq_word(word_list):
#     # Output: most frequent word and dictionary
#     count = 0
#     freq_dict = {word_list[i] : count for i in range(0, len(word_list))}
#     for word in freq_dict.keys():
#         freq_dict[word] = word_list.count(word)
#     most_freq = max(freq_dict, key=freq_dict.get)
#     return most_freq, freq_dict

# def freq_of_words(freq_dict):
#     for k, v in freq_dict.items():
#         print(k,": ",v)

# def avg_length(word_lst, num_words):
#     sum_len = 0
#     for word in word_lst:
#         sum_len = sum_len + len(word)
#     avg_len = sum_len / num_words
#     return avg_len

# def longest_word(word_set):
#     longest = ""
#     for word in word_set:
#         if len(word) > len(longest):
#             longest = word
#     return longest

# def main():
#     inp = input("Enter a paragraph: ")
#     cleaned = clean_paragraph(inp)
#     word_lst, num_words = total_words(cleaned)
#     number_unique, unique_set = unique_words(word_lst)
#     most_freq, freq_dict = most_freq_word(word_lst)
#     avg_len = avg_length(word_lst, num_words)
#     long_word = longest_word(unique_set)

#     print("REPORT:")
#     print("TOTAL WORDS: ", num_words)
#     print("UNIQUE WORDS: ", unique_set)
#     print("MOST FREQUENT WORD: ", most_freq)
#     print("FREQUENCY OF EACH WORD: ")
#     freq_of_words(freq_dict)
#     print("AVERAGE WORD LENGTH: ", avg_len)
#     print("LONGEST WORD: ", long_word)




# if __name__ == '__main__':
#     main()


# Unique words:
# Most frequent word:
# Frequency of each word:
# Average word length:
# Longest word:

######################################################################################

###################################################
# LARGEST & SMALLEST:
#
# INPUT: an integer list
# OUTPUT: the largest and smallest int in a list
# BRUTE FORCE: Can automatically visually see which is the largest and smallest
#   and simply do O(1) complexity knowing their direct index
# WHAT MUST I REMEMBER? DO NOT use max(), min() or sort(), do in one traversal.
# PSEUDOCODE:
#   need variable to hold largest
#   need variable to hold smallest
#   for each int in the list
#       compare int to largest and smallest known int
#       replace either if needed.
#   return once done
# TIME: O(N) ???
# SPACE: ???
# CODE:
# def largest_and_smallest(integer_lst):
#     largest = integer_lst[0]
#     smallest = integer_lst[0]
#     for integer in integer_lst:
#         if integer > largest:
#             largest = integer
#         elif integer < smallest:
#             smallest = integer
#     return largest, smallest

# def main():
#     inp = [4, 7, 8, 8, 3, 5, 1]
#     large, small = largest_and_smallest(inp)
#     print("LARGEST: ", large, " SMALLEST: ", small)

# if __name__ == '__main__':
#     main()
###################################################

###################################################
# SECOND LARGEST:
#
# INPUT: An int list
# OUTPUT: the second largest integer in the list (if duplicates, choose second distinctive value)
# BRUTE FORCE: Scan every element and maintain largest/smallest -> O(N)
# WHAT MUST I REMEMBER?  We want second distinct value 
# PSEUDOCODE:
#   Have variable that holds second largest value
#   Have variable that holds the third largest
#   Have variable that holds largest
#   for each integer in list
#       compare as needed
#   return second largest
# TIME: O(N) because we're only going through the n-length list 1 time
# SPACE: 
# CODE:
# def second_largest(int_list):
#     largest = int_list[0]
#     second = 0

#     for integer in int_list:
#         if integer > second and integer < largest:
#             # third = second
#             second = integer
#         elif integer > largest:
#             second = largest
#             largest = integer
#     return second, largest

# def main():
#     inp = [-8, -4, -6]
#     second, largest = second_largest(inp)
#     print("LARGEST: ", largest, " SECOND LARGEST: ", second)

# if __name__ == '__main__':
#     main()

###################################################
# SECOND-LARGET NUMBER FIXED:
#   Write def second_largest(numbers): 
#   DO NOT sort the list. Think about what info you actually
#   need to remember while traversing it
# FIX: with using an actual "not found yet" state
####################################################
# def second_largest(int_list):
#     largest = int_list[0]
#     second = None

#     for integer in int_list:
#         if integer < largest and (second is None or integer > second):
#             second = integer
#         elif integer > largest:
#             second = largest
#             largest = integer
#     return second, largest

# def main():
#     inp = [-3, -5, 6]
#     second, largest = second_largest(inp)
#     print("LARGEST: ", largest, " SECOND LARGEST: ", second)

# if __name__ == '__main__':
#     main()


###################################################
###################################################
# MOVE ZEROS:
#
# INPUT: An int list
# OUTPUT: Int list with all the zeros moved to the end
# BRUTE FORCE: Again, can simply visually see and choose the index where located or where we want to switch locations
# WHAT MUST I REMEMBER? consider not making a completely separate result list
# PSEUDOCODE:
#   Have temp variable to hold the index for switching things about
# TIME: O(n) because we go through the list once
# SPACE: NOT ENTIRELY SURE -- PLEASE EXPLAIN HOW TO FIND SPACE COMPLEXITY
# CODE: 

# def move_zeros(int_list):
#     # Pseudocode/ Thought process:

#     # start wih [0, 5, 0, 3, 8, 0, 2]
#     # want [5, 3, 8, 2, 0, 0, 0]
#     # preserve relative order of nonzero values

#     # have one variable meaning: the next location where a nonzero value belongs
#     # first it looks at ind 0: value is 0 (when scnaning left to right)
#     # next number is first nonzero : 5 -> save to index 0
#     # remaining is 0, 3, 8, 0, 2
#     # next number is 0, ignore-ish
#     # then 3, want to move this to index 1
#     # then 8, want to move to index 2
#     # next is 0. "Ignore" it.
#     # finally 2 we want to move to index 3

#     # Use 2 pointer method: read and write
#     # read - Going to be for finding the first nonzero value
#     write = 0 # the next location where a nonzero value belongs
#     for read in int_list:
#         if read != 0: 
#             int_list[write] = read
#             write = write + 1
#     while write < len(int_list):
#         int_list[write] = 0
#         write = write + 1
#     print(int_list)

# def main():
#     inp = [1, 0, 0, 3, 4]
#     move_zeros(inp)

# if __name__ == '__main__':
#     main()






########################################
# Problem 1 -- Duplicate Detection
########################################

# def dupe(int_list):
#     # O(n^2) approach: for each x, process all n vals of y to see if it is the same
#     # as x
#     for ind, x in enumerate(int_list):
#         for y in int_list[ind +1: len(int_list)+1]:
#             if x == y:
#                 return True
#     return False

# def main():
#     inp = [4, 2, 1, 2, 5]
#     print(dupe(inp))

# if __name__ == '__main__':
#     main()
# NOT SURE HOW TO IMPROVE -- NEED HELP / POINTERS

##### BETTER DUPE COMPLEXITY################
# def dupe(int_list):
#     # O(n) approach. Goes through list once and checking if x is in the set is O(1) complexity
#     seen = set()
#     for x in int_list:
#         if x in seen:
#             return True
#         else:
#             seen.add(x)
#     return False

# def main():
#     inp = [4, 2, 1, 2, 5]
#     print(dupe(inp))

# if __name__ == '__main__':
#     main()

########################################
# Problem 2 -- FREQUENCY COUNTER
########################################
# A dictionary is a better representation than repeatedly calling .count()
# because it has O(1) complexity to look up while count goes through the whole
# list to count the number of times it finds whatever word we're looking for.

########################################
# Problem 3 -- TWO SUM
########################################
# DIDN'T HAVE TIME (Sorry!) But my idea is possibly keep a dictionary since the look up
# is O(1) where the key is the number and the value is the indices of where its located?
# Then we can look at the target, subtract the current number , look up if the difference is in
# the dictionary, if yes then the current number index and the dictionary value index is returned

# def two_sum(int_list, target):
#     num_dict = {}
#     for ind, val in enumerate(int_list):
#         search_num = target - val
#         if search_num in num_dict.keys():
#             return num_dict[search_num], ind
#         else:
#             num_dict[val] = ind
#     return 0, 0

# def main():
#     inp = [3, 4, 6, 2, 7]
#     target = 6 # Should be 1, 3
#     ind_1, ind_2 = two_sum(inp, target)
#     print("Output: ", ind_1, ind_2)

# if __name__ == '__main__':
#     main()

########################################
# BLOCK 5: REDO FROM MEMORY: DUPLICATE DETECTION AND TWO SUM
########################################
# def dupe(int_list):
#     # Given list, return whether any dupes exit:
#     # make a seen list,
#     # go through the int list, check if in seen set, then add to set
#     seen = set()
#     for integer in int_list:
#         if integer in seen:
#             return True
#         seen.add(integer)
#     return False

# def main():
#     inp_1 = [3, 4, 5, 6, 7]
#     inp_2 = [2, 2, 4, 6, 8]
#     print(dupe(inp_1)) # False
#     print(dupe(inp_2)) # True

# if __name__ == '__main__':
#     main()

# def two_sum(int_list, target):
#     # Find two indices whose values sum to target
#     # Create a seen dictionary (element as key, index as value)
#     # go through list and calculate target - curr_integer
#     # if the difference in seen dictionary, get the index
#     seen = {}
#     for index, curr_int in enumerate(int_list):
#         difference = target - curr_int
#         if difference in seen:
#             return seen[difference], index
#         else:
#             seen[curr_int] = index
#     return None, None

# def main():
#     inp = [6, 3, 3, 4, 2] # (0, 3)
#     target = 10
#     print(two_sum(inp, target))

# if __name__ == '__main__':
#     main()

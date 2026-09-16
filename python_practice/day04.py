# def reverse_string(word):
#     stack = []
#     reversed_word = ""
#     word_len = 0
#     for character in word:
#         stack.append(character)
#     print(stack)
#     # Now we have list with each element beign a character in order
#     while word_len <= len(stack) + 1:
#         reversed_word += stack.pop()
#         word_len += 1
#     return reversed_word

# def main():
#     inp = "cat"
#     print(reverse_string(inp))

# if __name__ == '__main__':
#     main()

# def valid_parenthesis(string):
#     # When I encounter an opening symbol:
#         # Need to keep track if the last opened symbol is met first with the same closing symbol
#     # When I encounter a closing symbol, make sure that it matches an opening symbol 
#     # At the top of the stack should be an opening symbol of some sort
#     # Immediately return false with top of stack has closed symbol
#     # Immediately return false if end of stack has open symbol
#     # The stack should be an even lenght number
    
#     # Generalizing it for a problem were the string has letters too.

#     stack = []
#     for char in string:
#         if char in '({[':
#             # add to stack
#             stack.append(char)
#         elif char in ')}]':
#             # is stack empty?
#             if not stack:
#                 return False
#             # Does top match?
#             elif char == ')' and stack.pop() != '(':
#                 return False
#             elif char == '}' and stack.pop() != '{':
#                 return False
#             elif char == ']' and stack.pop() != '[':
#                 return False
#     # if len(stack) != 0:    # COULD be replaced with return not stack
#     #     return False          # instead of using != 0 with length
#     return not stack


# def main():
#     string = "()"
#     print(valid_parenthesis(string))

# if __name__ == '__main__':
#     main()



# from collections import deque

# def practice_queue():
#     queue = deque()
#     queue.append("A")
#     print(queue)
#     queue.append("B")
#     print(queue)
#     queue.append("C")
#     print(queue)

#     queue.popleft()
#     print(queue)
#     queue.popleft()
#     print(queue)


# def main():
#     practice_queue()

# if __name__ == '__main__':
#     main()

#####################################
# FACTORIAL
#
#####################################
# def factorial(n):
#     # base case is when we reach 0
#     if n == 0:
#         return 1
#     return n * factorial(n-1)


# def main():
#     print(factorial(4))

# if __name__ == '__main__':
#     main()

#####################################
# Sum To N
#
#####################################

# def sum_to_n(n):
#     if n == 0:
#         return 0
#     return n + sum_to_n(n-1)

# def main():
#     print(sum_to_n(4))

# if __name__ == '__main__':
#     main()


#####################################
# Node
#   manually connect 3 nodes
#   Write traversal that prints each value
#####################################

# class Node:
#     def __init__(self, node):
#         self.head = node
#         self.next = None

# node_1 = Node(17)
# node_2 = Node(20)
# node_3 = Node(30)

# node_1.next = node_2
# node_2.next = node_3

# head_node = node_1

# current = head_node

# while(current != None):
#     print(current.head)
#     current = current.next;

#####################################
# Best Time to Buy and Sell Stock
#  Wan to maximize your profit by choosing a single day to buy one stock
#       and choosing a idfferent day in the future to sell that stock.
#####################################

# INPUT: an array of prices where one element is the price of a given stock on that ith day
# OUTPUT: the maximum profit you can achieve from this transaction. If cannot achieve any profit, return 0.
# BRUTE FORCE: Go through the list while keeping track of the new smallest and new largest number where the 
#               indices of the largest number should be greater than the indices of the smaller.
# WHAT REPEATED WORK HAPPENS? Constantly checking the difference between the numbers later on in the list with the
#                           numbers later on in the list to find the profit.
# WHAT INFO ABOUT THE PAST DO I ACTUALLY NEED? Need to know the smallest number of if a high profit was found before while 
#                               continuing to check for the other differences/profits.
# WHAT STATE COULD I MAINTAIN WHILE SCANNING? Should always have the larger number be ahead of the smaller number. Otherwise, just ignore and move on.
#                   And tracking the smallest 0- (i-1) and the max profit so far.
# INVARIANT: min_price will hold the absolute lowest buying price in prices[0...n]
#            max_profit will hold the max profit achievable from any buy/sell pair chosen strictly within days 0...k
# TIME TARGET: O(n)
# SPACE TARGET: O(n)
# AUXILIARY SPACE: O(1) Because we traverse the input list only once (amount of additional memory doesn't grow with the number of prices)

def buy_and_sell_stock(int_list):
    # go through the list:
    # Note: track the smallest (0... (i-1)) number (prices[0...n])
    #       track the max profit so far so i and smallest seen so far
    #       sell day has to occur after the buy day
    if not int_list:
        return 0
    min_price = int_list[0]
    max_profit = 0
    for value in int_list:
        if value < min_price:
            min_price = value
        elif (value - min_price) > max_profit:
            max_profit = value - min_price
    return max_profit

def main():
    # Should be 7
    inp = [5, 3, 5, 7, 2, 8, 9]
    # Should be 0
    inp_2 = [9, 9, 9, 3, 3 ,3, 2]
    # Should be 3
    inp_3 = [1, 1, 1, 1, 4, 1, 1]
    # Should be 8
    inp_4 = [1, 3, 7, 2, 3, 9]
    # Should be 0 (since if we buy and sell on same day with 5, 5-5 = 0)
    inp_5 = [5] # CORRECT
    # Should be 0 since 1 comes after 5
    inp_6 = [5, 1] # CORRECT
    # Should be 3
    inp_7 = [3, 1, 4] # CORRECT
    # Should be 0
    inp_8 = []
    print(buy_and_sell_stock(inp_8))

if __name__ == '__main__':
    main()

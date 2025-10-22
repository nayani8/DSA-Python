# ----------------------------------------------------------
# Problem Title: Print Digits of a Number in Reverse Order
# ----------------------------------------------------------
# Problem Statement:
# ------------------
# Given a positive integer 'n', print all its digits in reverse order, 
# one digit per line.
#
# Example:
# Input : 12345
# Output:
# 5
# 4
# 3
# 2
# 1
#
# Approach:
# ---------
# 1. Extract the last digit using modulo operation: last_digit = num % 10
# 2. Print the last digit.
# 3. Remove the last digit from the number using integer division: num = num // 10
# 4. Repeat until the number becomes 0.
#
# Time Complexity: O(d), where d is the number of digits
# Space Complexity: O(1)
# ----------------------------------------------------------

# Input from user
n = int(input("Enter a number: "))

# Make a copy of n to process
num = n

# Loop to extract and print digits in reverse
while num > 0:
    last_digit = num % 10  # Get the last digit
    print(last_digit)       # Print the digit
    num = num // 10         # Remove the last digit

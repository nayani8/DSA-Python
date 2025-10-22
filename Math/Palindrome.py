# ----------------------------------------------------------
# Problem Title: Check if a Number is Palindrome
# ----------------------------------------------------------
# Problem Statement:
# ------------------
# Given a positive integer 'n', determine whether it is a palindrome.
# A number is a palindrome if it reads the same forwards and backwards.
#
# Example:
# Input : 12321
# Output: True
#
# Input : 12345
# Output: False
#
# Approaches:
# -----------  
# Method 1: Reverse the Number
#   - Reverse the number using a loop.
#   - Compare the reversed number with the original number.
#   - Time Complexity: O(d), d = number of digits
#   - Space Complexity: O(1)
#
# Method 2: Convert to String (Alternative Approach)
#   - Convert number to string and check if it is equal to its reverse.
#   - Time Complexity: O(d)
#   - Space Complexity: O(d)
# ----------------------------------------------------------

# -------------------- Methods --------------------

# Method 1: Using number reversal
def is_palindrome_number(n):
    num = n
    reversed_num = 0
    while num > 0:
        last_digit = num % 10
        reversed_num = (reversed_num * 10) + last_digit
        num = num // 10
    return reversed_num == n

# Method 2: Using string conversion
def is_palindrome_string(n):
    return str(n) == str(n)[::-1]

# -------------------- Input and Execution --------------------

n = int(input("Enter a number: "))

print("Palindrome check using number reversal:", is_palindrome_number(n))
print("Palindrome check using string conversion:", is_palindrome_string(n))

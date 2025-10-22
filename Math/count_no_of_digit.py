# ----------------------------------------------------------
# Problem Title: Count the Number of Digits in a Number
# ----------------------------------------------------------
# Problem Statement:
# ------------------
# Given a positive integer 'n', determine the total number of digits in it.
#
# Example:
# Input : 12345
# Output: 5
#
# Approaches:
# -----------  
# Method 1: Using While Loop (Direct Approach)
#   - Initialize count = 0
#   - While number > 0:
#       - Remove last digit: num = num // 10
#       - Increment count
#   - Time Complexity: O(log10(n))
#   - Space Complexity: O(1)
#
# Method 2: Using Logarithm (Mathematical Approach)
#   - Use formula: digits = int(log10(n)) + 1
#   - Time Complexity: O(1)
#   - Space Complexity: O(1)
# ----------------------------------------------------------

from math import log10

# -------------------- Methods --------------------

# Method 1: Using While Loop
def count_digits_loop(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count

# Method 2: Using Logarithm
def count_digits_log(num):
    if num == 0:  # Edge case for 0
        return 1
    return int(log10(num)) + 1

# -------------------- Input and Execution --------------------

n = int(input("Enter a number: "))

print("Number of digits using loop:", count_digits_loop(n))
print("Number of digits using logarithm:", count_digits_log(n))



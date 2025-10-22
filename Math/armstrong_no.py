# ----------------------------------------------------------
# Problem Title: Check if a Number is an Armstrong Number
# ----------------------------------------------------------
# Problem Statement:
# ------------------
# Given a positive integer 'n', determine whether it is an Armstrong number.
# An Armstrong number is a number that is equal to the sum of its digits
# each raised to the power of the number of digits.
#
# Example:
# Input : 153
# Output: True  (1^3 + 5^3 + 3^3 = 153)
#
# Input : 123
# Output: False
#
# Approaches:
# -----------  
# Method 1: Using Loop and Math
#   - Count the number of digits using log10 or iterative approach.
#   - Sum each digit raised to the power of total digits.
#   - Compare sum with original number.
#   - Time Complexity: O(d), d = number of digits
#   - Space Complexity: O(1)
#
# Method 2: Using String Conversion (Alternative)
#   - Convert number to string, iterate over digits, raise each to the power of total digits, sum them.
#   - Compare sum with original number.
# ----------------------------------------------------------

from math import log10

# -------------------- Methods --------------------

# Method 1: Using loop and math
def is_armstrong_number(n):
    if n == 0:  # Edge case
        return True
    num = n
    sum_of_powers = 0
    digits = int(log10(num)) + 1  # Count number of digits
    while num > 0:
        last_digit = num % 10
        sum_of_powers += last_digit ** digits
        num = num // 10
    return sum_of_powers == n

# Method 2: Using string conversion
def is_armstrong_string(n):
    num_str = str(n)
    digits = len(num_str)
    sum_of_powers = sum(int(digit) ** digits for digit in num_str)
    return sum_of_powers == n

# -------------------- Input and Execution --------------------

n = int(input("Enter a number: "))

print("Armstrong check using math:", is_armstrong_number(n))
print("Armstrong check using string conversion:", is_armstrong_string(n))

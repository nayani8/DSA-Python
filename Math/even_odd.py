# ----------------------------------------------------------
# Problem Title: Check Even or Odd using Bitwise Operator
# ----------------------------------------------------------
# Problem Statement:
# ------------------
# Given an integer 'n', determine whether it is even or odd
# using bitwise operations (without using modulus '%').
#
# Example:
# Input  : 6
# Output : True  (6 is even)
#
# Input  : 7
# Output : False (7 is odd)
#
# Approach:
# ---------
# 1. Use bitwise AND operation (&) with 1.
# 2. If the last bit is 0 → number is even.
# 3. If the last bit is 1 → number is odd.
#
# Time Complexity: O(1)
# Space Complexity: O(1)
# ----------------------------------------------------------

def isEven(n):
    if (n & 1) == 0:
        return True
    else:
        return False

# Input number
n = int(input("Enter a number: "))
print(isEven(n))

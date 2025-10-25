# ----------------------------------------------------------
# Problem Title: Reverse a Number
# ----------------------------------------------------------
# Problem Statement:
# ------------------
# Given a positive integer 'n', reverse its digits.
#
# Example:
# Input  : 12345
# Output : 54321
#
# Approach:
# ---------
# 1. Initialize 'reverse' to 0.
# 2. Extract last digit using modulo: last_digit = num % 10.
# 3. Update reverse: reverse = (reverse * 10) + last_digit.
# 4. Remove last digit: num = num // 10.
# 5. Repeat until num becomes 0.
#
# Time Complexity: O(d), where d is the number of digits
# Space Complexity: O(1)
# ----------------------------------------------------------

def reverse_number(n):
    num = n
    reverse = 0
    while num > 0:
        last_digit = num % 10
        reverse = (reverse * 10) + last_digit
        num = num // 10
    return reverse

# -------------------- Example --------------------
n = int(input("Enter a number: "))
print("Reversed Number:", reverse_number(n))

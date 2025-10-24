# ----------------------------------------------------------
# Problem Title: Decimal to Binary Conversion
# ----------------------------------------------------------
# Problem Statement:
# ------------------
# Given a positive integer 'n', convert it to its binary
# representation (without using built-in bin() function).
#
# Example:
# Input  : 13
# Output : 1101
#
# Approach:
# ---------
# 1. Use division by 2 method.
# 2. Store the remainder (num % 2) multiplied by the current power of 10.
# 3. Divide the number by 2 and repeat until it becomes 0.
# 4. The result forms the binary equivalent.
#
# Time Complexity: O(log₂n)
# Space Complexity: O(1)
# ----------------------------------------------------------

def decNum(num):
    ans = 0
    power = 1
    while num > 0:
        rem = num % 2            # Get remainder (0 or 1)
        num = num // 2           # Divide number by 2
        ans += rem * power       # Add remainder * place value
        power *= 10              # Move to next binary digit
    return ans

# Input number
n = int(input("Enter a number: "))
print(decNum(n))

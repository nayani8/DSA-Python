# ----------------------------------------------------------
# Problem Title: Binary to Decimal Conversion
# ----------------------------------------------------------
# Problem Statement:
# ------------------
# Convert a binary number (given as integer input) into its 
# equivalent decimal number without using built-in functions.
#
# Example:
# Input  : 1011
# Output : 11
#
# Approach:
# ---------
# 1. Initialize result (ans) = 0 and power = 1 (for 2^0).
# 2. Extract each binary digit from right to left using modulo (% 10).
# 3. Multiply digit by its power of 2 and add to result.
# 4. Update power *= 2 and remove last digit (num //= 10).
# 5. Continue until num becomes 0.
#
# Time Complexity: O(log₁₀(n))
# Space Complexity: O(1)
# ----------------------------------------------------------

def binNum(num):
    ans = 0
    pow = 1
    while num > 0:
        rem = num % 10         # Extract last binary digit
        ans += (rem * pow)     # Add its decimal value
        num //= 10             # Remove last digit
        pow *= 2               # Increase power of 2
    return ans

# Input from user
n = int(input("Enter a binary number: "))
print(binNum(n))

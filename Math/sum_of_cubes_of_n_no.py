# ----------------------------------------------------------
# Problem Title: Sum of Cubes of First n Natural Numbers
# ----------------------------------------------------------
# Problem Statement:
# ------------------
# Given a positive integer 'n', calculate the sum of cubes of 
# the first n natural numbers using recursion.
#
# Example:
# Input  : 5
# Output : 225 (1^3 + 2^3 + 3^3 + 4^3 + 5^3)
#
# Approach:
# ---------
# 1. Base Case: If n == 1, return 1.
# 2. Recursive Case: sum_cubes(n) = n^3 + sum_cubes(n-1)
#
# Time Complexity: O(n)
# Space Complexity: O(n) due to recursion stack
# ----------------------------------------------------------

def sum_of_cubes(n):
    if n == 1:
        return 1
    return n**3 + sum_of_cubes(n-1)

# -------------------- Example --------------------
n = 5
print(f"Sum of cubes of first {n} natural numbers:", sum_of_cubes(n))

# ----------------------------------------------------------
# Problem Title: Find All Factors of a Number
# ----------------------------------------------------------
# Problem Statement:
# ------------------
# Given a positive integer 'n', find all its factors (divisors).
# A factor of a number is an integer that divides the number exactly.
#
# Example:
# Input : 12
# Output: [1, 2, 3, 4, 6, 12]
#
# Approaches:
# -----------  
# Method 1: Brute Force
#   - Check all numbers from 1 to n. If n % i == 0, add i to the result.
#   - Time Complexity: O(n)
#   - Space Complexity: O(d), d = number of divisors
#
# Method 2: Better Approach
#   - Check all numbers from 1 to n//2 and add n itself at the end.
#   - Time Complexity: O(n/2) ≈ O(n)
#   - Space Complexity: O(d)
#
# Method 3: Optimal using Square Root
#   - Iterate from 1 to sqrt(n)
#   - If i divides n, add both i and n//i
#   - Sort the result to get factors in order
#   - Time Complexity: O(sqrt(n))
#   - Space Complexity: O(d)
# ----------------------------------------------------------

from math import sqrt

# -------------------- Methods --------------------

# Method 1: Brute Force
def factors_brute(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
    return result

# Method 2: Better Approach
def factors_better(num):
    result = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            result.append(i)
    result.append(num)
    return result

# Method 3: Optimal using Square Root
def factors_optimal(num):
    result = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            result.append(i)
            if (num // i != i):  # Avoid duplicate for perfect square
                result.append(num // i)
    return sorted(result)

# -------------------- Input and Execution --------------------

n = int(input("Enter a number: "))

print("Factors using brute force:", factors_brute(n))
print("Factors using better approach:", factors_better(n))
print("Factors using optimal approach:", factors_optimal(n))

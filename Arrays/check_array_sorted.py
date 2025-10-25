# ----------------------------------------------------------
# Problem Title: Check if Array is Sorted
# ----------------------------------------------------------
# Problem Statement:
# ------------------
# Given an array 'nums' of size 'n', check whether the array 
# elements are sorted in non-decreasing (ascending) order.
#
# Example:
# Input  : [3, 5, 6, 8, 9, 10]
# Output : True
#
# Input  : [3, 5, 6, 8, 9, 2, 10]
# Output : False
#
# Approach:
# ---------
# 1. Iterate through the array from index 0 to n-2.
# 2. Compare each element with the next one.
# 3. If any element is greater than its next, return False.
# 4. If loop completes, array is sorted → return True.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ----------------------------------------------------------

def check_array(nums, n):
    for i in range(0, n - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

# Input array
nums = [3, 5, 6, 8, 9, 2, 10, 11, 12, 20]
n = len(nums)

print(check_array(nums, n))

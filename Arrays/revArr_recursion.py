# ----------------------------------------------------------
# Problem Title: Reverse a Subarray using Recursion
# ----------------------------------------------------------
# Problem Statement:
# ------------------
# Given an array 'arr' and indices 'l' and 'r', reverse the 
# elements of the array from index l to r using recursion.
#
# Example:
# Input  : arr = [5, 7, 3, 2, 6, 1, 5, 9], l = 2, r = 4
# Output : [5, 7, 6, 2, 3, 1, 5, 9]
#
# Approach:
# ---------
# 1. Use a helper recursive function:
#    - Swap arr[l] and arr[r].
#    - Recur with l+1 and r-1 until l >= r.
# 2. Return the modified array.
#
# Time Complexity: O(r - l + 1)
# Space Complexity: O(r - l + 1) due to recursion stack
# ----------------------------------------------------------

def reverse_subarray_recursive(arr, l, r):
    if l >= r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    reverse_subarray_recursive(arr, l + 1, r - 1)

def rev_subarray(arr, l, r):
    reverse_subarray_recursive(arr, l, r)
    return arr

# -------------------- Example --------------------
arr = [5, 7, 3, 2, 6, 1, 5, 9]
l, r = 2, 4

print("Original Array:", arr)
rev_subarray(arr, l, r)
print("Array after reversing subarray:", arr)

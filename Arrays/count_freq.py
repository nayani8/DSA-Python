# ----------------------------------------------------------
# Problem Title: Count Frequency of Each Element in an Array
# ----------------------------------------------------------
# Problem Statement:
# ------------------
# Given an array 'nums', count the frequency of each unique element 
# and store the results in a dictionary where:
#   - Key   → Element
#   - Value → Frequency of that element
#
# Example:
# Input : [5, 6, 7, 7, 1, 9, 1, 1, 7, 7, 9, 5, 1, 1]
# Output: {5: 2, 6: 1, 7: 4, 1: 5, 9: 2}
#
# Approaches:
# -----------  
# Method 1: Brute Force (Using Loop)
#   - Traverse the array and manually count frequencies using a dictionary.
#   - Recreate freq_map for every element (inefficient).
#   - Time Complexity: O(n^2)
#   - Space Complexity: O(n)
#
# Method 2: Optimal (Using Hash Map)
#   - Use a single dictionary and update counts efficiently.
#   - Time Complexity: O(n)
#   - Space Complexity: O(n)
# ----------------------------------------------------------

# -------------------- Methods --------------------

# Method 1: Brute Force (Inefficient)
def frequency_brute(nums, n):
    freq_map = {}
    for i in range(0, n):
        count = 0
        for j in range(0, n):
            if nums[i] == nums[j]:
                count += 1
        freq_map[nums[i]] = count
    return freq_map

# Method 2: Optimal using Hash Map
def frequency_optimal(nums, n):
    hash_map = {}
    for i in range(0, n):
        hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
    return hash_map

# -------------------- Input and Execution --------------------

nums = [5, 6, 7, 7, 1, 9, 1, 1, 7, 7, 9, 5, 1, 1]
n = len(nums)

# Uncomment to test brute force
print("Frequencies (Brute Force):", frequency_brute(nums, n))
print("Frequencies (Optimal):", frequency_optimal(nums, n))

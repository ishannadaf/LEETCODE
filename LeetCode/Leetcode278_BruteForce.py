"""

278. First Bad Version (Brute Force)
You are a product manager and currently leading a team to develop a new product. Unfortunately, 
the latest version of your product fails the quality check. Since each version is developed based on the previous version,
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation: call isBadVersion(3) -> false
call isBadVersion(5) -> true

Example 2:
Input: n = 1, bad = 1
Output: 1
Explanation: call isBadVersion(1) -> true

"""

def isBadVersion(version):
    # This is a placeholder for the actual implementation of the API.
    # In a real scenario, this function would be provided and would return whether the given version is bad.
    pass

def firstBadVersion(n):
    for i in range(1, n + 1):
        if isBadVersion(i):
            return i
        
# Time Complexity: O(n) since we may have to check each version in the worst case
# Space Complexity: O(1) since we are not using any extra space

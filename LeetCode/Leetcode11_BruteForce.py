"""

11. Container With Most Water - Brute Force Solution
You are given an integer array height of length n. There are n vertical lines drawn such that
the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains
the most water.
Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Example 2:
Input: height = [1,1]
Output: 1

"""


def trap(height):
    n = len(height)
    water = 0

    for i in range(n):
        left_max = max(height[:i+1])
        right_max = max(height[i:])

        water += min(left_max, right_max) - height[i]

    return water


# Time Complexity: O(n^2) - We have a nested loop where the outer loop runs n times and
# the inner loop (max function) also runs up to n times in the worst case.
# Space Complexity: O(1) - We are using only a constant amount of extra space 
# for the water variable and the left_max and right_max variables.


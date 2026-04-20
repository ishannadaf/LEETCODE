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

    left_max = [0]*n
    right_max = [0]*n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])

    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])

    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]

    return water


# Time Complexity: O(n) - We have three separate loops that each run n times.
# Space Complexity: O(n) - We are using two additional arrays of size n to store the left and right maximum heights.
# for the water variable and the left_max and right_max variables.


# Space Optimized Solution (IMPORTANT)
# We can optimize the space by using two pointers instead of the left_max and right_max arrays

def trap(height):
    l, r = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0

    while l < r:
        if height[l] < height[r]:
            if height[l] >= left_max:
                left_max = height[l]
            else:
                water += left_max - height[l]
            l += 1
        else:
            if height[r] >= right_max:
                right_max = height[r]
            else:
                water += right_max - height[r]
            r -= 1

    return water


# Time Complexity: O(n) - We have a single loop that runs until the two pointers meet.
# Space Complexity: O(1) - We are using only a constant amount of extra space 
# for the pointers and temporary variables, regardless of the input size.


"""

🔥 Key Concept (VERY IMPORTANT)

👉 At any point:

Water depends on smaller side

So:

If left < right → process left
Else → process right
🧠 Interview Explanation (IMPORTANT)

👉 “We move the side which has smaller height because water is limited by the smaller boundary.”

⚠️ Common Mistakes
Not understanding why we move smaller side ❌
Wrong condition inside loop
Negative water addition

"""
"""

739. Daily Temperatures - Brute Force Solution
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after 
the ith day to get a warmer temperature. If there is no future day for which this is possible, 
keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

"""

def dailyTemperatures(temperatures):
    n = len(temperatures)
    res = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            if temperatures[j] > temperatures[i]:
                res[i] = j - i
                break

    return res

print(dailyTemperatures([73,74,75,71,69,72,76,73]))  # Output: [1,1,4,2,1,1,0,0]

# Time Complexity: O(n^2) - We have a nested loop where the outer loop runs n times and the inner 
# loop can run up to n times in the worst case.
# Space Complexity: O(n) - We are storing the result in a new list that takes O(n) space.
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

"""

def dailyTemperatures(temperatures):
    n = len(temperatures)
    res = [0] * n
    stack = []  # stores indices

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev = stack.pop()
            res[prev] = i - prev
        stack.append(i)

    return res

print(dailyTemperatures([73,74,75,71,69,72,76,73]))  # Output: [1,1,4,2,1,1,0,0]

# Time Complexity: O(n) - Each element is pushed and popped at most once.
# Space Complexity: O(n) - In the worst case, the stack can hold all indices 
# if the temperatures are in decreasing order.


"""



"""
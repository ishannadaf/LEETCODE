"""

56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]


🧠 Key Idea 🔥

👉 Overlap condition:

if current.start <= previous.end → overlap
🧠 Approach 1 — Brute Force (Inefficient Merge)
💡 Idea
Compare each interval with others
Merge repeatedly

❌ Too messy and inefficient (O(n²))

"""

# Brute Force (Inefficient Merge)
def merge(intervals):
    n = len(intervals)
    merged = [False] * n
    result = []
    
    for i in range(n):
        if merged[i]:
            continue
        
        start, end = intervals[i]
        
        for j in range(i + 1, n):
            if merged[j]:
                continue
            
            s2, e2 = intervals[j]
            
            # check overlap
            if max(start, s2) <= min(end, e2):
                start = min(start, s2)
                end = max(end, e2)
                merged[j] = True
        
        result.append([start, end])
    
    return result

# Time Complexity: O(n^2) where n is the number of intervals (due to nested loops)
# Space Complexity: O(n) in the worst case if all intervals are non-overlapping 
# (due to the result list storing all intervals)


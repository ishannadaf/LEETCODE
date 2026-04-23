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


💡 Core Insight

👉 If intervals are sorted by start:

You only need to compare with last merged interval
🧠 Steps
Sort intervals by start
Initialize result list
Iterate:
If overlap → merge
Else → add new interval

"""

# Optimized Solution
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged


# Time Complexity: O(n log n) due to sorting, where n is the number of intervals
# Space Complexity: O(n) in the worst case if all intervals are non-overlapping 
# (due to the merged list storing all intervals)



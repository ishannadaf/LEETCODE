"""

347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

"""

from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    return [x for x, _ in sorted(count.items(), key=lambda x: x[1], reverse=True)[:k]]

print(topKFrequent([1,1,1,2,2,3], 2))  # Output: [1, 2]
print(topKFrequent([1], 1))  # Output: [1]



# Time Complexity: O(n log n) - Sorting the items of the counter takes O(n log n) time, 
# where n is the number of unique elements in nums.

# Space Complexity: O(n) - We are storing the count of each unique element in the counter,
# which takes O(n) space in the worst case when all elements are unique.

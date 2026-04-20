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

#Bucket Sort Solution

from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    freq = [[] for _ in range(len(nums) + 1)]

    for num, c in count.items():
        freq[c].append(num)

    result = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            result.append(num)
            if len(result) == k:
                return result



# Time Complexity: O(n) - We iterate through the nums array once to build the frequency list, and then iterate through the frequency list to collect the top k elements.

# Space Complexity: O(n) - We are storing the count of each unique element in the counter,
# which takes O(n) space in the worst case when all elements are unique.


"""

🔥 Key Concept
📊 Frequency → Bucket Mapping

Instead of sorting:
👉 Use index as frequency

⚠️ Common Mistakes
Using full sort unnecessarily
Confusing heap min/max
Forgetting heap size control

🧪 Variations (VERY IMPORTANT)
Top K frequent words
K closest points
K largest/smallest elements
Streaming data (hard)
🧠 Pattern Summary So Far

You now know:

HashMap → frequency
Heap → top k
Bucket → optimize sorting

👉 This combo appears A LOT in interviews.

"""
"""

438. Find All Anagrams in a String
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order. 

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]


💡 Intuition (VERY IMPORTANT 🔥)

👉 Same as LeetCode 567, but:

Instead of returning True
We collect all matching indices
🔥 Key Idea:
Fixed window size = len(p)
Maintain frequency count
If match → store index

"""

from collections import Counter

def findAnagrams(s, p):
    res = []
    k = len(p)

    p_count = Counter(p)
    window_count = Counter()

    for i in range(len(s)):
        window_count[s[i]] += 1

        # maintain window size
        if i >= k:
            if window_count[s[i - k]] == 1:
                del window_count[s[i - k]]
            else:
                window_count[s[i - k]] -= 1

        if window_count == p_count:
            res.append(i - k + 1)

    return res

print(findAnagrams("cbaebabacd", "abc"))  # Output: [0, 6]
# Time Complexity: O(n * k log k) where n is the length of string s and k is the length of 
# string p (due to sorting each substring)
# Space Complexity: O(k) for storing the sorted version of p and the substring during comparison
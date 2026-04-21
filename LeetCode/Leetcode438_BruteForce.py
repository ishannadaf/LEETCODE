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


💡 Idea:
Generate all substrings of size len(p)
Sort each substring
Compare with sorted p

"""

def findAnagrams(s, p):
    res = []
    k = len(p)
    p_sorted = sorted(p)

    for i in range(len(s) - k + 1):
        substring = s[i:i+k]
        if sorted(substring) == p_sorted:
            res.append(i)

    return res

print(findAnagrams("cbaebabacd", "abc"))  # Output: [0, 6]
# Time Complexity: O(n * k log k) where n is the length of string s and k is the length of 
# string p (due to sorting each substring)
# Space Complexity: O(k) for storing the sorted version of p and the substring during comparison
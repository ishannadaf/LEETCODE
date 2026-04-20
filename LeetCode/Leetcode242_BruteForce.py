"""

242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false

"""

def isAnagram(s, t):
    return sorted(s) == sorted(t)


# Time Complexity: O(n log n) - Sorting both strings takes O(n log n) time, 
# where n is the length of the strings.

# Space Complexity: O(1) - We are sorting the strings in place and using only a
# constant amount of extra space for the sorted lists.

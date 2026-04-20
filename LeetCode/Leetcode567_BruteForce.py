"""

567. Permutation in String - Brute Force Solution
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

"""

from collections import Counter

def checkInclusion(s1, s2):
    n, m = len(s1), len(s2)

    for i in range(m - n + 1):
        substring = s2[i:i+n]

        if Counter(substring) == Counter(s1):
            return True

    return False


# Time Complexity: O(m * n) - We are iterating through the string s2 with a window of size n, 
# and for each window, we are counting the frequency of characters which takes O(n) time.
# Space Complexity: O(1) - We are using a fixed-size counter for the characters 
# in s1 and the current substring, which takes O(1) space since there are only 26 lowercase English letters.


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
    if len(s) != len(t):
        return False

    count = {}

    for c in s:
        count[c] = count.get(c, 0) + 1

    for c in t:
        if c not in count:
            return False
        count[c] -= 1
        if count[c] == 0:
            del count[c]

    return len(count) == 0


# Time Complexity: O(n) - We iterate through both strings once, 
# and each dictionary operation takes O(1) time.
# Space Complexity: O(k) - Where k is the number of unique characters in the strings, 
# as we store the character counts in a dictionary.


"""

⚠️ Common Mistakes
Forgetting length check ❌
Not handling missing characters
Using sorting without knowing optimal

🧪 Variations (VERY IMPORTANT)
Group Anagrams → next level
Find all anagrams in string
Check if permutation exists

"""
"""

125. Valid Palindrome
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: s = "race a car"
Output: false

"""

def isPalindrome(s):
    cleaned = ""

    for c in s:
        if c.isalnum():
            cleaned += c.lower()

    return cleaned == cleaned[::-1]


# Time Complexity: O(n) - We iterate through the string once to clean it, and then we check if 
# it's a palindrome, which also takes O(n) time.
# Space Complexity: O(n) - We create a new string cleaned that can take up to O(n) space in the worst case when all characters are alphanumeric.


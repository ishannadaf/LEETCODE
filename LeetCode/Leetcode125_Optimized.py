"""

125. Valid Palindrome
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: s = "race a car"
Output: false



👉 Use two pointers:

Left → start
Right → end

Move inward while checking for alphanumeric and comparing characters in a case-insensitive manner.

"""

def isPalindrome(s):
    l = 0
    r = len(s) - 1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True

# Time Complexity: O(n) - We traverse the string once with two pointers, 
# where n is the length of the string.
# Space Complexity: O(1) - We are using only a constant amount of extra space for the pointers and 
# temporary variables, regardless of the input size.

"""

🔥 Key Concept
👈👉 Two Pointers (Opposite Direction)

Used when:

Comparing ends
Sorted arrays
Palindromes

⚠️ Common Mistakes
Not skipping special characters ❌
Case sensitivity issues
Using extra space unnecessarily

"""
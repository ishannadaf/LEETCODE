"""

3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1

Example 3:
Input: s = "pwwkew"
Output: 3

"""


def lengthOfLongestSubstring(s):
    n = len(s)
    max_len = 0

    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)

    return max_len


print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3

# Time Complexity: O(n^2) - We have a nested loop where the outer loop runs n times and 
# the inner loop can run up to n times in the worst case.
# Space Complexity: O(min(m, n)) - We are using a set to store the characters in the current 
# substring, where m is the size of the character set and n is the length of the string. In the worst case, the set can grow to the size of the smaller of these two values.



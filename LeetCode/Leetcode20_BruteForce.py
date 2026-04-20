"""

20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

"""

def isValid(s):
    prev = None
    while prev != s:
        prev = s
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    return s == ""


# Time Complexity: O(n^2) - In the worst case, we might have to scan the string multiple times to 
# remove all pairs of parentheses, leading to O(n) for each scan and O(n) scans in the worst case.
# Space Complexity: O(n) - We are creating new strings during the replacement process, 
# which can take up to O(n) space in the worst case when the string is large and contains many parentheses.

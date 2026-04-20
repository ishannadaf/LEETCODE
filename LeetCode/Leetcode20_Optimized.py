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
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)

    return len(stack) == 0

print(isValid("()[]{}"))    # Output: true

# Time Complexity: O(n) - We iterate through the string once, and each operation on the stack takes 
# constant time.
# Space Complexity: O(n) - In the worst case, the stack can contain all characters of the string 
# if they are all opening brackets.



"""
1047. Remove All Adjacent Duplicates In String
Given a string s, a duplicate removal consists of choosing two adjacent and equal letters and removing them.
We repeatedly make duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It can be proven that
the answer is unique.

Example 1:
Input: s = "abbaca"
Output: "ca"

Example 2:
Input: s = "azxxzy"
Output: "ay"
"""

def removeDuplicates(s):
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    return "".join(stack)

print(removeDuplicates("abbaca"))  # Output: "ca"


# Time Complexity: O(n), where n is the length of the string. We traverse the string once.
# Space Complexity: O(n) in the worst case, if there are no duplicates and 
# we store all characters in the stack.

"""

💡 Intuition

👉 If current character == top of stack → remove it
👉 Else → push it

This automatically handles repeated removals in one pass

🔥 Key Idea:
Stack keeps final valid characters
Duplicate cancels previous one

⚡ Key Insight

Stack helps simulate “undo operation”

👉 Pattern:

Adjacent removal
Cancel effect
→ Use stack

"""
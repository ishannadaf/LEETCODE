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
    changed = True

    while changed:
        changed = False
        i = 0
        new_s = ""

        while i < len(s):
            if i < len(s) - 1 and s[i] == s[i + 1]:
                changed = True
                i += 2
            else:
                new_s += s[i]
                i += 1

        s = new_s

    return s

print(removeDuplicates("abbaca"))  # Output: "ca"


# Time Complexity: O(n^2) in the worst case, where n is the length of the string. 
# This happens when there are many adjacent duplicates.
# Space Complexity: O(n) for the new string created during each iteration.
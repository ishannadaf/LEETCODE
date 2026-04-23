"""

76. Minimum Window Substring
Given two strings s and t, return the minimum window in s which will contain all the characters in t. 
If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only 
one unique minimum window in s.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.


🧠 Why This is Hard ⚠️

👉 Unlike normal sliding window:

You must track exact character frequency
You must know when window is valid
You must shrink only when valid
🧠 Approach 1 — Brute Force (O(n³))
💡 Idea
Generate all substrings
Check if valid
Track minimum


"""

def minWindow(s, t):
    from collections import Counter
    
    def is_valid(sub, t_count):
        sub_count = Counter(sub)
        for c in t_count:
            if sub_count[c] < t_count[c]:
                return False
        return True
    
    t_count = Counter(t)
    min_len = float('inf')
    res = ""
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j+1]
            if is_valid(sub, t_count):
                if len(sub) < min_len:
                    min_len = len(sub)
                    res = sub
    
    return res


# Time Complexity: O(n^3) - due to the nested loops and the validation function
# Space Complexity: O(m) - where m is the length of string t for the counter
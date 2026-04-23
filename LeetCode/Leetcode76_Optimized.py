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


🚀 Approach 2 — Optimal (Sliding Window + HashMap)
💡 Key Insight 🔥

👉 Maintain:

need → frequency of t
window → current window freq
have → how many chars satisfied
need_count → total unique chars needed
🧠 Core Idea
Expand right → build valid window
Once valid → shrink from left
Track minimum

"""

from collections import Counter

def minWindow(s, t):
    if not t:
        return ""
    
    need = Counter(t)
    window = {}
    
    have = 0
    need_count = len(need)
    
    res = [-1, -1]
    res_len = float('inf')
    
    l = 0
    
    for r in range(len(s)):
        c = s[r]
        window[c] = window.get(c, 0) + 1
        
        if c in need and window[c] == need[c]:
            have += 1
        
        # shrink window
        while have == need_count:
            # update result
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = r - l + 1
            
            # remove from left
            window[s[l]] -= 1
            if s[l] in need and window[s[l]] < need[s[l]]:
                have -= 1
            
            l += 1
    
    l, r = res
    return s[l:r+1] if res_len != float('inf') else ""

# Time Complexity: O(n) - each element is visited at most twice
# Space Complexity: O(m) - where m is the length of string t for the counter

1,3,11,15,20,33,36,49,56,71,73,76,121,125,152,153,155,167,169,209,217,225,232,238,242,347,424,438,560,567,643,739,904,974,1004,1047
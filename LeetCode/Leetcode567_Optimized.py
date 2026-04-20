"""

567. Permutation in String - Brute Force Solution
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

"""

def checkInclusion(s1, s2):
    from collections import Counter

    n = len(s1)
    count1 = Counter(s1)
    window = Counter()

    for i in range(len(s2)):
        # add current char
        window[s2[i]] += 1

        # remove char if window too big
        if i >= n:
            if window[s2[i - n]] == 1:
                del window[s2[i - n]]
            else:
                window[s2[i - n]] -= 1

        # compare window with s1
        if window == count1:
            return True

    return False


# Time Complexity: O(n) - We are iterating through the string s2 once, and each operation on 
# the Counter takes O(1) time on average.
# Space Complexity: O(1) - We are using a fixed-size Counter for the characters in s1 and the 
# current window, which takes O(1) space since there are only 26 lowercase English letters.

"""

🔥 Key Concept
🧠 Fixed Sliding Window

👉 Size never changes
👉 Only moves forward

⚠️ Common Mistakes
Not removing old character ❌
Comparing full Counter inefficiently (still acceptable)
Window size mismatch
🧠 Optimization (Advanced)

Instead of comparing full hashmap:

👉 Track matches count (26 chars) → faster

(We’ll do this later if needed)

🧠 Pattern Summary

You now know:

Variable window → longest substring
Variable window + condition → character replacement
Fixed window → permutation check

👉 This is full sliding window foundation


"""
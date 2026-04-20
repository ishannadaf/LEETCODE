"""

424. Longest Repeating Character Replacement
Given a string s that consists of only uppercase English letters, you can perform at most k 
operations on that string. In one operation, you can choose any character of the string and 
change it to any other uppercase English character. Find the length of the longest sub-string 
containing all repeating letters you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA". 
The substring "BBBB" has the longest repeating letters, which is 4.

"""

def characterReplacement(s, k):
    count = {}
    l = 0
    max_freq = 0
    max_len = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        max_freq = max(max_freq, count[s[r]])

        window_size = r - l + 1

        # if invalid window → shrink
        if window_size - max_freq > k:
            count[s[l]] -= 1
            l += 1

        max_len = max(max_len, r - l + 1)

    return max_len


# Time Complexity: O(n) - We are using a sliding window approach where each element is visited at most twice.
# Space Complexity: O(1) - We are using a fixed-size dictionary to count the frequency of characters, 
# which takes O(1) space since there are only 26 uppercase English letters.

"""

🔥 Key Concept (VERY IMPORTANT)
🧠 “Keep window valid using most frequent char”

👉 Instead of checking all chars:
We only track:

max_freq = frequency of most common char
⚠️ Important Trick

👉 We do NOT decrease max_freq when shrinking

This feels wrong, but works.

Why?

Because we only care about max window size
Slight overestimation doesn't break correctness
🧪 Dry Run
s = "AABABBA", k = 1

Window grows:

A → AA → AAB → AABA ✔

Then shrink when needed

Final answer = 4

⚠️ Common Mistakes
Recomputing max_freq every time ❌
Shrinking with while instead of if (can still work but slower)
Misunderstanding condition
🧠 Pattern Insight

👉 This is advanced sliding window

Instead of:

“no duplicates”

We now allow:

“limited invalidity (k changes)”


"""
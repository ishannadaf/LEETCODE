from collections import Counter

def minWindow(s: str, t: str) -> str:
    if not t or not s:
        return ""
    
    count_t = Counter(t)
    min_len = float('inf')
    result = ""
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if all(substring.count(c) >= cnt for c, cnt in count_t.items()):
                if len(substring) < min_len:
                    min_len = len(substring)
                    result = substring
    
    return result

# Test cases
print(minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(minWindow("a", "a"))  # Output: "a"
print(minWindow("a", "aa"))  # Output: ""

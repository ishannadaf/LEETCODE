
"""

49 : Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

"""


from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        count = [0] * 26

        for c in word:
            count[ord(c) - ord('a')] += 1

        key = tuple(count)
        groups[key].append(word)

    return list(groups.values())


def groupAnagrams(strs):
    strs_table = {}

    for string in strs:
        sorted_string = ''.join(sorted(string))

        if sorted_string not in strs_table:
            strs_table[sorted_string] = []

        strs_table[sorted_string].append(string)

    return list(strs_table.values())


# Time Complexity: O(n k) - Where n is the number of strings and k is the maximum length of a string.
# We iterate through each string once, and counting characters takes O(k) time.
# Space Complexity: O(n k) - In the worst case, all strings are anagrams of each other,
# and we store all n strings in the groups dictionary, which takes O(n k) space.
# Additionally, the keys in the dictionary also take O(n k) space in the worst case.


"""

🧠 “Create a Signature”

Every group problem =

👉 Convert input → unique key
👉 Store in hashmap

⚠️ Common Mistakes
Using list as key (not hashable) ❌
Forgetting to convert to tuple
Not understanding why grouping works
🧪 Variations (VERY IMPORTANT)

These are frequently asked:

Count number of anagram groups
Find largest anagram group
Group words ignoring case
Group by custom rules
🧠 Pattern Evolution (Important)

See your growth:

Two Sum → find pair
Contains Duplicate → detect repeat
Valid Anagram → compare frequency
Group Anagrams → group by pattern

👉 This is how interview questions evolve.

"""

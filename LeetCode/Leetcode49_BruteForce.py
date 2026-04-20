
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
        key = "".join(sorted(word))
        groups[key].append(word)

    return list(groups.values())


# Time Complexity: O(n k log k) - Where n is the number of strings and k is the maximum length of a string.
# Sorting each string takes O(k log k) time, and we do this for all n strings.
# Space Complexity: O(n k) - In the worst case, all strings are anagrams
# of each other, and we store all n strings in the groups dictionary,
# which takes O(n k) space. Additionally, the keys in the dictionary also take O(n k) space in the worst case.


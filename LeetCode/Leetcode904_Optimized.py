"""

904. Fruit Into Baskets
You are visiting a farm that has a single row of fruit trees arranged from left to right. 
The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith 
tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that 
you must follow:
- You only have two baskets, and each basket can only hold a single type of fruit.
- Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
- Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2]. If we had started at the first tree, 
we would only pick from trees [0,1].


💡 Intuition (VERY IMPORTANT 🔥)

👉 This is:

Longest subarray with at most 2 distinct elements

🔥 Key Idea:
Use sliding window
Maintain frequency map
If distinct > 2 → shrink window

"""


from collections import defaultdict

def totalFruit(fruits):
    left = 0
    count = defaultdict(int)
    max_len = 0

    for right in range(len(fruits)):
        count[fruits[right]] += 1

        while len(count) > 2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


# Time Complexity: O(n^2) where n is the length of the input array fruits (due to nested loops)
# Space Complexity: O(1) since we are using only a constant amount of extra space


"""

⚡ Key Insight (VERY IMPORTANT)

When you see:

“At most K distinct elements”
👉 Use:
Sliding window + hashmap
Shrink when condition breaks

"""
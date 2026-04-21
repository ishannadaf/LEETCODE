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


💡 Idea:
Generate all subarrays
Count distinct fruit types
If ≤ 2 → valid
Track max length


"""


def totalFruit(fruits):
    n = len(fruits)
    max_len = 0

    for i in range(n):
        basket = set()
        for j in range(i, n):
            basket.add(fruits[j])
            if len(basket) > 2:
                break
            max_len = max(max_len, j - i + 1)

    return max_len


# Time Complexity: O(n^2) where n is the length of the input array fruits (due to nested loops)
# Space Complexity: O(1) since we are using only a constant amount of extra space
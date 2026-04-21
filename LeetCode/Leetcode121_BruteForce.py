"""

121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

💡 Idea
👉 Brute Force: Check all pairs of buy/sell days
Time Complexity: O(n^2)
Space Complexity: O(1)

"""


def maxProfit(prices):
    max_profit = 0
    n = len(prices)

    for i in range(n):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)

    return max_profit


# Time Complexity: O(n^2) where n is the number of days (length of prices array)
# Space Complexity: O(1) since we are using only a constant amount of extra space
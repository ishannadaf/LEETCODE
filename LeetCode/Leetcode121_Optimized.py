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


💡 Intuition

👉 We want:

Minimum price before current day
Max profit at current day
🔥 Key Idea:
Keep track of minimum price so far
At each step:
Calculate profit = current - min_price
Update max_profit


"""

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit

# Time Complexity: O(n) where n is the number of days (length of prices array)
# Space Complexity: O(1) since we are using only a constant amount of extra space


"""

⚡ Key Insight

Sliding window doesn’t always mean fixed size
👉 Sometimes it's just tracking best left boundary

🧠 Pattern Learned
Track min/max dynamically
Compare with current element
One pass solution

"""
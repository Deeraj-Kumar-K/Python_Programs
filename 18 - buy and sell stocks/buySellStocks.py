# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Best Time to Buy and Sell Stock
# Maximize profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock
# Return maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0
'''
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because
you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

def maxProfit(prices):
    profit = 0
    lowest = prices[0]
    for price in prices:
        if price < lowest:
            lowest = price
        else:
            # profit = price of stock - lowest price its bought on
            profit = max(profit,price - lowest)
    return profit


prices = [7,1,5,3,6,4]
print(maxProfit(prices))

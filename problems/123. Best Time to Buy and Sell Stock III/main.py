"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        L, R = [0] * l, [0] * l
        L_min, R_max = float("inf"), 0
        profit = 0

        # Divide into two sub-arrays and find optimal
        # solution for the both of them
        for i in range(0, l):
            t = prices[i]
            if t < L_min:
                L_min = t
            L[i] = max(L[i - 1], t - L_min)

            j = -i - 1
            t = prices[j]
            if t > R_max:
                R_max = t
            R[j] = max(R[j + 1], R_max - t)
        
        # Find maximum profit if array divided at ith pos
        # (First set to right[0] if edge-case)
        profit = R[0]
        for i in range(1, l):
            profit = max(profit, R[i] + L[i - 1])
        
        return profit

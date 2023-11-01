"""
Problem Description:
    Say you have an array prices for which the ith element is the price of a
    given stock on day i.
    Design an algorithm to find the maximum profit. You may complete as many
    transactions as you like (i.e., buy one and sell one share of the stock
    multiple times).
    Note: You may not engage in multiple transactions at the same time (i.e.,
    you must sell the stock before you buy again).

    Example 1:
        Input: [7,1,5,3,6,4]
        Output: 7
        Explanation:
            Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1
            = 4.
            Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit
            = 6-3 = 3.

    Example 2:
        Input: [1,2,3,4,5]
        Output: 4
        Explanation:
            Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
            5-1 = 4.
"""
from typing import List


# Solution:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        global i
        ans, flag, buy = 0, 0, 10 ** 10
        if len(prices) <= 1:
            return 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                if not flag:
                    flag = 1
                    buy = prices[i]
            else:
                if flag:
                    flag = 0
                    ans += prices[i] - buy
                    buy = 10 ** 10
        ans += (prices[i + 1] - buy > 0) * (prices[i + 1] - buy)
        return ans


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
    print(solution.maxProfit([1, 2, 3, 4, 5]))
    print(solution.maxProfit([7, 6, 4, 3, 1]))
    print(solution.maxProfit([1, 2]))

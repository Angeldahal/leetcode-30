# Problem Description:
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
# future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Example 1:
#   Input: prices = [7,1,5,3,6,4]
#   Output: 5
#   Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#   Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Solution:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day = 0
        sell_day = 1

        max_profit = 0

        while sell_day < len(prices):
            current_profit = prices[sell_day] - prices[buy_day]

            if prices[buy_day] < prices[sell_day]:
                max_profit = max(current_profit, max_profit)
            else:
                buy_day = sell_day
            sell_day += 1

        return max_profit

    def maxProfit2(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit

# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
    print(solution.maxProfit([7, 6, 4, 3, 1]))
    print(solution.maxProfit2([7, 1, 5, 3, 6, 4]))
    print(solution.maxProfit2([7, 6, 4, 3, 1]))


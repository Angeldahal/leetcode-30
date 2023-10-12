// Problem Description:
// You are given an array prices where prices[i] is the price of a given stock on the ith day.
//
// You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
// future to sell that stock.
// Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
// Example 1:
//   Input: prices = [7,1,5,3,6,4]
//   Output: 5
//   Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
//   Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

// Solution:
/**
 * @param {number[]} prices
 * @return {number}
 */
const maxProfit = function(prices) {
    let buy_day = 0;
    let sell_day = 1;

    let max_profit = 0;

    let current_profit;
    while (sell_day < prices.length) {
        current_profit = prices[sell_day] - prices[buy_day];

        if (prices[buy_day] < prices[sell_day]) {
            max_profit = Math.max(current_profit, max_profit);
        } else {
            buy_day = sell_day;
        }
        sell_day++;
    }
    return max_profit;
};

// Test Cases
console.log(maxProfit([7,1,5,3,6,4])); // 5
console.log(maxProfit([7,6,4,3,1])); // 0
console.log(maxProfit([1,2])); // 1
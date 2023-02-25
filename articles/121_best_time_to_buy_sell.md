# 121 - Best Time to Buy and Sell Stock

## Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the $i^th$ day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the *maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

### Example

```text
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

> [Link to the problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)

## Concept

In order to maximize the profit, we need to find the minimum price before the maximum price. We can do this by keeping track of the minimum price and the maximum profit.

## Solution

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        profit = 0

        for price in prices:
            profit = max(profit, price - buy)
            buy = min(buy, price)

        return profit
```

> Time Complexity: $O(n)$ \
> Space Complexity: $O(1)$

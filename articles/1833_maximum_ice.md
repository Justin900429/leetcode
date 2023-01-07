# 1833 - Maximum Ice Cream Bars

## Problem Description

It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are n ice cream bars. You are given an array costs of length `n`, where $\text{costs[i]}$ is the price of the $i^{th}$ ice cream bar in `coins`. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible.

Return the maximum number of ice cream bars the boy can buy with `coins` coins.

**Note**: The boy can buy the ice cream bars in any order.

### Example

```text
Input: costs = [1,3,2,4,1], coins = 7
Output: 4
Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
```

> [Link to the problem](https://leetcode.com/problems/maximum-ice-cream-bars/)

## Concept

To get the ice-cream bars, we can first sort the costs and start from the smallest one. After we spend all our money, we just return the number of ice-creams we get.

## Solution

```python
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        cur = 0

        while count < len(costs) and cur + costs[count] <= coins:
            cur += costs[count]
            count += 1

        return count
```

> Time Complexity: $O(n)$ \
> Space Complexity: $O(1)$

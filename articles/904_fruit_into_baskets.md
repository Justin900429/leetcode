# 904 - Fruit Into Baskets

## Problem Description

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the type of fruit the `ith` tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

* You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
* Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
* Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array `fruits`, return the **maximum** number of fruits you can pick.

### Example

```text
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
```

> [Link to the problem](https://leetcode.com/problems/fruit-into-baskets/)

## Concept

We maintain a hash and a sliding window. Each time we move the silding window one index right and check current hash table having two or less keys. If it has more than two keys, we move the sliding window left until it has two or less keys.

## Solution

```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        max_res = -1
        start = 0

        for end in range(len(fruits)):
            basket[fruits[end]] = basket.get(fruits[end], 0) + 1

            while len(basket) > 2:
                basket[fruits[start]] -= 1

                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                
                start += 1

            max_res = max(max_res, end - start + 1)

        return max_res
```

> Time complexity: $O(n)$ \
> Space complexity: $O(1)$

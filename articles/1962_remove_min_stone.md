# 1962 - Remove Stones to Minimize the Total

## Problem Description
You are given a 0-indexed integer array piles, where $\text{piles}[i]$ represents the number of stones in the ith pile, and an integer k. You should apply the following operation exactly $k$ times:

* Choose any $\text{piles}[i]$ and remove $\lfloor \text{piles[i]} / 2 \rfloor$ stones from it.
Notice that you can apply the operation on the same pile more than once.

Return the minimum possible total number of stones remaining after applying the k operations.

$\lfloor x \rfloor$ is the greatest integer that is smaller than or equal to $x$ (i.e., rounds $x$ down).

> [Link to the page](https://leetcode.com/problems/remove-stones-to-minimize-the-total/description/)
>

## Concept
This problems requires us to **take out** the maximum rocks to minimize the total. Every time we can choose the stone having the maximum number because we can remove more stones from it. To take out the maximum stones and add it back at each iteration, we can manage a max heap to save the time.

## Solution
The built-in heap in python is a min heap. To convert min heap to max heap, we just add minus sign to each num in the array.

```python
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # Convert to max heap by adding the minus sign in the front
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        
        for _ in range(k):
            cur_max = -heapq.heappop(piles)
            heapq.heappush(piles, -(cur_max - math.floor(cur_max / 2)))
        
        return -sum(piles)

```

> Time complexity: $O(k \log n)$ \
> Space complexity: $O(n)$

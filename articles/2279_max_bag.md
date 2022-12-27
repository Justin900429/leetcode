# 2279 - Maximum Bags With Full Capacity of Rocks

## Problem Description
You have `n` bags numbered from `0` to `n - 1`. You are given two 0-indexed integer arrays capacity and rocks. The ith bag can hold a maximum of $\text{capacity[i]}$ rocks and currently contains $\text{rocks[i]}$ rocks. You are also given an integer additionalRocks, the number of additional rocks you can place in any of the bags.

Return the maximum number of bags that could have full capacity after placing the additional rocks in some bags.

### Example
```
Input: capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2
Output: 3
Explanation:
Place 1 rock in bag 0 and 1 rock in bag 1.
The number of rocks in each bag are now [2,3,4,4].
Bags 0, 1, and 2 have full capacity.
There are 3 bags at full capacity, so we return 3.
It can be shown that it is not possible to have more than 3 bags at full capacity.
Note that there may be other ways of placing the rocks that result in an answer of 3.
```
> [Link to the page](https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/description/)

## Concept
To fill up more bags with rock, we can first find it the capacity and check how much rocks we need to fill up the bags. We should start from the smallest one (need less rocks to fill up) and place the rocks in it. The whole process should be done greedily to ensure maximum filled-up bags.

## Solution
The algorithm is as follows

```
1. Create a residual array and sort the residual array in ascending order
2. Greedily assign the rocks to the smallest one and so on til the rocks are over or reach the end of the array
```

```python
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        residual = [capacity[i] - rocks[i] for i in range(len(capacity))]
        residual.sort()

        cur = 0
        while additionalRocks > 0 and cur < len(rocks):
            if residual[cur] > 0 and additionalRocks >= residual[cur]:
                additionalRocks -= residual[cur]
                residual[cur] = 0
            elif residual[cur] > 0:
                break
            
            cur += 1
        
        return sum([residual[idx] == 0 for idx in range(len(rocks))])

```
> Time Complexity: $O(n)$ \
> Space Complexity: $O(n)$

We can also sum up the rocks from the beginning and check it doesn't exceed the additional rocks.

```python
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        residual = [capacity[i] - rocks[i] for i in range(len(capacity))]
        residual.sort()

        accum = 0
        for idx in range(len(residual)):
            accum += residual[idx]
            if accum > additionalRocks:
                return idx
        
        return len(rocks)
```
> Time Complexity: $O(n)$ \
> Space Complexity: $O(n)$
# 134 - Gas Station

## Problem Description

There are `n` gas stations along a circular route, where the amount of gas at the $i^{th}$ station is $\text{gas[i]}$.

You have a car with an unlimited gas tank and it costs $\text{cost[i]}$ of gas to travel from the ith station to its next $(i + 1)^{th}$ station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays `gas` and `cost`, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return `-1`. If there exists a solution, it is **guaranteed** to be **unique**

### Example

```text
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
```

> [Link to the problem](https://leetcode.com/problems/gas-station/)

## Concept

Our target is to find from which index $i$, we can have $\sum_i^k x_i \ge 0$ for $k \in [0, n - 1]$. We can start from the beginning of the array, and check whether current accumulated sum is smaller than 0. If it is 0, we move the start point to the next index and set the accumulated sum to 0. The step is shown below:

```text
Step1: start_point = 0
Step2:
    FOR i in (0, ..., n - 1)
        accum += gas[i] - cost[i]
        IF ACCUM < 0:
            start_point = i + 1
            accum = 0
        ENDIF
    ENDFOR
Step3:
    if SUM(GAS) < SUM(COST): return -1
    else: return start_point
```

Here, we proof the algorithm is valid. Let's suppose we are at the start point $k$, and the current accumulate sum is $S_k$, and $x_k = \text{gas[k]} - \text{cost[k]}$. We start from $k$ and add til $k + n$, we have $S_{k,k+n} \lt 0$ and $S_{k,k+n-1} \ge 0$. We must show that from $k$ to $k + n$ are all non-starting points. Suppose ${k + l}$ is the starting point, we should have $S_{k,k+n} - S_{k,k+l-1} \ge 0$. However, we know that $S_{k,k+l-1} \ge 0$, otherwise we would stop at $k+l-1$. So we have $S_{k,k+n}-S_{k,k+l-1} \lt 0$, showing the index $i \in [k, k + n]$ are all non-starting points.

## Solution

```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        accum = 0
        count = 0
        start_point = 0
        for idx in range(len(gas)):
            accum += gas[idx] - cost[idx]
            count += gas[idx] - cost[idx]
            if count < 0:
                count = 0
                start_point = idx + 1

        return -1 if accum < 0 else start_point
```

> Time complexity: $O(n)$ \
> Space complexity: $O(1)$

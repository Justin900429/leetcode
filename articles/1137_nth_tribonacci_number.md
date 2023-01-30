# 1137 - N-th Tribonacci Number

## Problem Description

The Tribonacci sequence Tn is defined as follows:
$T_0 = 0, T_1 = 1, T_2 = 1,$ and $T_{n+3} = T_n + T_{n+1} + T_{n+2}$ for $n \ge 0$.
Given `n`, return the value of $T_n$.

### Example

```text
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
```

> [Link to the problem](https://leetcode.com/problems/n-th-tribonacci-number/)

## Concept

Using recursive with memoization to solve the problem.

## Solution

```python
class Solution:
    @lru_cache(None)
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n < 3: return 1
        
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
```

> Time complexity: $O(n)$ \
> Space complexity: $O(n)$

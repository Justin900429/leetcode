# 926 - Flip String to Monotone Increasing

## Problem Description

A binary string is monotone increasing if it consists of some number of `0`'s (possibly none), followed by some number of `1`'s (also possibly none).

You are given a binary string `s`. You can flip `s[i]` changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make `s` monotone increasing.

### Example

```text
Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
```

> [Link to the problem](https://leetcode.com/problems/flip-string-to-monotone-increasing/description/)

## Concept

To create a monotonic string, we should definetly have zero on the left side and one on the right side. The current length minimum flip can also be computed by its `length - 1`. Therefore, this problem can be classified in to DP problem.

$$
dp[i] =
\begin{cases}
dp[i - 1], & \text{if s[i]} = 1 \\
\min(dp[i - 1] + 1, \text{count\_one}), & \text{if s[i]} = 0
\end{cases}
$$

The $\text{count\_one}$ here means the number of one in front of the current index. The reason we have to maintain the $\text{count\_one}$ because we might flip all the front coins to `0` if current coin is `0`, and the number of flips is equal to the number of `1` in the front.

## Solution

```python
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = 0
        m = 0

        for char in s:
            if char == "1":
                m += 1
            else:
                ans = min(ans + 1, m)
        
        return ans
```

> Time complexity: $O(n)$ \
> Space complexity: $O(1)$

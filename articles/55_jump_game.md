# 55 - Jump Game

## Problem Description
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

> [Link to the page.](https://leetcode.com/problems/jump-game/description/)

## Concept
This problem requires us to find the maximum index that can reach from the current position. For example, if we have the `nums` = [2, 3, 1], then the maximum index we can reach from `index 0` is `2`. The result requires us to check whether the maximum index accumulated from `index 0` can reach the end of the `nums`

## Solution
Here, we define $\text{dp}[i]$ as the maximum index which can reach from the position $i$. Then we have

$$
\text{dp}[i] = 
\begin{cases}
\text{nums}[0] &, \text{if } i = 0 \\
\max(\text{dp}[i - 1], i + \text{nums}[i]) & ,\text{if dp}[i - 1] \ge i \\
0 &, otherwise
\end{cases}
$$

Note that we should always check whether current index is reachable.

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        cur = 0
        for idx in range(1, len(nums)):
            if idx > dp[idx - 1] or dp[idx - 1] >= len(nums) - 1:
                break
            dp[idx] = max(dp[idx - 1], idx + nums[idx])
            cur = idx
        
        return dp[cur] >= len(nums) - 1
```
> Time complexity: $O(n)$ \
> Space complexity: $O(n)$

We can also remove the $\text{dp}$ and use only one variable to save the current max (current state is only related to the last state).

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_max = 0

        for idx in range(len(nums)):
            if idx > current_max or current_max >= len(nums) - 1:
                break
            current_max = max(current_max, idx + nums[idx])
        
        return current_max >= len(nums) - 1
```

> Time complexity: $O(n)$ \
> Space complexity: $O(1)$

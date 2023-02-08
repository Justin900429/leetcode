# 45 - Jump Game II

## Problem Description

You are given a 0-indexed array of integers `nums` of length n. You are initially positioned at `nums[0]`.

Each element `nums[i]` represents the maximum length of a forward jump from index i. In other words, if you are at `nums[i]`, you can jump to any nums[i + j] where:

* `0 <= j <= nums[i]` and
* `i + j < n`

Return the minimum number of jumps to reach `nums[n - 1]`. The test cases are generated such that you can reach `nums[n - 1]`.

### Example

```text
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

> [Link to the problem](https://leetcode.com/problems/jump-game-ii/)

## Concept

Use dynamic programming to solve this problem. The idea is to use a list to store the minimum number of jumps to reach the current index. Then for each index, we can calculate the minimum number of jumps to reach the next index by using the current index. The final result is the last element in the list.

## Solution

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = [float("inf")] * len(nums)
        res[0] = 0

        for idx in range(len(nums) - 1):
            for idy in range(idx + 1, min(idx + nums[idx] + 1, len(nums))):
                res[idy] = min(res[idy], res[idx] + 1)
        
        return res[-1]
```

> Time complexity: $O(mn)$ \
> Space complexity: $O(n)$

Note that $m$ is the maximum number of jumps and $n$ is the length of the array.

There is another greedy solution, please refer to [here](https://leetcode.com/problems/jump-game-ii/solutions/3076867/jump-game-ii/).

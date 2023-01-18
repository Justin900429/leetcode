# 918 - Maximum Sum Circular Subarray

## Problem Description

Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of `nums[i]` is `nums[(i + 1) % n]` and the previous element of `nums[i]` is `nums[(i - 1 + n) % n]`.

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray `nums[i], nums[i + 1], ..., nums[j]`, there does not exist `i <= k1, k2 <= j` with `k1 % n == k2 % n`.

### Example

```text
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
```

> [Link to the problem](https://leetcode.com/problems/maximum-sum-circular-subarray)

## Concept

To find the maximum subarray, we cam first compute the normal maximum sum array by using Kadane's algorithm. However, the array is the circular array, which we should also consider the prefix + suffix sum. Therefore, we can compute the minimum subarray first (by Kadane's algorithm) and use the total sum to minus the minimum subarray to obtain the maximum prefix + suffix sum. Note that if the minimum subarray is equal to the total sum of an array, the sign of each entry is negative, and we should defintely return the maximum subarray num (single element indeed).

## Solution

```python
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_min = min_num = float("inf")
        cur_max = max_num = float("-inf")
        sum_ = 0

        for num in nums:
            cur_min = min(cur_min, 0) + num
            min_num = min(min_num, cur_min)
            cur_max = max(cur_max, 0) + num
            max_num = max(max_num, cur_max)
            sum_ += num

        return max_num if min_num == sum_ else max(max_num, sum_ - min_num)
```

> Time Complexity: $O(n)$ \
> Space Complexity: $O(1)$

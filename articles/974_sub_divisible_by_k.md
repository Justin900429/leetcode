# 974 - Subarray Sums Divisible by K

## Problem Description

Given an integer array `nums` and an integer `k`, return the *number of non-empty* `subarrays` that have a sum divisible by `k`.

A **subarray** is a **contiguous** part of an array.

### Example

```text
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
```

> [Link to the problem](https://leetcode.com/problems/subarray-sums-divisible-by-k/)

## Concept

To find out the number of subarrays divisible by k, we can maintain a prefix sum and use a hash table to save the count of the remainder. For example, if we want to find whether from index `2` to index `5` is divisible by `k` or not, we should have

$$
(prefix[5] - prefix[1]) \mod k
$$

Then, to compute that all the subarrays end at index `5`, we can simply add the total number having the same remainder.

## Solution

```python
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0

        find = defaultdict(int)
        count = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum % k == 0:
                count += 1
            
            count += find[prefix_sum % k]
            find[prefix_sum % k] += 1
        
        return count
```

> Time Complexity: $O(n)$ \
> Space Complexity: $O(1)$

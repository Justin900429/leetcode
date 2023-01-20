# 491 - Non-decreasing Subsequences

## Problem Description

Given an integer array `nums`, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in **any order**.

### Example

```text
Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
```

## Concept

To find out the increasing subsequence, we can backtrack it and find the non-decreasing subsequence. However, the length of the array is small, we can also use a bitmask to create the sequence and check whether each sequence is acceptable.

## Solution

```python
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = set()
        
        for bitmask in range(1, 1 << n):
            sequence = [nums[i] for i in range(n) if (bitmask >> i) & 1]
            if len(sequence) >= 2 and all([sequence[i] <= sequence[i + 1]
                                          for i in range(len(sequence) - 1)]):
                result.add(tuple(sequence))
        return result
```

> Time Complexity: $O(2^n n)$ \
> Space Complexity: $O(2^n n)$

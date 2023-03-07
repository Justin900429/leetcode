# 2444 - Count Subarrays With Fixed Bounds

## Problem Description

You are given an integer array nums and two integers `minK` and `maxK`.

A **fixed-bound subarray** of `nums` is a subarray that satisfies the following conditions:

* The **minimum** value in the subarray is equal to `minK`.
* The **maximum** value in the subarray is equal to `maxK`.

*Return the* **number** *of fixed-bound subarrays*.

A **subarray** is a **contiguous** part of an array.

### Example

```text
Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
```

> [Link to the problem](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/)

## Concept

At every index, we save three different values:

* Bad index: the index of the last element that is not in the range `[minK, maxK]`.
* Min index: the index of the last element that is equal to `minK`.
* Max index: the index of the last element that is equal to `maxK`.

Then, the starting index of the subarray can be chose from `[bad index + 1, min(min index, max_index)]`. Hence, we can sum up all the subarray when we visit an index.

## Solution

```python
class Solution:
    def countSubarrays(self, A: List[int], minK: int, maxK: int) -> int:
        res = 0
        jmin = jmax = jbad = -1
        for i,a in enumerate(A):
            if not minK <= a <= maxK: jbad = i
            if a == minK: jmin = i
            if a == maxK: jmax = i
            res += max(0, min(jmin, jmax) - jbad)
        return res
```

> Time complexity: $O(n)$ \
> Space complexity: $O(1)$

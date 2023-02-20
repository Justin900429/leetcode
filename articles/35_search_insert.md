# 35 - Search Insert Position

## Problem Description

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with $O(\log n)$ runtime complexity.

### Example

```text
Input: nums = [1,3,5,6], target = 5
Output: 2
```

> [Link to the problem](https://leetcode.com/problems/search-insert-position/)

## Concept

To find the insert position within the sorted list, we can perform binary search. If the numner is found, we return the index. Otherwise, we return the left index after the searh is over.

## Solution

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
```

> Time complexity: $O(\log n)$ \
> Space complexity: $O(1)$

# 540 - Single Element in a Sorted Array

## Problem Description

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in $O(\log n)$ time and $O(1)$ space.

## Concept

To find the single element in a sorted array, we can perform a binary search. At each iteration, we check whether the number of either section is even or not. If either of it is even, we can safely check only the other one. Note that we should check the duplicate of the middle number and cross it.

## Solution

```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = start + (end - start) // 2
            print(mid)
            if nums[mid] == nums[mid - 1]:
                if (end - mid) % 2 == 0:
                    end = mid - 2
                else:
                    start = mid + 1
            elif nums[mid] == nums[mid + 1]:
                if (mid - start) % 2 == 0:
                    start = mid + 2
                else:
                    end = mid - 1
            else:
                return nums[mid]

        return nums[start]
```

> Time Complexity: $O(\log n)$ \
> Space Complexity: $O(1)$

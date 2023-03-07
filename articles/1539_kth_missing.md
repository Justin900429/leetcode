# 1539 - Kth Missing Positive Number

## Problem Description

Given an array `arr` of positive integers sorted in a **strictly increasing order,** and an integer `k`.

Return the `kth` **positive** integer that is **missing** from this array.

### Example

```text
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
```

> [Link to the problem](https://leetcode.com/problems/kth-missing-positive-number/)

## Concept

In order to find the $k^{th}$ missing number, we do a binary search. At each iteration, we obtain the mid number and check the number of missing values by `arr[mid] - mid - 1`. If the number of missing values is less than $k$, we know that the missing number is in the right half of the array. Otherwise, it is in the left half. Finally, the $k^{th}$ missing should be `arr[idx] + k - (arr[idx] - idx - 1) = k + idx + 1`, where the first term represents the next k missing number and the right term represents the number of missing values in the left half. Pratically, `idx` should be `mid` and `idx + 1` will be `mid + 1 = start`.

## Solution

```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] - mid - 1 < k:
                start = mid + 1
            else:
                end = mid - 1

        return start + k
```

> Time complexity: $O(\log n)$ \
> Space complexity: $O(n)$

# 912 - Sort an Array

## Problem Description

Given an array of integers `nums`, sort the array in ascending order and return it.

You must solve the problem **without using any built-in functions** in $O(n \log n)$ time complexity and with the smallest space complexity possible.

### Example

```text
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
```

> [Link to the problem](https://leetcode.com/problems/sort-an-array)

## Concept

To sort an array  within $O(n \log n)$ without using any built-in function, we can implement different solution such as **merge sort**, **quick sort**, **heap sort**, etc. Here we use **merge sort** to solve the problem. At each time, we divide the array into same length sub-arrays and sort them. Then we merge the sub-arrays into one sorted array.

## Solution

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        array_len = len(nums)
        left_sort = self.sortArray(nums[:array_len // 2])
        right_sort = self.sortArray(nums[array_len // 2:])

        return merge(left_sort, right_sort)

    def merge(sort_1, sort_2):
        res = [0] * len(len(sort_1) + len(sort_2))

        count_1 = conut_2 = 0

        while count_1 < len(sort_1) and count_2 < len(sort_2):
            if sort_1[count_1] < sort2[count_2]:
                res[count_1 + conut_2] = sort_1[count_1]
                count_1 += 1
            else:
                res[count_1 + count_2] = sort_2[count_2]

        while count_1 < len(sort_1):
            res[count_1 + count_2] = sort_1[count_1]
            count_1 += 1

        while count_2 < len(sort_2):
            res[count_1 + count_2] = sort_2[count_2]
            count_2 += 1

        return res
```

> Time complexity: $O(n \log n)$ \
> Space complexity: $O(n)$

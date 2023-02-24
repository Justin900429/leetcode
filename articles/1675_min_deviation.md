# 1675 - Minimize Deviation in Array

## Problem Description

You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

* If the element is **even**, **divide** it by `2`.
  * For example, if the array is `[1,2,3,4]`, then you can do this operation on the last element, and the array will be `[1,2,3,2]`.
* If the element is **odd**, **multiply** it by `2`.
  * For example, if the array is `[1,2,3,4]`, then you can do this operation on the first element, and the array will be `[2,2,3,4]`.

The **deviation** of the array is the **maximum difference** between any two elements in the array.

*Return the* **minimum deviation** *the array can have after performing some number of operations.*

### Example

```text
Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.
```

> [Link to the problem](https://leetcode.com/problems/minimize-deviation-in-array)

## Concept

To find the minimum deviation of the array, we should try maximize the minimum value and minimize the maximum value within the array. At first, we can multiply all odd numbers by 2 to make them even. To find the maximum value of the array, we maintain a heap. When the maximum number is a odd number, we stop the heap. Otherwise, we divide the maximum number by 2 and push it back to the heap. We can keep doing this until the maximum number is odd. Note that we should also maintain the min value of the array. We stop when the maximum number is odd because we can only multiply it by 2 and the next iteration will pick the same number (two times larger than previous) and devide it by 2 before pusing back to the heap. Similarly, in the next iteration, we will pick the same number and multiply it by 2. This process will continue forever. Therefore, we should stop when the maximum number is odd.

```text
## Iter n
Max Num: 7 -> Make it to be 14 and push back
to the heap

## Iter n + 1
Max Num: 14 -> Make it to be 7 and push back
to the heap

## Iter n + 2
Max Num: 7 -> Make it to be 14 and push back
to the heap
...
```

## Solution

```python
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = [-num * 2 if num % 2 == 1 else -num for num in nums]
        heapq.heapify(heap)
        min_val = float("inf")
        for num in nums:
            min_val = min(min_val, num * 2 if num % 2 == 1 else num)
        
        min_deviation = float("inf")
        while True:
            max_val = -heapq.heappop(heap)
            min_deviation = min(min_deviation, max_val - min_val)

            if max_val % 2 == 1:
                break
            
            heapq.heappush(heap, -(max_val // 2))
            min_val = min(min_val, max_val // 2)

        return min_deviation
```

> Time Complexity: $O(n\log n)$ \
> Space Complexity: $O(n)$

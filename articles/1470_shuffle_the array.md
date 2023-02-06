# 1470 - Shuffle the Array

## Problem Description

Given the array nums consisting of 2n elements in the form `[x1,x2,...,xn,y1,y2,...,yn]`.

Return the array in the form `[x1,y1,x2,y2,...,xn,yn]`.

### Example

```text
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
```

## Concept

We create an empty array, iterate the original array and fill two elements in the same time.

```text
# Intial
n: 2
Origin: [2, 5, 3, 4]

# Start
## First iteration: 
Res:             [2        ,      3]
Res index:       [2 * 0    ,   2 * 0 + 1]
Num index:       [0        ,    0 + n]

## Second iteration: 
Res:             [2        ,      3        ,     5       ,       4]
Res index:       [2 * 0    ,   2 * 0 + 1   ,   2 * 1     ,    2 * 1 + 1]
Num index:       [0        ,    0 + n      ,     1       ,     1 + n]
```

## Solution

```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [0] * (2 * n)

        for idx in range(n):
            res[2 * idx] = nums[idx]
            res[2 * idx + 1] = nums[idx + n]

        return res 
```

> Time complexity: $O(n)$ \
> Space complexity: $O(1)$

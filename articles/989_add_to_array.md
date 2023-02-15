# 989 - Add to Array-Form of Integer

## Problem Description

The **array-form** of an integer `num` is an array representing its digits in left to right order.

* For example, for `num = 1321`, the array form is `[1,3,2,1]`.

Given `num`, the **array-form** of an integer, and an integer `k`, return the ***array-form*** of the integer `num + k`.

## Concept

We add the number from the latest bit of the array including carry. Everytime we add a bit, we devide the `k` by 10 and add the carry. If k is zero, we break the loop to avoid unnecessary computation. If k is not zero, we convert k from string to integer array and add it before the array.

## Solution

```python
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for idx in range(len(num) - 1, -1, -1):
            k, d = divmod(k, 10)
            carry, num[idx] = divmod(num[idx] + d, 10)
            k += carry

            if not k: break

        if k:
            num = list(map(int, str(k))) + num

        return num
```

> Time complexity: $O(max(N, \log_{10}k))$ \
> Space complexity: $O(1)$

Note that $N$ here is the length of the array `num`.

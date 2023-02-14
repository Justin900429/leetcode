# 67 - Add Binary

## Problem Description

Given two binary strings `a` and `b`, return *their sum as a binary string*.

### Example

```text
Input: a = "11", b = "1"
Output: "100"
```

> [Link to the problem](https://leetcode.com/problems/add-binary/)

## Concept

We obtain the result backwardly and process three different scenarios:

1. `a[idx]` and `b[idx]` are 1
2. `a[idx]` and `b[idx]` are 0
3. One of `a[idx]` or `b[idx]` is 0 and 1

Note that we should maintain a `move` to save carry bit and should also consider the carry bit after computing both `a` and `b`.

## Solution

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        move = '0'
        cur = 1

        while cur <= min(len(a), len(b)):
            if a[-cur] == '0' and b[-cur] == '0':
                res += move
                move = '0'
            elif a[-cur] == '1' and b[-cur] == '1':
                res += move
                move = '1'
            elif a[-cur] == '1' or b[-cur] == '1':
                if move == '1':
                    res += '0'
                    move = '1'
                else:
                    res += '1'
                    move = '0'

            cur += 1

        longer = a if len(a) > len(b) else b
        while cur <= len(longer):
            if longer[-cur] == '0' and move == '1':
                res += '1'
                move = '0'
            elif longer[-cur] == '1' and move == '1':
                res += '0'
                move = '1'
            else:
                res += longer[-cur]
            cur += 1
        
        if move == '1':
            res += '1'
        
        return res[::-1]
```

> Time Complexity: $O(n)$ \
> Space Complexity: $O(1)$

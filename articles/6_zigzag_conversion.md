# 6 - Zigzag Conversion

## Problem Description

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```text
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

```text
string convert(string s, int numRows);
```

> [Link to the problem](https://leetcode.com/problems/zigzag-conversion/)

## Concept

The core concept of zigzag is going forward and backward. We only have to remember when to change direction and add the charater to the result. The only difference here is we should move on **row index**. The rest is the same.

## Solution

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res = ["" for _ in range(numRows)]

        back = True
        index = 0
        for char in s:
            res[index] += char

            if index == 0 or index == numRows - 1:
                back = not back
            
            if back: index -= 1
            else: index += 1

        return "".join(res)
```

> Time complexity: $O(n)$ \
> Space complexity: $O(1)$

Note that although we use `res` to build the output, it is necessary for us to create such space to save the result, therefore it should not be taken into account for extra spaces.

# 1523 - Count Odd Numbers in an Interval Range

## Problem Description

Given two non-negative integers `low` and `high`. Return the count of odd numbers between `low` and `high` *(inclusive)*.

### Example

```text
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
```

## Concept

Two check the odd number between the range, we first record the number between the range. We should check for the boundaries and add 1 if either `low` or `high` is an odd number.

## Solution

```python
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + ((high % 2 == 1) or (low % 2 == 1))
```

> Time complexity: $O(1)$ \
> Space complexity: $O(1)$

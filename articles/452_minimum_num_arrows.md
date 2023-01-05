# 452 - Minimum Number of Arrows to Burst Balloons

## Problem Description

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where $\text{points[i]}$ = `[xstart, xend]` denotes a balloon whose **horizontal diameter** stretches between `xstart` and `xend`. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up **directly vertically** (in the positive y-direction) from different points along the x-axis. A balloon with `xstart` and `xend` is **burst** by an arrow shot at `x` if `xstart <= x <= xend`. There is **no limit** to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array `points`, return the `minimum` number of arrows that must be shot to burst all balloons.

### Example

```text
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
```

## Concept

This problem can be classified into maximum-interval problem. After finding the maximum interval within a subrange, we can destroy all the ballons within this set with minimum cost, that is, `1`. We just follow this rule til the end and return the answer.

## Solution

We use only the `end` to sort the array and check whether current `start` exceed the first `end`.

```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        count = 1
        cur_end = points[0][1]

        for start, end in points:
            if start > cur_end:
                cur_end = end
                count += 1

        return count
```

> Time Complexity: $O(n \log n)$ \
> Space Complexity: $O(1)$

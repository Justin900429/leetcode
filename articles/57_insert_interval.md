# 57 - Insert Interval

## Problem Description

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [starti, endi]` represent the start and the end of the $i^{th}$ interval and intervals is sorted in ascending order by `starti`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `starti` and intervals still does not have any overlapping `intervals` (merge overlapping intervals if necessary).

Return `intervals` after the insertion.

### Example

```text
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

> [Link to the problem](https://leetcode.com/problems/insert-interval/description/)

## Concept

To merge all the intervals, we should first find out the insert point for the new interval. To efficiently find out the insert point in a sorted array, we can use binary search. After finding the insert point, we can add the interval one by one and compare the current interval with the last one in the answer and update the interval range or add it to the answer by:

1. If current start is greater than the last answer end, we add current interval to the end of the answer.
2. Otherwise, update the last answer end by max(answer end, current end)

## Solution

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.insert(bisect.bisect(intervals, newInterval), newInterval)

        res = []
        for inter in intervals:
            if not res or inter[0] > res[-1][1]:
                res.append(inter)
            else:
                res[-1][1] = max(res[-1][1], inter[1])  
        return res
```

> Time Complexity: $O(n)$ \
> Space Complexity: $O(1)$

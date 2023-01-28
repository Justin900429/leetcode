# 352. Data Stream as Disjoint Intervals

## Problem Description

Given a data stream input of non-negative integers `a1, a2, ..., an`, summarize the numbers seen so far as a list of disjoint intervals.

Implement the `SummaryRanges` class:

* `SummaryRanges()` Initializes the object with an empty stream.
* `void addNum(int value)` Adds the integer value to the stream.
* `int[][] getIntervals()` Returns a summary of the integers in the stream currently as a list of disjoint intervals `[starti, endi]`. The answer should be sorted by `starti`.

### Example

```text
Input
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
Output
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

Explanation
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // return [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
```

> [Link to the problm](https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/)

## Concept

We maintain a `num_list` and a `num_set` for saving numbers and checking whether number in the list. Note that we can add a $\inf$ at the end of the num list to handle the edge case for the `getIntervals`.

## Solution

```python
class SummaryRanges:

    def __init__(self):
        self.num_list = [float("inf")]
        self.num_set = set()

    def addNum(self, value: int) -> None:
        if value in self.num_set:
            return

        bisect.insort_left(self.num_list, value)
        self.num_set.add(value)

    def getIntervals(self) -> List[List[int]]:
        if len(self.num_list) == 0: return []

        res = []
        temp = [self.num_list[0], self.num_list[0]]
        accum = temp[0]

        for num in self.num_list[1:]:
            if num - accum == 1:
                accum += 1
            else:
                temp[1] = accum
                res.append(temp[:])
                temp[0] = accum = num

        return res
```

> Time Complexity: $O(\log n) \text{  for addNum},\\ O(n) \text{ for getIntervals}$ \
> Space Complexity: $O(n)$

Note that using C++ can have $O(\log n)$ solution for `getIntervals` with `Treemap` data structure.

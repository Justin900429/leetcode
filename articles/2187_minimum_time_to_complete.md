# 2187 - Minimum Time to Complete Trips

## Problem Description

You are given an array `time` where `time[i]` denotes the time taken by the $i^{th}$ bus to complete **one trip**.

Each bus can make multiple trips **successively**; that is, the next trip can start **immediately after** completing the current trip. Also, each bus operates **independently**; that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer `totalTrips`, which denotes the number of trips all buses should make **in total**. Return the ***minimum time*** *required for all buses to complete* ***at least*** `totalTrips` *trips*.

### Example

```text
Input: time = [1,2,3], totalTrips = 5
Output: 3
Explanation:
- At time t = 1, the number of trips completed by each bus are [1,0,0]. 
  The total number of trips completed is 1 + 0 + 0 = 1.
- At time t = 2, the number of trips completed by each bus are [2,1,0]. 
  The total number of trips completed is 2 + 1 + 0 = 3.
- At time t = 3, the number of trips completed by each bus are [3,1,1]. 
  The total number of trips completed is 3 + 1 + 1 = 5.
So the minimum time needed for all buses to complete at least 5 trips is 3.
```

> [Link to the problem](https://leetcode.com/problems/minimum-time-to-complete-trips)

## Concept

In order to find the minimum time to finish the trips, we can start from the maximum number, and do the binary search on that number. At each iteration, we require extra $O(n)$ time to check the whether current time is enough for all buses to finish the trips. If the time is not enought, we move to right part, otherwise, we check the left part.

## Solution

```python
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def check_require(total_time):
            return sum([total_time // required_time for required_time in time]) < totalTrips
        start = 1
        end = 10**16

        while start < end:
            mid = start + (end - start) // 2
            if check_require(mid):
                start = mid + 1
            else:
                end = mid

        return start
```

> Time Complexity: $O(n\log 10^{16})$ \
> Space Complexity: $O(1)$

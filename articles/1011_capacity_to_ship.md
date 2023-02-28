# 1011 - Capacity To Ship Packages Within D Days

## Problem Description

A conveyor belt has packages that must be shipped from one port to another within `days` days.

The `ith` package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `days` days.

### Example

```text
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
```

> [Link to the problem](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days)

## Concept

The maximum capacity should the sum of the `weights`, therefore, we can start from the maximum capcity and do the binary search to find the minimum capactity that can ship the cargos with `days` days.

## Solution

```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = 1
        end = sum(weights)

        def check_cap(cap):
            cur = 0
            idx = 0
            count_day = 1

            while idx < len(weights):
                if weights[idx] > cap:
                    return 1
                if cur + weights[idx] > cap:
                    count_day += 1
                    cur = 0

                cur += weights[idx]
                idx += 1

            return count_day > days
        
        while start < end:
            mid = start + (end - start) // 2
            state = check_cap(mid)
            if state:
                start = mid + 1
            else:
                end = mid

        return start
```

Note that $n$ is the length of `weights`.

> Time Complexity: $O(n * \log(500n))$ \
> Space Complexity: $O(1)$

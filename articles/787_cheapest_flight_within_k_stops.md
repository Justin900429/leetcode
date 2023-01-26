# 787 - Cheapest Flights Within K Stops

## Problem Description

There are n cities connected by some number of flights. You are given an array flights where `flights[i] = [fromi, toi, pricei]` indicates that there is a flight from city `fromi` to city `toi` with cost pricei.

You are also given three integers `src`, `dst`, and `k`, return **the cheapest price** from `src` to `dst` with at most `k` stops. If there is no such route, return `-1`.

### Example

![787 example image](https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-3drawio.png)

```text
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
```

## Concept

Another directed shortest path problem with BFS. The only different is to limit the search to k level.

## Solution

```python
class Solution:        
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        
        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))
        
        queue = deque([(src, 0)])
        dist = [float("inf")] * len(graph)
        dist[src] = 0
        level = 0
        
        while level < k + 1 and len(queue) != 0:
            level += 1
            
            new_level = []
            while len(queue) != 0:
                cur, cur_dis = queue.popleft()
                for child, weight in graph[cur]:
                    if dist[child] > cur_dis + weight:
                        dist[child] = cur_dis + weight
                        new_level.append((child, dist[child]))
            
            if new_level:
                queue.extend(new_level)

        return -1 if dist[dst] == float("inf") else dist[dst]
```

> Time Complexity: $O(n)$ \
> Space Complexity: $O(n)$

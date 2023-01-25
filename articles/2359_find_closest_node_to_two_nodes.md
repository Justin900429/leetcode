# 2359 - Find Closest Node to Given Two Nodes

## Problem Description

You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node `edges[i]`. If there is no outgoing edge from `i`, then `edges[i] == -1`.

You are also given two integers `node1` and `node2`.

Return the **index** of the node that can be reached from both `node1` and `node2`, such that the **maximum** between the distance from `node1` to that node, and from `node2` to that node is minimized. If there are multiple answers, return the node with the **smallest index**, and if no possible answer exists, return `-1`.

Note that `edges` may contain cycles.

### Example

![2359 example image](https://assets.leetcode.com/uploads/2022/06/07/graph4drawio-2.png)

```text
Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
Output: 2
Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.
```

## Concept

Finding the shortest path on directed graph with BFS on two given nodes. Iterate all the nodes and find the minimum of maximum distance in each pair.

## Solution

```python
class Solution:class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        graph = [[] for _ in range(len(edges))]

        for idx, e in enumerate(edges):
            if e != -1: graph[idx].append(e)
        
        dis1 = [float("inf")] * len(edges)
        dis2 = [float("inf")] * len(edges)

        def find(start, dis):
            dis[start] = 0
            queue = deque([(0, start)])

            while queue:
                d, cur = queue.popleft()
                if d > dis[cur]:
                    continue
                
                for neigh in graph[cur]:
                    if dis[cur] + 1 < dis[neigh]:
                        dis[neigh] = dis[cur] + 1
                        queue.append((dis[neigh], neigh))

        find(node1, dis1)
        find(node2, dis2)

        min_res = float("inf")
        res = -1

        for idx in range(len(dis1)):
            if dis1[idx] == float("inf") or dis2[idx] == float("inf"):
                continue

            if min_res > max(dis1[idx], dis2[idx]):
                min_res = max(dis1[idx], dis2[idx])
                res = idx
        
        return -1 if min_res == float("inf") else res
```

> Time complexity: $O(|E| + |V|)$ \
> Space complexity: $O(|E|)$

Note that $O(E)$ space complexity is contributed by the adjacent list graph. This can be reduced to $O(V)$ just by using the given `edges`.

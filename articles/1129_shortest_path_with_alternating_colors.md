# 1129 - Shortest Path with Alternating Colors

## Description

You are given an integer `n`, the number of nodes in a directed graph where the nodes are labeled from `0` to `n - 1`. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays `redEdges` and `blueEdges` where:

* `redEdges[i] = [ai, bi]` indicates that there is a directed red edge from node `ai` to node `bi` in the graph, and
* `blueEdges[j] = [uj, vj]` indicates that there is a directed blue edge from node `uj` to node `vj` in the graph.

Return an array `answer` of length `n`, where each `answer[x]` is the length of the shortest path from node `0` to node `x` such that the edge colors alternate along the path, or `-1` if such a path does not exist.

### Example

```text
Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
```

## Concept

This problem can be considered as the multisource BFS. We record whether current node has been visited with different colors and only visit the node with different color. We also need to record the minimum distance from the source node to the current node.

## Solution

```python
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        dist = [float("inf")] * n
        dist[0] = 0

        graph = [[] for _ in range(n)]
        for i, j in redEdges:
            graph[i].append((j, 0))
        
        for i, j in blueEdges:
            graph[i].append((j, 1))

        queue = deque([(0, 0, -1)])
        visited = [[False, False] for _ in range(n)]

        while queue:
            cur, step, cur_color = queue.popleft()

            for neigh, neigh_color in graph[cur]:
                if neigh_color != cur_color and not visited[neigh][neigh_color]:
                    dist[neigh] = min(dist[neigh], step + 1)
                    visited[neigh][neigh_color] = True
                    queue.append((neigh, step + 1, neigh_color))
        
        return [-1 if temp == float("inf") else temp for temp in dist]
```

> Time complexity: $O(|V| + |E|)$ \
> Space complexity: $O(|V| + |E|)$

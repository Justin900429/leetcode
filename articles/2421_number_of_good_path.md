# 2421 - Number of Good Paths

## Problem Description

There is a tree (i.e. a connected, undirected graph with no cycles) consisting of n nodes numbered from `0` to `n - 1` and exactly `n - 1` edges.

You are given a 0-indexed integer array vals of length `n` where `vals[i]` denotes the value of the ith node. You are also given a 2D integer array edges where `edges[i] = [ai, bi]` denotes that there exists an undirected edge connecting nodes `ai` and `bi`.

A good path is a simple path that satisfies the following conditions:

The starting node and the ending node have the same value.
All nodes between the starting node and the ending node have values less than or equal to the starting node (i.e. the starting node's value should be the maximum value along the path).
Return the number of distinct good paths.

Note that a path and its reverse are counted as the same path. For example, `0 -> 1` is considered to be the same as `1 -> 0`. A single node is also considered as a valid path.

### Example

![2421 example image](https://assets.leetcode.com/uploads/2022/08/04/f9caaac15b383af9115c5586779dec5.png)

```text
Input: vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
Output: 6
Explanation: There are 5 good paths consisting of a single node.
There is 1 additional good path: 1 -> 0 -> 2 -> 4.
(The reverse path 4 -> 2 -> 0 -> 1 is treated as the same as 1 -> 0 -> 2 -> 4.)
Note that 0 -> 2 -> 3 is not a good path because vals[2] > vals[0].
```

## Concept

## Solution

```python
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        res = n = len(vals)
        count = [Counter({vals[i]: 1}) for i in range(n)]
        edges = sorted([(max(vals[i], vals[j]), i, j) for i, j in edges])
        par = [-1] * n

        def find(n):
            if par[n] == -1:
                return n
            
            par[n] = find(par[n])
            return par[n]
            
        for v, i, j in edges:
            p_i, p_j = find(i), find(j)
            c_i, c_j = count[p_i][v], count[p_j][v]
            res += c_i * c_j
            par[p_i] = p_j
            count[p_j] = Counter({v: c_i + c_j})
        
        return res
```

> Time Complexity: $O(n\log n)$ \
> Space Complexity: $O(n)$

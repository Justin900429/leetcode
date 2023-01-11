# 1443 - Minimum Time to Collect All Apples in a Tree

## Problem Description

Given an undirected tree consisting of `n` vertices numbered from `0` to `n-1`, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at **vertex 0** and coming back to this vertex.

The edges of the undirected tree are given in the array `edges`, where `edges[i] = [ai, bi]` means that exists an edge connecting the vertices `ai` and `bi`. Additionally, there is a boolean array hasApple, where `hasApple[i] = true` means that vertex `i` has an apple; otherwise, it does not have any apple.

### Example

![1443 example](https://assets.leetcode.com/uploads/2020/04/23/min_time_collect_apple_1.png)

```text
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
Output: 8 
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  
```

## Concept

To find the minimum time for collecting the apples, we should visit all the child nodes first to know where the apples are. From the parent's perspective, we only have to add 2 to the result when the child is an apple or the child's subtree has apples. To visit all the nodes, we use DFS.

## Solution

```python
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for _ in range(n)]

        for f, s in edges:
            graph[f].append(s)
            graph[s].append(f)

        def find(cur, par):
            count = 0
            for child in graph[cur]:
                if par == child: continue
                child_count = find(child, cur)

                if child_count or hasApple[child]:
                    count += child_count + 2

            return count

        return find(0, -1)
```

> Time complexity: $O(n)$ \
> Space complexity: $O(h)$
>

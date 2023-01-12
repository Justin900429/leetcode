# 1519 - Number of Nodes in the Sub-Tree With the Same Label

## Problem Description

You are given a tree (i.e. a connected, undirected graph that has no cycles) consisting of `n` nodes numbered from `0`to `n - 1` and exactly `n - 1` edges. The root of the tree is the node `0`, and each node of the tree has a label which is a lower-case character given in the string labels (i.e. The node with the number `i` has the label `labels[i]`).

The edges array is given on the form `edges[i]` = `[ai, bi]`, which means there is an edge between nodes `ai` and `bi` in the tree.

Return an array of size `n` where `ans[i]` is the number of nodes in the subtree of the ith node which have the same label as node `i`.

A subtree of a tree `T` is the tree consisting of a node in T and all of its descendant nodes.

### Example

![1519 example image](https://assets.leetcode.com/uploads/2020/07/01/q3e1.jpg)

```text
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
Output: [2,1,1,1,1,1,1]
Explanation: Node 0 has label 'a' and its sub-tree has node 2 with label 'a' as well, thus the answer is 2. Notice that any node is part of its sub-tree.
Node 1 has a label 'b'. The sub-tree of node 1 contains nodes 1,4 and 5, as nodes 4 and 5 have different labels than node 1, the answer is just 1 (the node itself).
```

## Concept

Another DFS/iterative problem. We just explore the subtree and comput how many nodes have the same label as the parent node. Note that we don't have to create many count array for each node. We can save the previous num with a variable and get the number by subtracting the previous with current number.

$$
\text{Label in subtree} = \text{Visited} - \text{Not visited}
$$

## Solution

### Recursive

```python
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = [[] for _ in range(n)]
        res = [0] * n
        for f, s in edges:
            graph[f].append(s)
            graph[s].append(f)

        count = [0] * 26
        def find(cur, par):
            alpha = ord(labels[cur]) - ord('a')
            previous = count[alpha]
            count[alpha] += 1

            for child in graph[cur]:
                if child == par: continue
                find(child, cur)

            res[cur] = count[alpha] - previous

        find(0, -1)
        return res
```

> Time complexity: $O(n)$ \
> Space complexity: $O(n)$

### Iterative

[Visit here](https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/solutions/2864718/number-of-nodes-in-the-sub-tree-with-the-same-label/)

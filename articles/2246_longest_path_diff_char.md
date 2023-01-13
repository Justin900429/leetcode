# 2246 - Longest Path With Different Adjacent Characters

## Problem Description

You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of `n` nodes numbered from `0` to `n - 1`. The tree is represented by a `0-indexed` array parent of size n, where `parent[i]` is the parent of node i. Since node 0 is the root, `parent[0] == -1`.

You are also given a string `s` of length `n`, where `s[i]` is the character assigned to node `i`.

Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.

### Example

![2246 example image](https://assets.leetcode.com/uploads/2022/03/25/testingdrawio.png)

```text
Input: parent = [-1,0,0,1,1,2], s = "abacbe"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
It can be proven that there is no longer path that satisfies the conditions. 
```

## Concept

We can use DFS and search from the leafs. At each iteration, we compute the children's node depth and save the biggest $first$ and second biggest $second$. The length of node depth will be $first + second + 1$.

## Solution

The return in the below `find` function is the max length from the current node and the depth from the current node.

```python
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = [[] for _ in range(len(parent))]
        for idx in range(len(parent)):
            if idx != 0:
                graph[parent[idx]].append(idx)

        def find(cur, par):
            cur_max = 1
            first = 0
            second = 0

            for child in graph[cur]:
                if child != par:
                    next_n, depth = find(child, cur)

                    if s[cur] != s[child]:
                        if depth > first:
                            second = first
                            first = depth
                        elif depth > second:
                            second = depth

                cur_max = max(cur_max, first + second + 1, next_n)
            
            return cur_max, first + 1
        
        return find(0, -1)[0]
```

> Time complexity: $O(n)$ \
> Space complexity: $O(h)$

# 797 - All Paths From Source to Target

## Problem Description
Given a directed acyclic graph (DAG) of n nodes labeled from `0` to `n - 1`, find all possible paths from node `0` to node `n - 1` and return them in any order.

The graph is given as follows: $\text{graph[i]}$ is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node $\text{graph[i][j]}$).

### Example
![797 example 1](https://assets.leetcode.com/uploads/2020/09/28/all_1.jpg)

```text
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
```

> [Link to the page](https://leetcode.com/problems/all-paths-from-source-to-target/description/)

## Concept
This problem requires us to find all the path within a DAG. We can simply use backtracking and add node into current path. Due to DAG, we don't need extra boolean array to check whether current node is visited or not.

## Solution
```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        res = []
        temp = [0]
        def find(cur):
            # Reach the target
            if cur == len(graph) - 1:
                res.append(temp[:])
                return

            for nei in graph[cur]:
                temp.append(nei)
                find(nei)
                temp.pop()
        
        find(0)
        return res
```

The analysis of this problem is quite complex. First step, we imagine we have an array `[1, 2, 3, 4, ..., n - 1]` in the worst case. Due to the property of DAG, we have at most $n + (n - 1) + (n - 2) + ... + 1 \approx O(n^2)$ edges. Next, we want to calculate how many path we have in this case. For path length `k`, we have $n - 2 \choose k - 2$ choices. Therefore, the total number of path is $\sum_{k=3}^{n} {n - 2 \choose k - 2} = \sum_{k=1}^{n-2} {n - 2 \choose k}$. From binomial expansion of $(1 + x)^n = \sum_{k=0}^{n}{n \choose k}x^k$, we have $2^n=\sum_{k=0}^n {n \choose k}$. Therefore, we have number of path $\approx O(2^n)$. However, we should also consider the time for construting each path, which requires $O(n)$. Therefore, we have our final time complexity $O(n \times 2^n)$.

> Time complexity: $O(n\times2^n)$ \
> Space complexity: $O(n)$

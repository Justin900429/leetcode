# 2477 - Minimum Fuel Cost to Report to the Capital

## Problem Description

There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of n cities numbered from `0` to `n - 1` and exactly `n - 1` roads. The capital city is city 0. You are given a 2D integer array `roads` where `roads[i] = [ai, bi]` denotes that there exists a bidirectional road connecting cities `ai` and `bi`.

There is a meeting for the representatives of each city. The meeting is in the capital city.

There is a car in each city. You are given an integer `seats` that indicates the number of seats in each car.

A representative can use the car in their city to travel or change the car and ride with another representative. The cost of traveling between two cities is one liter of fuel.

*Return the minimum number of liters of fuel to reach the capital city.*

### Example

![2477 example image](https://assets.leetcode.com/uploads/2022/09/22/a4c380025e3ff0c379525e96a7d63a3.png)

```text
Input: roads = [[0,1],[0,2],[0,3]], seats = 5
Output: 3
Explanation: 
- Representative1 goes directly to the capital with 1 liter of fuel.
- Representative2 goes directly to the capital with 1 liter of fuel.
- Representative3 goes directly to the capital with 1 liter of fuel.
It costs 3 liters of fuel at minimum. 
It can be proven that 3 is the minimum number of liters of fuel needed.
```

## Concept

We use DFS to go thought all the subtree node. At each node, we calculate the number of nodes in the subtree and the cost of the subtree. The cost of the subtree is the sum of the cost of the subtree and the cost of the current node. We devide the num seat to decide how many cars we need to use to travel to the capital.

## Solution

```python
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        res = 0
        graph = defaultdict(list)
        for i, j in roads:
            graph[i].append(j)
            graph[j].append(i)

        def find(cur, par):
            all_count, cost = 1, 0

            for child in graph[cur]:
                if child != par:
                    child_count, child_cost= find(child, cur)
                    all_count += child_count
                    cost += child_cost + (child_count - 1) // seats + 1
            
            return all_count, cost

        return find(0, -1)[1]
```

> Time complexity: $O(|V| + |E|)$ \
> Space complexity: $O(|V| + |E|)$

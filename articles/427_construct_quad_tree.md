# 427 - Construct Quad Tree

## Problem Description

Given a `n * n` matrix grid of 0's and 1's only. We want to represent the `grid` with a Quad-Tree.

Return *the root of the Quad-Tree* representing the `grid`.

Notice that you can assign the value of a node to **True** or **False** when `isLeaf` is **False**, and both are **accepted** in the answer.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

* `val`: True if the node represents a grid of 1's or False if the node represents a grid of 0's.
* `isLeaf`: True if the node is leaf node on the tree or False if the node has the four children.

```java
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
```

We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all `1's` or all `0's`) set isLeaf True and set `val` to the value of the grid and set the four children to Null and stop.

If the current grid has different values, set `isLeaf` to False and set `val` to any value and divide the current grid into four sub-grids as shown in the photo.

Recurse for each of the children with the proper sub-grid.

![427 description image](https://assets.leetcode.com/uploads/2020/02/11/new_top.png)

If you want to know more about the Quad-Tree, you can refer to the [wiki](https://en.wikipedia.org/wiki/Quadtree).

**Quad-Tree format:**

The output represents the serialized format of a Quad-Tree using level order traversal, where `null` signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list `[isLeaf, val]`.

If the value of `isLeaf` or `val` is True we represent it as 1 in the list `[isLeaf, val]` and if the value of `isLeaf` or `val` is False we represent it as **0**.

### Example

![427 example image](https://assets.leetcode.com/uploads/2020/02/11/grid1.png)

```text
Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represnts False and 1 represents True in the photo representing the Quad-Tree.
```

![427 solution image](https://assets.leetcode.com/uploads/2020/02/12/e1tree.png)

> [Link to the problem](https://leetcode.com/problems/construct-quad-tree)

## Concept

In order to construct the quad tree, we can recursivly check and build the tree. The checking process can be done by checking the overall value of the grid, if all the values are the same, then we can set the `isLeaf` to `True` and set the `val` to the value of the grid. Otherwise, we can set the `isLeaf` to `False` and set the `val` to any value. Then we can divide the grid into four sub-grids and recursivly build the tree.

## Solution

```python
class Solution:
    def check(self, grid):
        return all([grid[0][0] == grid[i][j] for i in range(len(grid)) for j in range(len(grid[0]))])
        
    def construct(self, grid: List[List[int]]) -> 'Node':        
        n = len(grid)
        # Check overall:
        if self.check(grid):
            return Node(grid[0][0], True, None, None, None, None)
        else:
            return Node(
                1, False,
                self.construct([row[:n//2] for row in grid[:n//2]]),
                self.construct([row[n//2:] for row in grid[:n//2]]),
                self.construct([row[:n//2] for row in grid[n//2:]]),
                self.construct([row[n//2:] for row in grid[n//2:]])
            )
```

> Time Complexity: $O(n^2\log_4n)=O(n^2\log n)$ \
> Space Complexity: $O(n^2)$

Note that the time complexity is computed by:

```text
n^2                                                -|
|                                                   |
n^2/4 - n^2/4 - n^2/4 - n^2/4                       |
|         |       | ...                             |
|         |                                         | log_4(n)
|         n^2/16 - n^2/16 - n^2/16 - n^2/16         |
n^2 / 16 - n^2 / 16 - n^2 / 16 - n^2 / 16           |
| ...                                              -|
```

$\rightarrow O(n^2\log_4n)=O(n^2\log n)$

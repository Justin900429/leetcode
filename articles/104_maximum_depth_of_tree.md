# 104 - Maximum Depth of Binary Tree

## Problem Description

Given the `root` of a binary tree, return its *maximum* depth.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

### Example

![example image of 104](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

```text
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

## Concept

Recursively find the depth of the current node. The depth of a current ndoe can be computed by:

$$
\text{Depth}(node) = \max(\text{Depth(left)}, \text{Depth(right)}) + 1
$$

## Python

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1
```

> Time Complexity: $O(n)$ \
> Space Complexity: $O(h)$

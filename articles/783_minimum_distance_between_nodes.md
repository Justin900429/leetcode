# 783 - Minimum Distance Between BST Nodes

## Problem Description

Given the `root` of a Binary Search Tree (BST), return *the minimum difference between the values of any two different nodes in the tree*.

### Example

![783 example image](https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg)

```text
Input: root = [4,2,6,1,3]
Output: 1
```

> [Link to the problem](https://leetcode.com/problems/minimum-distance-between-bst-nodes)

## Concept

To compute the minimum distance between nodes within BST, we only need to check the successive node.

## Solution

```python
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        get = []
        def in_order(root):
            if not root:
                return
            
            in_order(root.left)
            get.append(root.val)
            in_order(root.right)
        
        in_order(root)
        res = 10**9
        for idx in range(len(get) - 1):
            res = min(res, abs(get[idx] - get[idx + 1]))
        return res
```

> Time Complexity: $O(n)$ \
> Space Complexity: $O(n)$

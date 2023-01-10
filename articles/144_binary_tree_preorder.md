# 144 - Binary Tree Preorder Traversal

## Problem Description

Given the `root` of a binary tree, return the *preorder traversal* of its nodes' values.

### Example

![144 Example](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)

```text
Input: root = [1,null,2,3]
Output: [1,2,3]
```

> [Link to the problem](https://leetcode.com/problems/binary-tree-preorder-traversal/)

## Concept

The problem requires us to do the preorder traversal, which can be achieved in two ways: iterative and recursive.

## Solution

### Recursive

The recursive solution is intuitive.

```python
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def find(root):
            if root is None: return

            res.append(root.val)
            find(root.left)
            find(root.right)

        find(root)
        return res
        
```

> Time Complexity: $O(n)$ \
> Space Complexity: $O(n)$

### Iterative

To implement the interative solution, we can maintain a stack. Note that we should first put the right node before the left node because we need to **pop out the left node first**.

```python
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        if root is None: return res
        stack = [root]

        while stack:
            cur = stack.pop()
            res.append(cur.val)

            if cur.right is not None:
                stack.append(cur.right)
            
            if cur.left is not None:
                stack.append(cur.left)

        return res
```

> Time Complexity: $O(n)$ \
> Space Complexity: $O(n)$

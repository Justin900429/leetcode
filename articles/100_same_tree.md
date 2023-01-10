# 100 - Same Tree

## Problem Description

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

### Example

![100 example image](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

```text
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

## Concept

The same tree means the tree structure is all the same. The better way to describe it is:

1. Current node of `p` and `q` have the same value
2. Left subtree of `p` and `q` are the same
3. Right subtree of `p` and `q` are the same

## Solution

### Recursive

```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        
        elif p is None or q is None:
            return False

        return p.val == q.val and \
               self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)
```

> Time Complexity: $O(n)$ \
> Space Complexity: $O(1)$
>

Note that using recursive method still has stack memory in the system, which is $O(h)$, where $h$ is the tree height.

### Iterative

```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            cur_p, cur_q = stack.pop()

            if cur_p is None and cur_q is None:
                continue

            if cur_p is None or cur_q is None or (cur_p.val != cur_q.val):
                return False

            stack.append((cur_p.left, cur_q.left))
            stack.append((cur_p.right, cur_q.right))

        return True
            

```

> Time Complexity: $O(n)$ \
> Space Complexity: $O(h)$
>
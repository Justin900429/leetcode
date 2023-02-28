# 652 - Find Duplicate Subtrees

## Problem Description

Given the `root` of a binary tree, return all **duplicate subtrees**.

For each kind of duplicate subtrees, you only need to return the root node of any **one** of them.

Two trees are **duplicate** if they have the **same structure** with the **same node values**.

### Example

![652 example image](https://assets.leetcode.com/uploads/2020/08/16/e1.jpg)

## Concept

To find the tree with same structure, we recursivly check the subtree by encoding the tree into a string. At each node, we save string into a hashmap, and if the string has been seen before, we add the node to the result. Note that each string can only be added once.

## Solution

```python
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        find = defaultdict(int)

        def recurse(node):
            if node is None:
                return "#"

            path = ",".join([str(node.val), recurse(node.left), recurse(node.right)])

            find[path] += 1
            if find[path] == 2:
                res.append(node)
                
            return path
        
        recurse(root)
        return res
```

> Time complexity: $O(n)$ \
> Space complexity: $O(n)$

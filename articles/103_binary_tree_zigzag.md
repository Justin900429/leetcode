# 103 - Binary Tree Zigzag Level Order Traversal

## Problem Description

Given the `root` of a binary tree, return the *zigzag level order traversal of its nodes' values*. (i.e., from left to right, then right to left for the next level and alternate between).

### Example

![103 example image](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

```text
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
```

## Concept

To reverse the order of the list, we use a flag to indicate whether we should change the order. The rest are the same as the level order traversal.

## Solution

```python
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        res = []

        queue = deque([root])
        turn = 0
        while queue:
            temp = []
            for _ in range(len(queue)):
                cur = queue.popleft()

                if cur.left is not None:
                    queue.append(cur.left)
                
                if cur.right is not None:
                    queue.append(cur.right)
                
                temp.append(cur.val)
            
            if turn:
                temp = reversed(temp)
            res.append(temp)
            turn = 1 - turn
        
        return res
```

> Time complexity: $O(n)$ \
> Space complexity: $O(n)$

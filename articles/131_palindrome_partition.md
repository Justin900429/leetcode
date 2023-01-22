# 131 - Palindrome Partitioning

## Problem Description

Given a string `s`, partition `s` such that every  substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.

### Example

```text
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

> [Link to the problem](https://leetcode.com/problems/palindrome-partitioning)

## Concept

## Solution

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        table = [[0] * len(s) for _ in range(len(s))]

        for idx in range(len(table)):
            for idy in range(idx + 1):
                if abs(idx - idy) <= 2:
                    table[idy][idx] = s[idx] == s[idy]
                else:
                    table[idy][idx] = table[idy + 1][idx - 1] and s[idx] == s[idy]
        
        res = []
        temp = []

        def find(cur):
            if cur == len(table):
                res.append(temp[:])
                return

            for idx in range(cur, len(table)):
                if table[cur][idx]:
                    temp.append(s[cur:idx+1])
                    find(idx + 1)
                    temp.pop()
                
        find(0)
        return res
```

> Time complexity: $O(1)$ \
> Space complexity: $O(s^2)$

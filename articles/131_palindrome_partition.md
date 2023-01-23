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

The backtracking step is quite intuitive, we just iterate the string from current starting index, and check to which index is still a palindrome and start from a new round. The difficult part is to quickly check the palindrome for the given starting and ending points. The proper way is to apply dp with a 2D table, where $\text{T[i][j]}$ means whether string `s` is a palindrome from index $i$ to index $j$. The recurrence can be written as:

$$
\text{T[i][j]} = 
\begin{cases}
\text{T[i + 1][j - 1]} &, \text{if s[i] = s[j]} \\
1 &, \text{if s[i]=s[j] and abs(i - j)} \le \text{2} \\
0 &, otherwise
\end{cases}
$$

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

> Time complexity: $O(n \times 2^n)$ \
> Space complexity: $O(n^2)$

Note that the time complexity is obtained by ${n - 1 \choose 1} + {n - 1 \choose 2} + \cdots + {n - 1 \choose n - 1} = O(2^{n - 1}) = O(2^n)$ with another $O(n)$ to build each partition.

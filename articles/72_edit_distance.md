# 72 - Edit Distance

## Problem Description

Given two strings `word1` and `word2`, return *the minimum number of operations required to convert `word1` to `word2`*.

You have the following three operations permitted on a word:

* Insert a character
* Delete a character
* Replace a character

### Example

```text
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

> [Link to the problem](https://leetcode.com/problems/edit-distance)

## Concept

To find the minimum number of operations required to convert `word1` to `word2`, we can use dynamic programming. We can define a 2D array `dp` where `dp[i][j]` represents the minimum number of operations required to convert `word1[:i]` to `word2[:j]`. We can then use the following recurrence relation to fill up the array:

$$
\text{dp[i][j]} = \min(\text{dp[i - 1][j]}, \text{dp[i][j - 1]}, \text{dp[i - 1][j - 1]}) + 1
$$

Note that $\text{dp[i - 1][j]}$ means deleting the first word from word $i$, $\text{dp[i][j - 1]}$ means inserting the word from word $j$, and $\text{dp[i - 1][j - 1]} means replacing the word.

## Solution

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for idx in range(m + 1):
            dp[idx][0] = idx

        for idx in range(n + 1):
            dp[0][idx] = idx

        for idx in range(1, m + 1):
            for idy in range(1, n + 1):
                if word1[idx - 1] == word2[idy - 1]:
                    dp[idx][idy] = dp[idx - 1][idy - 1]
                else:
                    dp[idx][idy] = min(
                        dp[idx - 1][idy],
                        dp[idx][idy - 1],
                        dp[idx - 1][idy - 1]
                    ) + 1

        return dp[m][n]
```

> Time Complexity: $O(mn)$ \
> Space Complexity: $O(mn)$

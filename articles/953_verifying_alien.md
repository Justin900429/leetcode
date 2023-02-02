# 953 - Verifying an Alien Dictionar

## Problem Description

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different `order`. The `order` of the alphabet is some permutation of lowercase letters.

Given a sequence of `words` written in the alien language, and the `order` of the alphabet, return `true` if and only if the given `words` are sorted lexicographically in this alien language.

### Example

```text
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
```

> [Link to the problem](https://leetcode.com/problems/verifying-an-alien-dictionary/)

## Concept

To verify the sequence is sorted or not, we only have to verify the adjacent word. Because if the sequence $a, b, c, \cdots$ is sorted, we have $a \le b \le c \le \cdots$. Therefore, checking the adjacent word is enough for us to check the order.

## Solution

We maintain a hash for projecting the word to the number for checking the adjancent order.

```python
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        num_map = {chr: num for num, chr in enumerate(order)}

        for idx in range(len(words) - 1):
            for idy in range(len(words[idx])):
                if idy == len(words[idx + 1]):
                    return False
                if num_map[words[idx][idy]] > num_map[words[idx + 1][idy]]:
                    return False
                elif num_map[words[idx][idy]] < num_map[words[idx + 1][idy]]:
                    break
        
        return True
```

$M: \text{Number of charaters in the words}$
> Time complexity: $O(M)$ \
> Space complexity: $O(1)$

Note that we have space complexity $O(1)$ because the hash size is always 26.

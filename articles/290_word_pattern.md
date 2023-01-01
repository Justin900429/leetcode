# 290 - Word Pattern

## Problem Description

Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `s`.

### Example

```text
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
```

## Concept

The key concept of this question is the word **bijection**. Bijection means that each element should be **1 to 1**. Therefore, we cannot connect multiple patterns to a single word. To save the relationship between patterns and words, we can maintain a hash table and check whether each pattern match to a unique word.

## Solution

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")

        # Check 1-to-1 by couting the unique patterns and words.
        # Using length to check whether each string or pattern
        #  can be covered by each other
        if len(set(pattern)) != len(set(s)) or len(pattern) != len(s):
            return False

        find = dict()
        for idx in range(len(pattern)):
            if pattern[idx] not in find:
                find[pattern[idx]] = s[idx]
            else:
                if find[pattern[idx]] != s[idx]:
                    return False

        return True
```

> Time Complexity: $O(n)$ \
> Space Complexity: $O(n)$

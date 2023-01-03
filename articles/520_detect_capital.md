# 520 - Detect Capital

## Problem Description

We define the usage of capitals in a word to be right when one of the following cases holds:

* All letters in this word are capitals, like `"USA"`.
* All letters in this word are not capitals, like `"leetcode"`.
* Only the first letter in this word is capital, like `"Google"`.

Given a string word, return true if the usage of capitals in it is right.

### Example

```text
Input: word = "USA"
Output: true

Input: word = "FlaG"
Output: false
```

> [Link to the page](https://leetcode.com/problems/detect-capital/)

## Concept

Just consider all three cases. If any of it is true, return true. Otherwise, return false.

## Solution

```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if all([temp.isupper() for temp in word]):
            return True
        elif all([not temp.isupper() for temp in word]):
            return True
        elif word[0].isupper() and all([not temp.isupper() for temp in word[1:]]):
            return True

        return False
```

> Time Complexity: $O(n)$ \
> Space Complexity: $O(1)$

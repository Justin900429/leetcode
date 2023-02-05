# 438 - Find All Anagrams in a String

## Problem Description

Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in any order.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Example

```text
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

> [Link to the problem](https://leetcode.com/problems/find-all-anagrams-in-a-string/description/)

## Concept

Maintain a hash table to count the charaters of string `p`. Also, we create a sliding window with the same length as `p` and check through all the string with another hash table.

## Solution

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pattern = [0] * 26
        for char in p:
            pattern[ord(char) - ord('a')] += 1

        sub_pattern_of_s = [0] * 26
        for char in s[:len(p)]:
            sub_pattern_of_s[ord(char) - ord('a')] += 1

        res = []
        for idx in range(len(p), len(s) + 1):
            if all([pattern[idy] == sub_pattern_of_s[idy] for idy in range(26)]):
                res.append(idx - len(p))

            sub_pattern_of_s[ord(s[idx - len(p)]) - ord('a')] -= 1
            if idx < len(s):
                sub_pattern_of_s[ord(s[idx]) - ord('a')] += 1
        
        return res
```

> Time complexity: $O(n)$ \
> Space complexity: $O(1)$

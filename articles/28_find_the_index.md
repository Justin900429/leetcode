# 28 - Find the Index of the First Occurrence in a String

## Problem Description

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

### Example

```text
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```

> [Link to the problem](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string)

## Concept

To find the index of the array, we can simply iterate through the string and check if the substring of the same length as `needle` is equal to the `needle`. Return the index if the `needle` is found. Otherwise, return `-1`.

## Solution

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for idx in range(len(haystack)):
            if idx + len(needle) <= len(haystack) and haystack[idx:idx+len(needle)] == needle:
                return idx

        return -1
```

> Time Complexity: $O(mn)$ \
> Space Complexity: $O(m)$

# 567 - Permutation in String

## Problem Description

Given two strings `s1` and `s2`, return true if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return true if one of `s1`'s permutations is the substring of `s2`.

### Example

```text
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

## Concept

This problem requires us to search the `s1`in the substring of `s2`. The best way is to maintain two hash to compare the string `s1` and substring of `s2`. We create a sliding window having the same length as `s1` to obtain the substring of `s2`. Return true if the hash table is the same otherwise move the window one charater forward. To update the hash table, we only need to check the first and the very next last of the sliding window.

## Solution

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        voc_count_s1 = [0] * 26
        for c in s1:
            voc_count_s1[ord(c) - ord('a')] += 1

        voc_count_sub_s2 = [0] * 26
        for c in s2[:len(s1)]:
            voc_count_sub_s2[ord(c) - ord('a')] += 1

        for idx in range(len(s1), len(s2) + 1):
            if all([voc_count_s1[idy] == voc_count_sub_s2[idy] for idy in range(26)]):
                return True

            voc_count_sub_s2[ord(s2[idx - len(s1)]) - ord('a')] -= 1
            if idx < len(s2):
                voc_count_sub_s2[ord(s2[idx]) - ord('a')] += 1

        return False
```

> Time complexity: $O(\text{len(s1)}\times (\text{len(s2) - len(s1)}))$ \
> Space complexity: $O(1)$

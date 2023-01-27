# 472 - Concatenated Words

## Problem Description

Given an array of strings `words` **(without duplicates)**, return all the **concatenated words** in the given list of `words`.

A **concatenated word** is defined as a string that is comprised entirely of at least two shorter words in the given array.

### Example

```text
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
```

> [Link to the problem](https://leetcode.com/problems/concatenated-words/description/)

## Concept

To find the concatenated words, we can separated a words into its prefix and suffix. Later, we check whether the prefix is in the list and recursively search the answer for the suffix. Note that we can also search the suffix from the `words` first.

See also other [solutions](https://leetcode.com/problems/concatenated-words/solutions/2822170/concatenated-words/).

## Solution

```python
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        @lru_cache(None)
        def dfs(word):
            for i in range(1, len(word)):
                prefix, suffix = word[:i], word[i:]
                if prefix in words and suffix in words:
                    return True
                if prefix in words and dfs(suffix):
                    return True
            return False
        return [word for word in words if dfs(word)]
```

> Time Complexity: $O(m^3n)$ \
> Space Complexity: $O(mn)$

$n$ is the number of word in the list `words` and $m$ is the maximum length of word with the `words`. The time complexity is $O(m^3n)$ because each dfs requires $O(m^3)$ (search in set $O(m)$ for computing the hash, dfs has $O(m)$ state, separate prefix and suffix with $O(m)$).

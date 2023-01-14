# 1061 - Lexicographically Smallest Equivalent String

## Problem Description

You are given two strings of the same length s1 and s2 and a string baseStr.

We say `s1[i]` and `s2[i]` are equivalent characters.

For example, if `s1 = "abc"` and `s2 = "cde"`, then we have `'a' == 'c'`, `'b' == 'd'`, and `'c' == 'e'`.
Equivalent characters follow the usual rules of any equivalence relation:

**Reflexivity**: `'a' == 'a'`.
**Symmetry**: `'a' == 'b'` implies `'b' == 'a'`.
**Transitivity**: `'a' == 'b'` and `'b' == 'c'` implies `'a' == 'c'`.

For example, given the equivalency information from `s1 = "abc"` and `s2 = "cde"`, `"acd"` and `"aab"` are equivalent strings of `baseStr = "eed"`, and `"aab"` is the lexicographically smallest equivalent string of `baseStr`.

Return the lexicographically smallest equivalent string of `baseStr` by using the equivalency information from `s1` and `s2`.

### Example

```text
Input: s1 = "parker", s2 = "morris", baseStr = "parser"
Output: "makkek"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
The characters in each group are equivalent and sorted in lexicographical order.
So the answer is "makkek".
```

> [Link to the problem](lexicographically-smallest-equivalent-string)

## Concept

The problem requires us to cluster all the equivalent to gether and find the smallest one for each cluster. We can easily implement this one with Union Tree.

## Solution

The key concept is that we use lexicographically order to decide which charater should be the root during union operation.

```python
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        par = [-1] * 26

        def find(cur):
            if par[cur] == -1:
                return cur
            
            par[cur] = find(par[cur])
            return par[cur]

        def union(f, s):
            f_p = find(f)
            s_p = find(s)

            # Use the smaller one as the root
            if f_p > s_p:
                par[f_p] = s_p
            elif f_p < s_p:
                par[s_p] = f_p

        for idx in range(len(s1)):
            union(ord(s1[idx]) - ord('a'), ord(s2[idx]) - ord('a'))

        res = ""        
        for base in baseStr:
            res += chr(find(ord(base) - ord('a')) + ord('a'))
        
        return res
```

> Time Complexity: $O((N + M)\log(26))$ \
> Space Complexity: $O(26)$

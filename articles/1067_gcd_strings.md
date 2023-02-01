# 1071 - Greatest Common Divisor of Strings

## Problem Description

For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s = t + ... + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`.

### Example

```text
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
```

> [Link to the problem](https://leetcode.com/problems/greatest-common-divisor-of-strings/)

## Concept

We just try all the substring from the smaller string. For example, we use `str2` and search from `ABC`, `AB`, `A`. We can stop searching at `ABC` because it can compose `str1`.

## Solution

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        small = str2 if len(str2) < len(str1) else str1
        big = str1 if len(str1) > len(str2) else str2
        
        for idx in range(len(small), 0, -1):
            gcd = small[:idx]

            if len(small) % len(gcd) or len(big) % len(gcd):
                continue

            small_length = len(small) // len(gcd)
            big_length = len(big) // len(gcd)
            if small_length * gcd == small and big_length * gcd == big:
                return gcd

        return ""
```

> Time complexity: $O(\min(m, n) \times (m + n))$ \
> Space complexity: $O(\min(m, n))$

Another better solution can be found at [here](https://leetcode.com/problems/greatest-common-divisor-of-strings/solutions/3024822/greatest-common-divisor-of-strings/).

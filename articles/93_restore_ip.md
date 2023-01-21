# 93 - Restore IP Addresses

## Problem Description

A **valid IP address** consists of exactly four integers separated by single dots. Each integer is between `0` and `255` (**inclusive**) and cannot have leading zeros.

For example, `"0.1.2.201"` and `"192.168.1.1"` are **valid** IP addresses, but `"0.011.255.245"`, `"192.168.1.312"` and `"192.168@1.1"` are invalid IP addresses.
Given a string `s` containing only digits, return *all possible valid IP* addresses that can be formed by inserting dots into `s`. You are **not** allowed to reorder or remove any digits in `s`. You may return the valid IP addresses in **any** order.

### Example

```text
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
```

> [Link to the problem](https://leetcode.com/problems/restore-ip-addresses/)

## Concept

Firstly, we remove the string length greater than 12. Later, we just backtrack the string and do two things:

1. Add a new section to the IP if the number of section is smaller than 4
2. Append current num to the previous section if previous section has no leading zero and result is smaller than 255

We add the IP address if it has four section. In our algorthm, we don't have to test the correctness in the final round but only the number of section should equal to four.

## Solution

```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
            
        res = []

        def find(cur, temp):
            if cur == len(s):
                if len(temp) == 4:
                    res.append(".".join(temp))
                return

            if len(temp) < 4:
                temp.append(s[cur])
                find(cur + 1, temp)
                temp.pop()
            
            if temp and \
               int(temp[-1]) * 10 + int(s[cur]) <= 255 and \
               int(temp[-1][0]) != 0:
                temp[-1] += s[cur]
                find(cur + 1, temp)
        
        temp = []
        find(0, temp)
        return res
```

> Time complexity: $O(1)$ \
> Space complexity: $O(1)$

Note that the space complexity is $O(1)$ is because we only requires at most $12 \ (3 \times 4)$ string places and, the time complexity is $O(1)$ because the answer should defintely be smaller than $255^4$ which can viewed as the constant time .

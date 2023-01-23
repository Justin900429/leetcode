# 997 - Find the Town Judge

## Problem Description

In a town, there are `n` people labeled from `1` to `n`. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties **1** and **2**.
You are given an array `trust` where `trust[i] = [ai, bi]` representing that the person labeled `ai` trusts the person labeled `bi`.

Return the label of the town judge if the town judge exists and can be identified, or return `-1` otherwise.

### Example

```text
Input: n = 2, trust = [[1,2]]
Output: 2
```

> [Link to the problem](https://leetcode.com/problems/find-the-town-judge)

## Concept

The problem can be formulated into a graph problem but we can still solve it without using the concept of graph but with only two array. The $i^{th}$ entry of the first array records how many people $i^{th}$ trusts. The $i^{th}$ entry of the second array records how many people trust $i^{th}$ person. We should check two things:

1. There is only one person who is trusted by every person except himself.
2. The person who is trusted by all the others doesn't trust anyone

## Solution

```python
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_other = [0] * n
        has_trust = [0] * n

        for f, s in trust:
            has_trust[f - 1] += 1
            trust_other[s - 1] += 1
        
        has = 0
        res = None
        for idx in range(len(trust_other)):
            if trust_other[idx] == n - 1 and has_trust[idx] == 0:
                res = idx + 1   
                has += 1

        return res if has == 1 else -1
```

> Time complexity: $O(n)$ \
> Space complexity: $O(n)$

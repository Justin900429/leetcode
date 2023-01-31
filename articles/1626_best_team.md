# 1626 - Best Team With No Conflicts

## Problem Description

You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.

However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

Given two lists, scores and ages, where each `scores[i]` and `ages[i]` represents the score and age of the `ith` player, respectively, return the highest overall score of all possible basketball teams.

```text
Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
Output: 34
Explanation: You can choose all the players.
```

## Concept

We sort the age in ascending order and create a `dp` array, where `dp[i]` means the maximum score start from index `0` to index `i`. Then, we have the relations:

$$
\text{dp[i]} = \underset{\text{scores[i]} \ge \text{scores[j]}}{\max}(\text{dp[i]}, \text{scores[i]} + \text{dp[j]})
$$

## Solution

```python
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        combine = sorted([[age, score] for score, age in zip(scores, ages)])

        dp = [combine[idx][1] for idx in range(len(scores))]
        max_res = max(dp)

        for idx in range(len(scores)):
            for idy in range(idx):
                if combine[idx][1] >= combine[idy][1]:
                    dp[idx] = max(dp[idx], combine[idx][1] + dp[idy])
            max_res = max(max_res, dp[idx])
        
        return max_res
```

> Time complexity: $O(n^2)$ \
> Space complexity: $O(h)$

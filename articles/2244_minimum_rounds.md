# 2244 - Minimum Rounds to Complete All Tasks

## Description

You are given a 0-indexed integer array $\text{tasks}$, where $\text{tasks[i]}$ represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.

Return the minimum rounds required to complete all the tasks, or `-1` if it is not possible to complete all the tasks.

### Example

```text
Input: tasks = [2,2,3,3,2,4,4,4,4,4]
Output: 4
Explanation: To complete all the tasks, a possible plan is:
- In the first round, you complete 3 tasks of difficulty level 2. 
- In the second round, you complete 2 tasks of difficulty level 3. 
- In the third round, you complete 3 tasks of difficulty level 4. 
- In the fourth round, you complete 2 tasks of difficulty level 4.  
It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.
```

> [Link to the problem](https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/)

## Concept

Because the problem only allow us to finish the same level of tasks within a round, we should maintain a hash table to save the number of each task. Latter, we can greedily compute how many rounds we need to finish each level of task.

## Solution

```python
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        find = defaultdict(int)
        for task in tasks:
            find[task] += 1

        count = 0
        for value in find.values():
            if value == 1:
                return -1
            count += math.ceil(value / 3)

        return count
```

> Time complexity: $O(n)$ \
> Space complexity: $O(n)$

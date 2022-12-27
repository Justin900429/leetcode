# 2389 - Longest Subsequence With Limited Sum

## Problem Description
You are given an integer array nums of length $n$, and an integer array queries of length $m$.

Return an array answer of length m where $\text{answer[i]}$ is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to $\text{queries[i]}$.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

### Example 1
```text
Input: nums = [4,5,2,1], queries = [3,10,21]
Output: [2,3,4]
Explanation: We answer the queries as follows:
- The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
- The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
- The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.
```

> [Link to the page.](https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/)

## Concept
Observing that the word **subsequence** can be changed to **subelement** cause we can remove the unwanted element without considering the order in this problem. For example, from the above example, we can view the sequence `[2, 1]` as `[1, 2]`. Therefore, we just change this problem into greedy one.

## Solution

### Slower solution
For each entry in the $\text{queries}$, we start from the smallest element in the $\text{nums}$ and accumulate the number till the end. Note that we cannot surpass the numbers in the queries.

```python
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = [0] * len(queries)
        nums.sort()

        for idx in range(len(queries)):
            cur = amount = 0
            while cur < len(nums):
                # Ensure the accumulation will not exceed the query
                if amount + nums[cur] <= queries[idx]:
                    amount += nums[cur]
                    ans[idx] += 1
                else:
                    break
                cur += 1
        
        return ans
```
> Time Complexity: $O(mn)$ \
> Space Complexity: $O(m)$

### Better solution
Instead of summing up the $\text{nums}$ one by one, we can make a prefix-sum array and do the binary search for each num in the queries.

#### Example
```
nums: [3, 2, 1]
queries: [5]

1. Sort the nums -> [1, 2, 3]
2. Find the prefix sum -> [1, 3, 6]
3. Perform binary search -> [1, 3, [5], 6] -> ans[0] = 2
```

```python
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = [0] * len(queries)
        nums.sort()

        # Find the prefix sum
        prefix = [nums[0]] * len(nums)
        for idx in range(1, len(nums)):
            prefix[idx] = nums[idx] + prefix[idx - 1]

        for idx in range(len(queries)):
            # Do the binary search for index
            ans[idx] = bisect.bisect_right(prefix, queries[idx])
        return ans
```

> Time Complexity: $O(\max(m, n)\log{n})$ \
> Space Complexity: $O(m)$
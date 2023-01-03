# 944 - Delete Columns to Make Sorted

## Problem Description

You are given an array of n strings `strs`, all of the same length `k`.

The strings can be arranged such that there is one on each line, making a grid. For example, strs = `["abc", "bce", "cae"]` can be arranged as:

```text
abc
bce
cae
```

You want to **delete** the columns that are **not sorted lexicographically**. In the above example (0-indexed), columns 0 (`'a'`, `'b'`, `'c'`) and 2 (`'c'`, `'e'`, `'e'`) are sorted while column 1 (`'b'`, `'c'`, `'a'`) is not, so you would delete column 1.

Return the number of columns that you will delete.

### Example

```text
Input: strs = ["cba","daf","ghi"]
Output: 1
Explanation: The grid looks as follows:
  cba
  daf
  ghi
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.
```

> [Link to the problem](https://leetcode.com/problems/delete-columns-to-make-sorted/description/)

## Concept

We only need to iterate each column once and check whether each column is sorted or not.

## Solution

```python
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for col in range(len(strs[0])):
            for idx in range(len(strs) - 1):
                if strs[idx][col] > strs[idx + 1][col]:
                    count += 1
                    break

        return count
```

> Time complexity: $O(nk)$ \
> Space complexity: $O(1)$

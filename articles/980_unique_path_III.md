# 980 - Unique Paths III

## Problem Description

You are given an `m x n` integer array grid where `grid[i][j]` could be:

* `1` representing the starting square. There is exactly one starting square.
* `2` representing the ending square. There is exactly one ending square.
* `0` representing empty squares we can walk over.
* `-1` representing obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

### Example
![980 example image](https://assets.leetcode.com/uploads/2021/08/02/lc-unique1.jpg)

```text
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
```

## Concept
Finding the unique path to cover all the non-obstacle square can be easily solved with backtracking. We can first save the **start point** and the **end point** and change the **end point** and **obstacle** to `1`, and **start point** to 0. When we visit a point, we change it to 1 and compute the total sum of the `grid` when we reach the end point. The sum should equal to `len(grid) * len(grid[0])` indicating all the squares had been covered.

## Solution
```python
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start_x = start_y = None
        end_x = end_y = None
        # Finding start, end point and change the value of squares
        for idx in range(len(grid)):
            for idy in range(len(grid[0])):
                if grid[idx][idy] == 1:
                    start_x = idx
                    start_y = idy
                    grid[idx][idy] = 0
                elif grid[idx][idy] == 2:
                    end_x = idx
                    end_y = idy
                    grid[idx][idy] = 1
                elif grid[idx][idy] == -1:
                    grid[idx][idy] = 1

        count = 0
        def find(cur_x, cur_y):
            nonlocal end_x, end_y, count

            # Check whether all the squares had been covered
            if cur_x == end_x and cur_y == end_y:
                count += sum(sum(temp) for temp in grid) == (len(grid[0]) * len(grid))
                return

            # Check the boundaries
            if cur_x < 0 or cur_x >= len(grid) or cur_y < 0 or cur_y >= len(grid[0]) or grid[cur_x][cur_y] == 1:
                return


            grid[cur_x][cur_y] = 1

            find(cur_x - 1, cur_y)
            find(cur_x + 1, cur_y)
            find(cur_x, cur_y - 1)
            find(cur_x, cur_y + 1)

            grid[cur_x][cur_y] = 0

        find(start_x, start_y)
        return count
```

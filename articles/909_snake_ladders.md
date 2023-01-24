# 909 - Snakes and Ladders

## Problem Description

You are given an `n x n` integer matrix `board` where the cells are labeled from `1` to $n^2$ in a Boustrophedon style starting from the bottom left of the board (i.e. `board[n - 1][0]`) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range `[curr + 1, min(curr + 6, n2)]`.
This choice simulates the result of a standard **6-sided die roll**: i.e., there are always at most 6 destinations, regardless of the size of the board.
If **next** has a snake or ladder, you **must** move to the destination of that snake or ladder. Otherwise, you move to **next**.
The game ends when you reach the square $n^2$.
A board square on row r and column c has a snake or ladder if `board[r][c] != -1`. The destination of that snake or ladder is `board[r][c]`. Squares 1 and n2 do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is `[[-1,4],[-1,3]]`, and on the first move, your destination square is `2`. You follow the ladder to square `3`, but do not follow the subsequent ladder to `4`.
Return the least number of moves required to reach the square $n^2$. If it is not possible to reach the square, return `-1`.

### Example

![](https://assets.leetcode.com/uploads/2018/09/23/snakes.png)

```text
Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.
```

> [Link to the problem](https://leetcode.com/problems/snakes-and-ladders)

## Concept

Transform the problem into the shortest path and apply Dijkstra's algorithm. Note the style of the board should be processed reversely every two row.

## Solution

```python
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        hor_board = []
        for idx in range(len(board)):
            if idx % 2 == 1:
                hor_board.extend(reversed(board[len(board) - idx - 1]))
            else:
                hor_board.extend(board[len(board) - idx - 1])

        dist = [-1] * len(hor_board)
        dist[0] = 0
        queue = [(0, 0)]

        while queue:
            d, cur = heapq.heappop(queue)
            if d < dist[cur]:
                continue

            for neigh in range(cur + 1, min(cur + 7, len(hor_board))):
                dest = neigh if hor_board[neigh] == -1 else hor_board[neigh] - 1
                if dist[dest] == -1 or dist[dest] > dist[cur] + 1:
                    dist[dest] = dist[cur] + 1
                    heapq.heappush(queue, (dist[dest], dest))
        
        return dist[-1]
```

> Time complexity: $O(n^2 \log n)$ \
> Space complexity: $O(n^2)$

Note that the number of edges is smaller than $2n^2$, suppose each entry on the board has a sladder or snake. So $O(E) = O(N^2)$.
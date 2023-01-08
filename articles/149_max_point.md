# 149 - Max Points on a Line

## Problem Description

Given an array of `points` where `points[i] = [xi, yi]` represents a point on the **X-Y** plane, return the maximum number of points that lie on the same straight line.

### Example

![149 example](https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg)

```text
Input: points = [[1,1],[2,2],[3,3]]
Output: 3
```

> [Link to the problem](https://leetcode.com/problems/max-points-on-a-line/description/)

## Concept

To check how many points on a single line, we can utilize the slope. The slope measure the degree of incline of a line. The equation shown below:

$$
\text{slope} = \frac{y_1 - y_2}{x_1 - x_2}
$$

To find out the maximum number of points on a line, we can maintain a hash table for the slope.

## Solution

Although all the points are integer, the slope might be floating number. To avoid the imprecise error of the floating number, we can save the $(\text{diff}_x, \text{diff}_y)$ istead, where $\text{diff}_x$ and $\text{diff}_y$ are all integers.

However, even we save the $\text{diff}_x$ and $\text{diff}_y$, there might have some factors (*e.g.*, -1, 2) that cause different. Hence, we should unified our format (x, y) like:

1. **y** should always be positive, (Put the negative sign to **x** if necessary)
2. If **y** is 0, x should always be positive
3. Devide both (**x**, **y**) by their greatest common devisor (GCD)

```python
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Preprocess the node to the unified format
        def pre(point1, point2):
            if point2 < 0:
                point1 *= -1; point2 *= -1
            elif point2 == 0:
                point1 = abs(point1)

            factor = math.gcd(abs(point1), abs(point2))
            return point1 // factor, point2 // factor
        
        if len(points) <= 2:
            return len(points)

        max_node = -1
        for idx in range(len(points)):
            count_slope = defaultdict(int)
            for idy in range(idx + 1, len(points)):
                count_slope[pre(points[idx][0] - points[idy][0], points[idx][1] - points[idy][1])] += 1
            
            # +1 to include itself
            if count_slope:
                max_node = max(max_node, max(count_slope.values()) + 1)
        return max_node
```

> Time Complexity: $O(n^2)$ \
> Space Complexity: $O(n)$

"""
https://leetcode.com/problems/unique-paths-iii/

You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Example 1:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2

Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4

Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:
Input: grid = [[0,1],[2,0]]
Output: 0

Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 20
1 <= m * n <= 20
-1 <= grid[i][j] <= 2
There is exactly one starting cell and one ending cell.
"""

from collections import deque
from typing import Tuple, Set


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # First, we need to discover both the starting and
        # ending node, and the number of obstacles:
        start, end = (-1, -1), (-1, -1)
        obstacles = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == -1:
                    obstacles += 1

        # Next, run DFS from end to start, and keep the
        # visited nodes in a set:
        def dfs(node: Tuple[int, int], count: int, visited: Set[Tuple[int, int]]) -> Tuple[int, Set]:
            y, x = node
            count += 1

            # Out of bounds
            if y < 0 or y > m - 1:
                return 0
            if x < 0 or x > n - 1:
                return 0

            # Reached end, check if all covered
            if node == start:
                if count == n * m - obstacles:
                    return 1
                return 0

            # Skip if obstacle
            if grid[y][x] == -1:
                return 0

            # Skip if obstacle
            if (y, x) in visited:
                return 0

            # Do DFS on children, recursively
            r = 0
            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            # Set cached
            visited.add(node)
            for d in directions:
                next_node = (
                    node[0] + d[0],
                    node[1] + d[1]
                )
                r += dfs(next_node, count, visited)
            visited.remove(node)
            return r
        return dfs(end, 0, set())

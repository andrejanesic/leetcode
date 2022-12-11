"""
https://leetcode.com/problems/maximal-rectangle/description/

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = [["0"]]
Output: 0

Example 3:
Input: matrix = [["1"]]
Output: 1

Constraints:
rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
"""


class Solution:
    def maximalHistogramRectangle(self, heights: List[int]) -> int:
        stack = []
        a = 0
        for i, h in enumerate(heights):
            h = int(h)
            h = self.lastHeights[i] * h + h
            self.lastHeights[i] = h
            j = i
            while stack and h < stack[-1][1]:
                j, hMax = stack.pop()
                # In case there is a flat surface
                while stack and stack[-1][1] == hMax:
                    j, hMax = stack.pop()
                currA = (i - j) * hMax
                a = max(a, currA)
            stack.append([j, h])
        i = len(heights)
        while stack:
            j, hMax = stack.pop()
            # In case there is a flat surface
            while stack and stack[-1][1] == hMax:
                j, hMax = stack.pop()
            currA = (i - j) * hMax
            a = max(a, currA)
        return a

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        self.lastHeights = [0] * len(matrix[0])
        a = 0
        for row in matrix:
            a = max(a, self.maximalHistogramRectangle(row))
        return a

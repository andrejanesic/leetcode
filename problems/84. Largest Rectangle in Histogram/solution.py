"""
https://leetcode.com/problems/largest-rectangle-in-histogram/description/

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
1 <= heights.length <= 105
0 <= heights[i] <= 104
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        a = 0
        for i, h in enumerate(heights):
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

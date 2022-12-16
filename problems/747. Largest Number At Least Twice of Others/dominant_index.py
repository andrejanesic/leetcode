"""
https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/

You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

Example 1:
Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.

Example 2:
Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.

Constraints:

2 <= nums.length <= 50
0 <= nums[i] <= 100
The largest element in nums is unique.
"""


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        lar, secLar, larInd = 0, 0, -1
        for i, n in enumerate(nums):
            if n > lar:
                secLar = lar
                lar = n
                larInd = i
            elif n > secLar:
                secLar = n
        return larInd if lar >= 2 * secLar else -1

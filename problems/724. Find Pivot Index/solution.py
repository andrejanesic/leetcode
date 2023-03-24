"""
https://leetcode.com/problems/find-pivot-index

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.


Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3

Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
Input: nums = [1,2,3]
Output: -1

Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:
Input: nums = [2,1,-1]
Output: 0

Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0

Constraints:
1 <= nums.length <= 104
-1000 <= nums[i] <= 1000

Note: This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/
"""


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        # Calculate cumulative sum from the left
        left_csum = [0] * n
        left_csum[0] = nums[0]
        for i in range(1, n):
            left_csum[i] = nums[i] + left_csum[i - 1]

        # Calculate cumulative sum from the right
        right_csum = [0] * n
        right_csum[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_csum[i] = nums[i] + right_csum[i + 1]

        for i in range(n):
            if left_csum[i] == right_csum[i]:
                return i
        return -1

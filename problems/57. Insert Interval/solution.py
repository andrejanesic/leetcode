"""
https://leetcode.com/problems/insert-interval/description/

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        final = []
        lbFound, ubFound = False, False
        lb, ub = newInterval[0], newInterval[1]

        # counter for where we last inserted into
        # final array
        j = 0

        for s, e in intervals:

            # find position for lower bound
            if not lbFound:

                # s < e < lb
                if lb > e:
                    final.append([s, e])
                    j += 1
                    continue

                lbFound = True

                # s <= lb <= e
                if lb == e or lb >= s:
                    final.append([s, None])

                else:
                    # lb < s < e
                    final.append([lb, None])

            # find position for upper bound
            if not ubFound:

                # s < e < lb < ub
                if ub > e:
                    continue

                ubFound = True

                # s <= ub <= e
                if ub == e or ub >= s:
                    final[j][1] = e
                    continue

                else:
                    # ub < s < e
                    final[j][1] = ub

            if lbFound and ubFound:
                final.append([s, e])

        if not lbFound:
            final.append([lb, ub])
            ubFound = True
        if not ubFound:
            final[j][1] = ub
        return final

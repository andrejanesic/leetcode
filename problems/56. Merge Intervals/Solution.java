/**
 * https://leetcode.com/problems/merge-intervals/description/
 * 
 * Given an array of intervals where intervals[i] = [starti, endi], merge all
 * overlapping intervals, and return an array of the non-overlapping intervals
 * that cover all the intervals in the input.
 * 
 * Example 1:
 * Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
 * Output: [[1,6],[8,10],[15,18]]
 * Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
 * 
 * Example 2:
 * Input: intervals = [[1,4],[4,5]]
 * Output: [[1,5]]
 * Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 * 
 * Constraints:
 * 1 <= intervals.length <= 104
 * intervals[i].length == 2
 * 0 <= starti <= endi <= 104
 */

class Solution {
    public int[][] merge(int[][] intervals) {
        // Edge-case
        if (intervals.length == 0)
            return new int[][] {};

        // Turn matrix into a priority queue so that
        // we are always processing the "leftmost" edge.
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>(
                intervals.length, (a, b) -> ((int[]) a)[0] - ((int[]) b)[0]);
        for (int i = 0; i < intervals.length; i++)
            pq.offer(((int[]) intervals[i]));

        // x = smaller edge, y = greater edge
        int x = pq.peek()[0], y = pq.peek()[1];
        List<int[]> arr = new ArrayList<int[]>();
        while (pq.peek() != null) {
            int[] pair = pq.poll();
            if (pair[0] > y) {
                arr.add(new int[] { x, y });
                x = pair[0];
                y = pair[1];
                continue;
            }

            y = Math.max(y, pair[1]);
        }
        arr.add(new int[] { x, y });

        // solution object
        int[][] sol = new int[arr.size()][2];
        for (int i = 0; i < arr.size(); i++) {
            sol[i] = arr.get(i);
        }
        return sol;
    }
}
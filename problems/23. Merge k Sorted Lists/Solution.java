/*
https://leetcode.com/problems/merge-k-sorted-lists/description/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.

*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {

        /**
         * Go through all the lists (O(n)) and add elements into a
         * PriorityQueue, which is Java's implementation of the
         * binary heap. We'll use a min heap to be able to easily
         * fetch the smallest element. The complexity of adding
         * elements into this queue is O(logn), with n elements,
         * so O(nlogn). Finally, the sort is executed with O(nlogn)
         * complexity, giving us an O(nlogn) time and O(n) space
         * complexity. The queue is read again for conversion into
         * the "ListNode" class, with an additional O(n) time cost.
         */

        PriorityQueue<Integer> minHeap = new PriorityQueue();
        for (ListNode l : lists) {
            ListNode curr = l;
            while (curr != null) {
                minHeap.add(curr.val);
                curr = curr.next;
            }
        }

        if (minHeap.size() == 0) return null;

        ListNode res = new ListNode(minHeap.poll());
        ListNode curr = res;
        while (minHeap.size() > 0) {
            curr.next = new ListNode(minHeap.poll());
            curr = curr.next;
        }
        return res;
    }
}
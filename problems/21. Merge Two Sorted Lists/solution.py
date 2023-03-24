"""
https://leetcode.com/problems/merge-two-sorted-lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Edge cases
        if not list1:
            return list2
        if not list2:
            return list1

        head, tail = None, None
        next1, next2 = list1.next, list2.next
        prev = None
        while list1 or list2:
            # If either list is exhausted
            if not list1 or not list2:
                leftover = list1 if list1 else list2
                tail.next = leftover
                break

            # If both lists still available
            if list1.val <= list2.val:
                # Update list
                if not head:
                    tail = head = list1
                else:
                    tail.next = list1

                # Remove from list
                t = list1.next
                list1.next = None
                tail = list1
                list1 = t
            else:
                # Update list
                if not head:
                    tail = head = list2
                else:
                    tail.next = list2

                # Remove from list
                t = list2.next
                list2.next = None
                tail = list2
                list2 = t
        return head

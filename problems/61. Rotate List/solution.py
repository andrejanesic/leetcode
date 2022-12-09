"""
https://leetcode.com/problems/rotate-list/description/

Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0: return head

        # Keep a memo dictionary of all values so we can access them in O(1)
        memo = {}
        # Find the length of the linked list and memoize the elements
        l = 0
        curr = head
        while curr:
            l += 1
            memo[l] = curr
            curr = curr.next

        # Get the correct k
        if l < 2: return head
        k = k % l
        if k == 0: return head


        tailOld = memo[l]
        tail = memo[l - k]
        headNew = memo[l - k + 1]
        tailOld.next = head
        tail.next = None
        return headNew

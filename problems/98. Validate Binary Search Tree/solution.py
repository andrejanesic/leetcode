"""
https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

from typing import Tuple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def bst(root: Optional[TreeNode]) -> Tuple[bool, Optional[int], Optional[int], Optional[int], Optional[int]]:
            # Check the validity of both subtrees
            lMin = float("inf")
            lMax = -float("inf")
            rMin = float("inf")
            rMax = -float("inf")

            if root.left:
                if root.left.val >= root.val:
                    return (False, None, None, None, None)
                valid, lMinT, lMaxT, rMinT, rMaxT = bst(root.left)
                if not valid:
                    return (False, None, None, None, None)
                lMin = min(lMin, lMinT)
                lMax = max(lMaxT, rMaxT)
                if lMax >= root.val:
                    return (False, None, None, None, None)

            if root.right:
                if root.right.val <= root.val:
                    return (False, None, None, None, None)
                valid, lMinT, lMaxT, rMinT, rMaxT = bst(root.right)
                if not valid:
                    return (False, None, None, None, None)
                rMin = min(lMinT, rMinT)
                rMax = max(rMax, rMaxT)
                if rMin <= root.val:
                    return (False, None, None, None, None)

            if lMin == float("inf"):
                lMin = root.val
            if lMax == -float("inf"):
                lMax = root.val
            if rMin == float("inf"):
                rMin = root.val
            if rMax == -float("inf"):
                rMax = root.val
            return (True, lMin, lMax, rMin, rMax)
        return bst(root)[0]

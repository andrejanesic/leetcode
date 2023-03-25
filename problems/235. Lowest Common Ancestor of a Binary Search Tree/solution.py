"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Inorder traversal, but we check the parent for p and q first.
        """
        stack = [[root, False, 0]]
        while stack:
            root, isTraversed, foundCount = stack.pop()

            # Check if this is either p or q (if the value is a
            # descendant of itself)
            if (p and root.val == p.val):
                p = None
                foundCount += 1
            elif (q and root.val == q.val):
                q = None
                foundCount += 1

            # If not traversed yet and either value is missing,
            # traverse L R first (preorder), then process this node
            if not isTraversed and (p or q):
                stack.append([root, True, foundCount])
                if root.right:
                    stack.append([root.right, False, 0])
                if root.left:
                    stack.append([root.left, False, 0])
                continue

            # If ancestor of both p and q, set this as LCA
            if foundCount == 2:
                return root

            # Otherwise this is not the LCA, so increment the
            # ancestor by your found count and continue
            parentIndex = -1 if stack[-1][1] else -2
            stack[parentIndex][2] += foundCount

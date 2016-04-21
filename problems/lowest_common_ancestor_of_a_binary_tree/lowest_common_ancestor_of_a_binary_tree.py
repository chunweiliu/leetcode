# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # If root is either p or q, it is the part of answer.
        if root in (None, p, q):
            return root

        left, right = (self.lowestCommonAncestor(child, p, q)
                       for child in (root.left, root.right))

        # The LCA is the root has p and q in different side.
        # If p and q are in the same side, the LCA is in that side.
        return root if left and right else left or right

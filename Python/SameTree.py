# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        """Traverse two trees together
        Time: O(n)
        Space: O(n)
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        ret = True
        ret &= self.isSameTree(p.left, q.left)
        ret &= self.isSameTree(p.right, q.right)
        return ret

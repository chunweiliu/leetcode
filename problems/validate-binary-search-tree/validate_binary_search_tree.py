# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution(object):
    def isValidBST(self, root, min_node=None, max_node=None):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Know the minimum and maximum for the right and the left sub
        if not root:
            return True
        if ((min_node and min_node.val >= root.val) or
                (max_node and max_node.val <= root.val)):
            return False
        return (self.isValidBST(root.left, min_node, root) and
                self.isValidBST(root.right, root, max_node))

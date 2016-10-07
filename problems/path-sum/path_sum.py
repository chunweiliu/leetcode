# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def hasPathSum(self, root, target, path_sum=0):
        """
        :type root: TreeNode
        :type target: int
        :rtype: bool
        """
        if not root:
            return False

        if not root.left and not root.right:
            return root.val + path_sum == target

        return (self.hasPathSum(root.left, target, path_sum + root.val) or
                self.hasPathSum(root.right, target, path_sum + root.val))

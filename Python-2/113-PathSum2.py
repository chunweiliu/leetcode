# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """
        return self.path_sum(root, target, 0, [], [])

    def path_sum(self, root, target, path_sum=0, path=[], paths=[]):
        if not root:
            return []

        if not root.left and not root.right:
            if root.val + path_sum == target:
                paths.append(path + [root.val])
                return paths

        self.path_sum(root.left, target, path_sum + root.val,
                      path + [root.val], paths)
        self.path_sum(root.right, target, path_sum + root.val,
                      path + [root.val], paths)
        return paths

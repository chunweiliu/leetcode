# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # The maximum depth is the number of nodes along the longest path from
        # the root node down to the farthest leaf node.
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == '__main__':
    root = TreeNode(0, TreeNode(1))
    print Solution().maxDepth(root)

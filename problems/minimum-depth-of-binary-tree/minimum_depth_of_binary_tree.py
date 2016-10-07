# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        min_depth = 0
        level = [root]
        while level:
            min_depth += 1
            next_level = []
            for node in level:
                if not node.left and not node.right:
                    return min_depth
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level
        return min_depth

if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2))
    print Solution().minDepth(root)

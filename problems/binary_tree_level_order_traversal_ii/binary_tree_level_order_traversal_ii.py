# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level, levels = [root], []
        if root:
            while level:
                levels.append([node.val for node in level])
                level = [child
                         for node in level
                         for child in (node.left, node.right) if child]
        return list(reversed(levels))

if __name__ == '__main__':
    root = TreeNode(0, TreeNode(11, TreeNode(111)), TreeNode(12))
    print Solution().levelOrderBottom(root)

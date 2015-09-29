# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return (self.isBalanced(root.left) and
                self.isBalanced(root.right) and
                abs(self.tree_height(root.left) -
                    self.tree_height(root.right)) < 2)

    def tree_height(self, root):
        # The maximum path from any leaf (height 0) to the root.
        if not root:
            return 0
        return 1 + max(self.tree_height(root.left),
                       self.tree_height(root.right))

if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5))), TreeNode(3))
    print Solution().isBalanced(root)

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        """Set median as root, recursive for left and right
        Time: O(log n)
        Space: O(n)
        """
        if not num:
            return None
        if len(num) == 1:
            return TreeNode(num[0])

        middle = len(num) / 2
        root = TreeNode(num[middle])
        root.left = self.sortedArrayToBST(num[:middle])
        root.right = self.sortedArrayToBST(num[middle+1:])
        return root

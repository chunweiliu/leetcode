# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        # check root in [lower, upper], time: O(n), space: O(h)
        if root is None:
            return True
        else:
            return self.is_valid_bst(root, -10000, 10000)

    def is_valid_bst(self, root, lower, upper):
        if root is None:
            return True
        elif root.val <= lower or root.val >= upper:
            return False

        return self.is_valid_bst(root.left, lower, root.val) \
            and self.is_valid_bst(root.right, root.val, upper)

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(1))
    print Solution().isValidBST(root)

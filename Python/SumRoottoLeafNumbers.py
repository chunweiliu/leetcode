# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if root is None:
            return 0
        else:
            return self.sumNumbersRecursive(root, root.val)

    def sumNumbersRecursive(self, root, num_from_root):
        if root.left is None and root.right is None:
            return num_from_root

        # sum up different branches
        num = 0
        if root.left:
            num += self.sumNumbersRecursive(
                root.left, root.left.val + 10 * num_from_root)
        if root.right:
            num += self.sumNumbersRecursive(
                root.right, root.right.val + 10 * num_from_root)
        return num


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    print Solution().sumNumbers(root)

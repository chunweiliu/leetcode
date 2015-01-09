# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        while root:
            if root.left:
                curr = root.left
                while curr.right:
                    curr = curr.right  # the last pre-order node
                curr.right = root.right  # point to the right root
                root.right = root.left
                root.left = None
            root = root.right


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                    TreeNode(5, None, TreeNode(6)))
    #root = TreeNode(1, TreeNode(2))
    Solution().flatten(root)

    def traverseTree(root):
        if root:
            print root.val
            traverseTree(root.left)
            traverseTree(root.right)
    traverseTree(root)

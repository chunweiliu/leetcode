# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        """Traverse from root to leaves, if any return True
        Time: O(n)
        Space: O(n)
        """
        def preorder(root, sum):
            if not root.left and not root.right:  # leaves
                return True if sum == 0 else False

            found = False
            if root.left:
                found |= preorder(root.left, sum - root.left.val)
            if root.right:
                found |= preorder(root.right, sum - root.right.val)
            return found

        if not root:
            return False
        return preorder(root, sum - root.val)

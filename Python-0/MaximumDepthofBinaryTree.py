# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        """Traverse the tree and record the max depth
        Time: O(n)
        Space: O(n)
        """
        self.max_depth = 0  # ask about this

        def max_depth(root, depth):
            if not root.left and not root.right:  # leaves
                self.max_depth = depth if depth > self.max_depth \
                    else self.max_depth
            if root.left:
                max_depth(root.left, depth + 1)
            if root.right:
                max_depth(root.right, depth + 1)

        if root:
            max_depth(root, 1)
        return self.max_depth

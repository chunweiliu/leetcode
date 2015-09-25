# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # A path means a one way connection: such as left -> root -> right.
        # In the above case, the value cannot be passed to the root's parent.
        def max_path_to_root(root):
            if not root:
                return 0
            l = max(0, max_path_to_root(root.left))
            r = max(0, max_path_to_root(root.right))

            #      root
            #    /      \
            # left      right
            self.max = max(self.max, l + root.val + r)  # Global maximum.

            # parent
            #       \
            #      root
            #    /
            # left
            return max(l, r) + root.val

        # Use a global variabl to record the maximum path sum in the tree.
        self.max = None
        max_path_to_root(root)
        return self.max

    def maxPathSum_wa(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Each node record the maximum path sum below it.
        # Find the maximum in the 6 conditions:
        # [x + l + r, x + l, x + r, x, l, r]
        if not root.left and not root.right:
            return root.val

        x = root.val
        l = r = None  # Have to been None to include all negative cases.
        if root.left:
            l = self.maxPathSum(root.left)
        if root.right:
            r = self.maxPathSum(root.right)
        x += l if l > 0 else 0
        x += r if r > 0 else 0
        return max([x, l, r])

if __name__ == '__main__':
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    print Solution().maxPathSum(root)

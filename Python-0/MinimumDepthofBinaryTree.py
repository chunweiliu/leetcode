# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # @param root, a tree node
    # @return an integer
    min_depth = 1000

    def minDepth2(self, root):
        # Recursive
        # Time: O(n)
        # Space: O(h)
        if root is None:
            return
        else:
            return self.depthCount(root, 0)

    def depthCount(self, root, depth):
        if root is None:
            return depth - 1
        else:
            count_l = self.depthCount(root.left, depth + 1)
            count_r = self.depthCount(root.right, depth + 1)
            print root.val, count_l, count_r
            return min(count_l, count_r)

    def minDepth(self, root):
        """Traverse a tree and record the min depth in instance variable
        Time: O(n)
        Space: O(n)
        """
        self.min_depth = float('inf')

        def min_depth(root, depth):
            if not root.left and not root.right:
                self.min_depth = depth if depth < self.min_depth \
                    else self.min_depth
            if root.left:
                min_depth(root.left, depth + 1)
            if root.right:
                min_depth(root.right, depth + 1)

        if not root:
            return 0

        min_depth(root, 1)
        return self.min_depth


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4, TreeNode(5))))
    print Solution().minDepth(root)

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        """Find all paths from root to leaves had path sum equal to sum
        Time: O(n)
        Space: O(n)
        """
        def path_finder(root, sum, path, paths):
            if not root.left and not root.right:  # leaves
                if sum == 0:
                    paths.append(path)

            if root.left:  # copy of path, so they won't affect each
                path_finder(root.left, sum-root.left.val,
                            list(path+[root.left.val]), paths)
            if root.right:
                path_finder(root.right, sum-root.right.val,
                            list(path+[root.right.val]), paths)
        if not root:
            return list()

        paths = list()
        path_finder(root, sum-root.val, [root.val], paths)
        return paths

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(0), TreeNode(0)), TreeNode(-1, TreeNode(3)))
    print Solution().pathSum(root, 3)

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        """Record max path so far in a container
        Time: O(n)
        Space: O(n)
        Style: Using MEMBER
        """
        self.max_value = float('-inf')
        self.maxPathSumRec(root)
        return self.max_value

    def maxPathSumRec(self, root):
        if not root:
            return 0

        left_sum = self.maxPathSumRec(root.left)
        right_sum = self.maxPathSumRec(root.right)

        if left_sum < 0 and right_sum < 0:
            self.max_value = max(self.max_value, root.val)
            level_max = root.val
        else:
            if left_sum > 0 and right_sum > 0:
                self.max_value = max(self.max_value,
                                     left_sum + root.val + right_sum)

            level_max = max(left_sum, right_sum) + root.val
            self.max_value = max(self.max_value, level_max)
        return level_max

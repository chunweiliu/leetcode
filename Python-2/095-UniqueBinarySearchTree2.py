# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.build_bst(1, n)

    def build_bst(self, s, e):
        # Assume the input are valid (1 <= s <= e <= n).
        if s > e:
            return [None]

        ans = []
        for i in range(s, e + 1):
            left_roots = self.build_bst(s, i - 1)
            right_roots = self.build_bst(i + 1, e)
            for left in left_roots:
                for right in right_roots:
                    # Need to call the root constructor each time.
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    ans.append(root)
        return ans

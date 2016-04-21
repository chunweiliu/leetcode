# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.stack = []
        self.visit_the_left_most(root)
        while k:
            curr = self.stack.pop()
            if curr and curr.right:
                self.visit_the_left_most(curr.right)
            k -= 1
        return curr.val

    def visit_the_left_most(self, root):
        while root:
            self.stack.append(root)
            root = root.left

if __name__ == '__main__':
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),
                    TreeNode(6, None, TreeNode(8)))
    k = 6
    print Solution().kthSmallest(root, k)

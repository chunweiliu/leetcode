# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path_p = self.search(root, p)
        path_q = self.search(root, q)

        i, j = 0, 0
        lowest_common_ancestor = root
        while i < len(path_p) and j < len(path_q):
            if path_p[i] is path_q[j]:
                lowest_common_ancestor = path_p[i]
                i += 1
                j += 1
            else:
                break
        return lowest_common_ancestor

    def search(self, root, p):
        if p.val == root.val:
            return [root]
        if p.val < root.val:
            return [root] + self.search(root.left, p)
        return [root] + self.search(root.right, p)

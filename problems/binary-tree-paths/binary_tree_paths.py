# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # Use two stacks. One stack to travese, one for recording paths.
        #     1
        #   2   5
        # 3   4
        if not root:
            return []

        paths = []
        stack = [(root, '')]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path + str(node.val))
            if node.right:
                stack.append((node.right, path + str(node.val) + '->'))
            if node.left:
                stack.append((node.left, path + str(node.val) + '->'))

        # This affects the time complexity.
        # return ['->'.join(map(str, path)) for path in paths]
        return paths


if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5))
    print Solution().binaryTreePaths(root)

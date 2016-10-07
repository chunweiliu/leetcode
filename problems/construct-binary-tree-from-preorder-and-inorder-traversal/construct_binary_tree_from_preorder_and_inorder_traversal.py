class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root = TreeNode(preorder.pop(0))
            root.left = self.buildTree(preorder, inorder[:inorder.index(root.val)])
            root.right = self.buildTree(preorder, inorder[inorder.index(root.val) + 1:])
            return root


preorder = 'F, B, A, D, C, E, G, I, H'.split(', ')
inorder = 'A, B, C, D, E, F, G, H, I'.split(', ')
root = Solution().buildTree(preorder, inorder)

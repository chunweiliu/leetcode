# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root = TreeNode(postorder.pop())

            # The order of building right tree than left tree is important.
            # Because the postorder hold right subtree from the right, 
            # so we won't find any match for next popped root, which would be the root of right subtree,
            # in the left substree.
            root.right = self.buildTree(inorder[inorder.index(root.val) + 1:], postorder)
            root.left = self.buildTree(inorder[:inorder.index(root.val)], postorder)
            return root
        

inorder = [2, 1, 3]
postorder = [2, 3, 1]
root = Solution().buildTree(inorder, postorder)
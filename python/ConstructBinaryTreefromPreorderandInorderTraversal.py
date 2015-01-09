# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        """Recursively build tree
        Time: O(n log n) in avergae
        Space: O(log n) in average
        """
        if not preorder:
            return None

        root_val = preorder[0]
        left_count = inorder.index(root_val)

        left_preorder = preorder[1:1+left_count]
        left_inorder = inorder[:left_count]

        right_preorder = preorder[1+left_count:]
        right_inorder = inorder[1+left_count:]

        root = TreeNode(root_val)
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root

#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        """Recuresively build
        Time: O(n log n) in average
        Space: O(log n) in average
        """
        if not postorder:
            return None

        root_val = postorder[-1]
        left_count = inorder.index(root_val)

        left_inorder = inorder[:left_count]
        left_postorder = postorder[:left_count]

        right_inorder = inorder[1+left_count:]
        right_postorder = postorder[left_count:len(postorder)-1]  # end index!

        root = TreeNode(root_val)
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root

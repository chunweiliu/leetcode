# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        """Binary tree level order traversal using stack
        Time: O(n)
        Space: O(n)
        """
        if not root:
            return []  # This should be awared!

        level_order = list()

        this_level = list()
        this_level.append(root)
        while this_level:
            level_order.append([x.val for x in this_level])

            next_level = list()
            for node in this_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            this_level = next_level

        return level_order

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Level order triversal, see if each level is symmetric. (None?)

        # Recursively see if two inversed nodes are equal.
        def is_reversed(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            # If has
            #  /  \
            # /\  /\
            return (is_reversed(left.left, right.right) and
                    is_reversed(left.right, right.left))

        if not root:
            return True
        return is_reversed(root.left, root.right)

if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2), TreeNode(2))
    print Solution().isSymmetric(root)

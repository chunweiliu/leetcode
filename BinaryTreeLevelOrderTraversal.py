# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        # trivial case
        if root is None:
            return list()  # None: WA, root: WA

        ret = list()
        this_level = [root]
        while this_level:
            next_level = list()
            this_level_val = list()
            for x in this_level:
                if x is not None:
                    this_level_val.append(x.val)
                if x.left is not None:
                    next_level.append(x.left)
                if x.right is not None:
                    next_level.append(x.right)
            ret.append(this_level_val)
            this_level = next_level

        return ret


if __name__ == "__main__":
    tree = None
    #tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print Solution().levelOrder(tree)

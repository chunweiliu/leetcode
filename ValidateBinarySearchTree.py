# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        """Perform Morris traversal and check if all current > previous node
        Time: O(n)
        Space: O(1)
        """
        MIN_VALUE = -1000000
        if root is None:
            return True

        ret = True
        curr = root
        last_value = MIN_VALUE
        while curr:
            if curr.left:
                pred = curr.left
                # find the end node of the left subtree
                while pred.right and pred.right is not curr:
                    pred = pred.right

                if pred.right:  # pred.right is curr
                    pred.right = None  # revert the next link
                    if last_value >= curr.val:
                        ret = False
                    last_value = curr.val
                    curr = curr.right
                else:
                    pred.right = curr
                    curr = curr.left
            else:
                if last_value >= curr.val:
                    ret = False
                last_value = curr.val
                curr = curr.right
        return ret


if __name__ == "__main__":
    root = TreeNode(1, None, TreeNode(1))
    print Solution().isValidBST(root)

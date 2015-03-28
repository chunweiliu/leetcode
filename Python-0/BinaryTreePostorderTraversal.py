# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        # The print order is reverse, so two stacks are need
        # This is DIFFERENT than in-and-pre order
        # Time: O(n)
        # Space: O(2h)
        in_stack = list()
        out_stack = list()
        curr = root

        in_stack.append(root)
        while len(in_stack) != 0:
            curr = in_stack.pop()
            if curr:
                out_stack.append(curr)
                if curr.left:
                    in_stack.append(curr.left)
                if curr.right:
                    in_stack.append(curr.right)

        ans = list()
        while len(out_stack) != 0:
            ans.append(out_stack.pop().val)
        return ans

if __name__ == "__main__":
    root = TreeNode(4, TreeNode(3, TreeNode(1), TreeNode(2)))
    print Solution().postorderTraversal(root)

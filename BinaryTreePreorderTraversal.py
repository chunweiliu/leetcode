# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        # Using stack as inorder, just need to change where to pop value
        # Time: O(n)
        # Space: O(h), h = O(log n)

        ans = list()
        stack = list()

        curr = root
        done = False
        while not done:
            if curr:
                ans.append(curr.val)
                stack.append(curr)
                curr = curr.left
            else:
                if len(stack) == 0:
                    done = True
                else:
                    temp = stack.pop()
                    curr = temp.right
        return ans


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5))
    print Solution().preorderTraversal(root)

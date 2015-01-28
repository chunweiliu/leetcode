# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        # Traverse a binary tree iterativly
        # Time: O(n)
        # Space: O(h), h = O(log n) if using stack; O(1) if using Morris
        stack = list()
        ans = list()

        # if left is None: pop and print
        curr = root
        done = False
        while not done:
            if curr is not None:  # curr might be None, and we don't push then
                stack.append(curr)
                curr = curr.left
            else:
                if len(stack) == 0:  # because stack was initially []
                    done = True
                else:
                    temp = stack.pop()
                    ans.append(temp.val)
                    curr = temp.right
        return ans

if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)))
    print Solution().inorderTraversal(root)

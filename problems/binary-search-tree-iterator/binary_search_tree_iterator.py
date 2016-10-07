# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # hasNext Time: O(1), Space: O(h)
        # next Time: O(1), Space: O(h)
        #     4
        #   2   5
        #     3    6
        self.stack = []
        self.visit_the_left_most(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        # If the stack is empty, it would be evaluted as False, otherwise, True
        return self.stack

    def next(self):
        """
        :rtype: int
        """
        current_node = self.stack.pop()

        if current_node.right:
            self.visit_the_left_most(current_node.right)

        return current_node.val

    def visit_the_left_most(self, root):
        while root:
            self.stack.append(root)
            root = root.left

if __name__ == '__main__':
    # Your BSTIterator will be called like this:
    root = TreeNode(4, TreeNode(2, None, TreeNode(3)), TreeNode(5, None, TreeNode(6)))
    i, v = BSTIterator(root), []
    while i.hasNext():
        v.append(i.next())
    print v

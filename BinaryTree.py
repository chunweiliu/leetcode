# Definition for a binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
    	# Preorder
        self.val = x
        self.left = left
        self.right = right

class Tree:
	def __init__(self):
		self.root = None

	def addNode(self, data):
		return TreeNode(data)

	def insert(self, root, data):
		if root is None:
			return self.addNode(data)
		else:
			if data <= root.val:
				root.left = self.insert(root.left, data)
			else:
				root.right = self.insert(root.right, data)
			return root

	def printTree(self, root):
		if root is None:
			pass
		else:
			self.printTree(root.left)
			print root.val
			self.printTree(root.right)


    # @param root, a tree node
    # @return an integer
    # def maxDepth(self, root):
    #     maxd = 1
    #     if self.left is None and self.right is None:
    #     	return maxd
    #     else:
    #     	maxDepth(self.left, self)
    #     	maxDepth(self.right, self)
        
if __name__ == "__main__":
    btree = Tree()
    root = TreeNode(0)
    for i in range(5):
    	data = int(i)+1
    	btree.insert(root, data)

    btree.printTree(root)
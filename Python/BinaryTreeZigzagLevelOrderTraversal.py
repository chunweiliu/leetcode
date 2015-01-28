# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from BinaryTree import Tree
from BinaryTree import TreeNode

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
    	# test tricky basic case
    	if root is None:
    		return list()
    		
    	# for loop for BFS instead of recursives
    	values = list()
    	thislevel = [root]
    	# traverse a tree
    	while thislevel:
    		thislevelval = list()
    		nextlevel = list()
    		for x in thislevel:
    			if x is None:
    				continue  			
    			thislevelval.append(x.val)
    			if x.left: nextlevel.append(x.left)
    			if x.right: nextlevel.append(x.right)
    		if thislevelval is not None:
    			values.append(thislevelval)
     		thislevel = nextlevel
     		
     	# traverse a list of lists
        zigzagvalues = list()
        n = 1
    	for x in values:
    		if n == -1:
    			x.reverse()
    			zigzagvalues.append(x)
    		else:
    			zigzagvalues.append(x)
    		n *= -1
    	return zigzagvalues

 
if __name__ == "__main__":
	#tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
	tree = TreeNode(None)
	print Solution().zigzagLevelOrder(None)
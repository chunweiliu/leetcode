# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.to_bst(nums, -1, len(nums))

    def to_bst(self, nums, start, end):
        if end - start == 1:
            return None

        mid = (end - start) / 2 + start
        root = TreeNode(nums[mid])
        root.left = self.to_bst(nums, start, mid)
        root.right = self.to_bst(nums, mid, end)
        return root

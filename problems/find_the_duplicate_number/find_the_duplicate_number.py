class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(nlogn): Apply pinghole theory to the half of a range.
        # [1, 2, 3, 4, 4, 5, 6]
        # [1, 6] check 3 -> [1, 3] or [4, 6]
        # [4, 6] check 5 -> [4, 5] or [6, 6]
        # [4, 5] check 4 -> [4, 4] or [5, 5]
        left, right = 1, len(nums) - 1
        while left != right:
            middle = left + (right - left) // 2
            # Only need to check how many numbers are under the middle.
            count = sum([1 for num in nums if num <= middle])
            if count > middle:
                right = left
            else:
                left = middle + 1
        return left

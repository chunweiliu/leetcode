class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Apply the framework of binary search.
        # 1. What's the range for searching?
        # 2. What's the loop invariant?

        # Search [0, n - 1] -> left, right = -1, n
        left, right = -1, len(nums)
        while right - left > 1:
            mid = (right - left) / 2 + left
            if nums[mid] < target:  # nums[left] < target <= nums[right]
                left = mid
            else:
                right = mid
        return right

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

        # Search [0, n - 1] -> start, end = -1, n
        start, end = -1, len(nums)
        while end - start > 1:
            mid = (end - start) / 2 + start
            if nums[mid] < target:
                start = mid  # nums[start] < target <= nums[end]
            else:
                end = mid
        return end

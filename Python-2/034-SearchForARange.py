class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.search_left(nums, target),
                self.search_right(nums, target)]

    def search_left(self, nums, target):
        start, end = -1, len(nums)
        while end - start > 1:
            mid = (end - start) / 2 + start
            if nums[mid] < target:  # nums[start] < target <= nums[end]
                start = mid
            else:
                end = mid
        return end if end != len(nums) and nums[end] == target else -1

    def search_right(self, nums, target):
        start, end = -1, len(nums)
        while end - start > 1:
            mid = (end - start) / 2 + start
            if nums[mid] <= target:  # nums[start] <= target < nums[end]
                start = mid
            else:
                end = mid
        return start if start != -1 and nums[start] == target else -1

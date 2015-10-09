class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.left_search(nums, target),
                self.right_search(nums, target)]

    def left_search(self, nums, target):
        left_interval = -1  # [BUG] left_interval = 0
        i, j = 0, len(nums) - 1
        while i <= j:
            m = i + (j - i) / 2
            if target <= nums[m]:
                j = m - 1
                if target == nums[m]:  # [BUG] N/A
                    left_interval = m
            else:
                i = m + 1
        return left_interval

    def right_search(self, nums, target):
        right_interval = -1
        i, j = 0, len(nums) - 1
        while i <= j:
            m = i + (j - i) / 2
            if target >= nums[m]:
                i = m + 1
                if target == nums[m]:
                    right_interval = m
            else:
                j = m - 1
        return right_interval

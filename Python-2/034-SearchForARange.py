class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Search for the left interval.
        left_interval = -1
        i, j = 0, len(nums) - 1
        while i <= j:
            m = i + (j - i) / 2
            if nums[m] >= target:
                if nums[m] == target:
                    left_interval = m
                j = m - 1
            else:
                i = m + 1

        # Search for the right interval.
        right_interval = -1
        i, j = 0, len(nums) - 1
        while i <= j:
            m = i + (j - i) / 2
            if nums[m] <= target:
                if nums[m] == target:
                    right_interval = m
                i = m + 1
            else:
                j = m - 1
        return [left_interval, right_interval]

if __name__ == '__main__':
    nums = [1]
    target = 0
    print Solution().searchRange(nums, target)

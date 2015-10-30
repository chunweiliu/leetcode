class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = -1, len(nums)
        min_num = nums[0]
        while end - start > 1:
            mid = (end - start) / 2 + start
            min_num = min(min_num, nums[mid])
            if nums[mid] > nums[end - 1]:
                start = mid
            elif nums[mid] < nums[end - 1]:
                end = mid
            else:
                end -= 1
        return min_num

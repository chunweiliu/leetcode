class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        remainder = len(nums) * (len(nums) + 1) / 2
        for num in nums:
            remainder -= num
        return remainder

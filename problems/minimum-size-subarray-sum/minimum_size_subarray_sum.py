class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        start, current_sum = 0, 0
        min_length = len(nums) + 1
        for i, num in enumerate(nums):
            current_sum += num
            while current_sum >= target:
                min_length = min(min_length, i - start + 1)
                current_sum -= nums[start]
                start += 1
        return min_length if min_length != len(nums) + 1 else 0

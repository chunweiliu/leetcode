class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sum up numbers accumlatively. If the current sum is negative, reset.
        if not nums:
            return nums
        maximum_sum = nums[0]
        current_sum = 0
        for num in nums:
            current_sum += num
            maximum_sum = max(current_sum, maximum_sum)
            current_sum = max(0, current_sum)  # Get rid off the negative sum.
        return maximum_sum

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print Solution().maxSubArray(nums)

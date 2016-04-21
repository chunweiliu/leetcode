class Solution:
    # @param nums, a list of integer
    # @return an integer
    def rob(self, nums):
        # Find the maximum value with some constraints
        # t[n] = t[n - 2] + v[n]
        #      = t[n - 1]
        n = len(nums)
        if n < 2:
            return nums[-1] if nums else 0

        t = [0] * n
        t[0] = nums[0]
        t[1] = max(nums[0], nums[1])  # [BUG] The first neighbor can be skiped
        for i in range(2, n):
            t[i] = max(t[i - 2] + nums[i], t[i - 1])
        return t[-1]

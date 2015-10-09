class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(self.rob_street(nums[1:]), self.rob_street(nums[:-1]))

    def rob_street(self, nums):
        n = len(nums)
        if n < 2:
            return nums[-1] if nums else 0

        t = [0] * n
        t[0] = nums[0]
        t[1] = max(nums[0], nums[1])

        for i in range(2, n):
            t[i] = max(t[i - 2] + nums[i], t[i - 1])

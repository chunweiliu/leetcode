class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # For k larger than or equal to the length of numbers
        k %= len(nums)

        # Slice operator generally failed for zero index.
        if k == 0:
            return 

        # Use slice operator [:] to indicate the original object.
        nums[:] = nums[-k:] + nums[:len(nums) - k]


if __name__ == "__main__":
    nums = [1]
    k = 1
    Solution().rotate(nums, k)
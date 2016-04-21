class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # The last statement to be excuted, the faster the time would be.

        # Find the first none increasing number from left
        i = len(nums) - 1
        while i >= 1 and nums[i - 1] >= nums[i]:
            i -= 1
        i -= 1  # i either is the answer or -1

        # Decreasing all the way down. No swap need.
        if i == -1:
            nums.reverse()
            return

        # Find the first number larger than the pivot from left
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1

        # Swap i, j
        nums[i], nums[j] = nums[j], nums[i]

        # Revserse the number after i
        nums[i+1:] = reversed(nums[i+1:])

if __name__ == '__main__':
    nums = [1]
    print nums
    Solution().nextPermutation(nums)
    print nums

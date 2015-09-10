class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Find the pivot (largest number in accending order in backward).
        # 6 8 7 4 3 2
        # p
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            # Decending all the way, like 3, 2, 1, 1
            nums.reverse()
            return
        pivot = i - 1

        # Find the smallest larger number to swap with the pivot.
        # 6 8 7 4 3 2
        # p   i
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[pivot]:
            i -= 1
        nums[pivot], nums[i] = nums[i], nums[pivot]

        # Reorder the numbers after the pivot for a mimimum increasing.
        # 7 2 3 4 6 8
        nums[pivot + 1:] = reversed(nums[pivot + 1:])

if __name__ == '__main__':
    nums = [1, 3, 2]
    print nums
    Solution().nextPermutation(nums)
    print nums

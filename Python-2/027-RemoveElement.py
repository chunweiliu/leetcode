class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # The element privous than i is well maintained.
        i = j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i

        # Due to the order is not matter, two pointers is a easier solution.
        # i, j = 0, len(nums) - 1
        # while i <= j:
        #     if nums[i] == val:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         j -= 1
        #     else:
        #         i += 1
        # return j + 1

        # AC one liner. But create another list.
        # nums[:] = [nums[i] for i in range(len(nums)) if nums[i] != val]
        # return len(nums)

if __name__ == '__main__':
    nums = [1, 1, 2, 3]
    val = 1
    print Solution().removeElement(nums, val)
    print nums

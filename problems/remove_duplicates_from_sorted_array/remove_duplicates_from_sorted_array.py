class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Update tail if the current number is not a duplicate.
        tail = 0
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                tail += 1
            nums[tail] = nums[i]
        return tail + 1

        # num_duplicate = 0
        # none_duplicate = 0
        # total_num = len(nums)
        # for i in range(total_num - 1):
        #     if nums[i] == nums[i + 1]:
        #         num_duplicate += 1
        #     else:
        #         none_duplicate += 1
        #     nums[none_duplicate] = nums[none_duplicate + num_duplicate]
        # return total_num - num_duplicate

        # AC one liner. But create a new list first then replace the old one.
        # nums[:] = [nums[x] for x in range(len(nums))
        #            if nums[x] != nums[x - 1] or x == 0]
        # return len(nums)

if __name__ == '__main__':
    nums = [0, 0, 0, 1, 2, 2, 3, 4]
    print Solution().removeDuplicates(nums)
    print nums

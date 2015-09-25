class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Duplicates are allowed at most twice.
        # Assume the array elements preivous than i are fully took care of:
        # 1 1 2 2 2 2 2 2 ... 2 2 2 2 3
        #         i  wait until n hit ^
        ALLOWED_DUPLICATE = 2

        i = 0
        for n in nums:
            if i < ALLOWED_DUPLICATE or n > nums[i - ALLOWED_DUPLICATE]:
                nums[i] = n
                i += 1
        return i

if __name__ == '__main__':
    nums = [1, 1, 1, 1, 2, 2, 2, 3]
    print Solution().removeDuplicates(nums)

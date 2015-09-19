class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Duplicates are allowed at most twice.
        # Loop through the numbers and include those in the result haven't been
        # include twice already.
        # 1) Why check nums[i - ALLOWED_DUPLICATE]?
        # 2) Why nums[i] is always less than n, otherwise it is a duplicate?
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

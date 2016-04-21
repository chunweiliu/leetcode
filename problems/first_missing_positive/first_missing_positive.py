# from collections import defaultdict
# import pdb


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Given a list of unsorted integer [-1, 1, 3, 0, 4], return 2.
        # Require Time: O(n), Space: O(1) -> Use the original vector as space.
        # Algo: Swap the number to their original space if we can. Return the
        # first invalid location.
        for i, num in enumerate(nums):
            # Continously check the current possition to make sure the element
            # which has been swapped to this place can be taken care of.
            while 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                # Need this temperal veriable x for swap.
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i] won't
                # work. What the above commend did for i == 1 is that:
                # Load nums[3], nums[1], swap them, put it to nums[1], nums[0].
                # Because nums[i] is changing during the swap.
                x = nums[i] - 1
                nums[i], nums[x] = nums[x], nums[i]

        for i, num in enumerate(nums):
            if i + 1 != num:
                return i + 1
        return len(nums) + 1

        # Put the positive numbers into buckets. Scan the bucket from 1 to N.
        # No consider a constant space solution.
        # existed_numbers = defaultdict(int)
        # for i, num in enumerate(nums):
        #     if num > 0:
        #         existed_numbers[num] = 1
        # for num in range(1, 10 ** 5):
        #     if num not in existed_numbers:
        #         return num

if __name__ == '__main__':
    nums = [3, 4, -1, 1]
    print Solution().firstMissingPositive(nums)

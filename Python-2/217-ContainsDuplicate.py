from collections import Counter


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # O(n) time, O(n) space.
        if not nums:
            return False

        return any([value > 1 for value in Counter(nums).values()])

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # An array has all pair numbers expect of one. Find the one.
        # Time: O(n), Space: O(1)
        return reduce(lambda x, y: x ^ y, nums)

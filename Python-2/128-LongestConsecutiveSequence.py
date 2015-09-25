class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Given [100, 4, 200, 1, 2, 3] -> return the lenght 4 for [1, 2, 3, 4].
        # The key idea is the look-up time in set is O(1) in average.
        # Also, the set itself can handle negative and very large numbers.
        nums = set(nums)

        max_length = 1
        for num in nums:
            # Check only the start of the consecutive numbers. This gives us a
            # O(n) algorithm.
            if num - 1 not in nums:
                current_consecutive_num = num
                while current_consecutive_num + 1 in nums:
                    current_consecutive_num += 1
                max_length = max(current_consecutive_num - num + 1, max_length)
        return max_length

if __name__ == '__main__':
    nums = [9, 1, -3, 2, 4, 8, 3, -1, 6, -2, -4, 7]
    print Solution().longestConsecutive(nums)

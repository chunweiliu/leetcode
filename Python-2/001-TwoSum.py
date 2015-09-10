from collections import defaultdict


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = defaultdict(lambda: -1)
        for i, x in enumerate(nums):
            # Assume there is no conflict numbers
            hash_map[x] = i

        for i, x in enumerate(nums):
            j = hash_map[target - x]
            if j != -1 and j != i:
                return [i + 1, j + 1]
        return list()

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 10
    print Solution().twoSum(nums, target)

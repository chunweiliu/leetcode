class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = [[]]
        for n in sorted(nums):
            subsets += [s + [n] for s in subsets if s + [n] not in subsets]
        return subsets


if __name__ == '__main__':
    nums = [1, 2, 2]
    print Solution().subsetsWithDup(nums)

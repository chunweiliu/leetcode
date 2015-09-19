class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = [[]]
        for n in sorted(nums):
            # [] is a element. It's like 0 in addition or 1 in multiplication.
            subsets += [s + [n] for s in subsets]
        return subsets

if __name__ == '__main__':
    nums = [1, 2, 3]
    print Solution().subsets(nums)

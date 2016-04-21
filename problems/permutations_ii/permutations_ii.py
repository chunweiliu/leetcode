class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Follow the idea of permutation, but skip the duplicate one.
        nums.sort()

        def permute(nums):
            # This make two times faster than `if not nums: return [[]]`
            if len(nums) < 2:
                return [nums]

            ans = []
            previous = None
            for i, n in enumerate(nums):
                if nums[i] != previous:
                    for p in permute(nums[:i] + nums[i+1:]):
                        ans.append([n] + p)
                    previous = nums[i]
            return ans

        return permute(nums)

        # This built-in permutations with set operation.
        # from itertools import permutations
        # print list(set(permutations(nums)))

if __name__ == '__main__':
    nums = [1, 1, 2]
    print Solution().permuteUnique(nums)

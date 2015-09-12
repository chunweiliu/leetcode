class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # # Generate permutation indices
        # if len(nums) == 0:
        #     return [[]]
        # previous = self.permute(nums[1:])
        # return [previous[:i] + [nums[0]] + previous[i:]
        #         # BUG: previous is a list of list, not a list you want.
        #         for i in range(len(previous) + 1)]

        # https://leetcode.com/discuss/42550/one-liners-in-python
        # Take any number as the fist number and append any permutation of
        # other number.
        # return [[n] + p
        #         for i, n in enumerate(nums)
        #         for p in self.permute(nums[:i] + nums[i+1:])] or [[]]

        # Use reduce to insert the next number in the permuted part.
        # reduce(function, iterable[, initializer])
        # function e.g lambda x + y: The left argument, x, is the accumulated
        # val. and the right argument, y, is the update val. from the iter.
        # [] -> list, () -> generator        
        return reduce(lambda pp, n: [p[:i] + [n] + p[i:]
                                     for p in pp for i in range(len(p) + 1)],
                      nums, [[]])

if __name__ == '__main__':
    nums = [0, 1, 2]
    print Solution().permute(nums)

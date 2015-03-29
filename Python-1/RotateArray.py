import unittest


class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        """Try to think as many solutions as you can
        1) array concatenation using slicing syntax, Space: O(n)
         - can do inplace
        2) looping with module index, Space: O(n)
        3) swaping, Space: O(1) -> (X)
        4) three-time reversing
        """
        k = k % len(nums)

        # 1)
        # return nums[k+1:] + nums[:k+1]  # create a new copy
        nums[:] = nums[-k:] + nums[:-k]  # slice assignment (in-place)
        return nums  # just for value check

        # 2)
        # rnums = [0] * len(nums)
        # for i in range(len(nums)):
        #     rnums[i] = nums[(i+k+1) % len(nums)]
        # return rnums


class Test(unittest.TestCase):
    def test_rotate1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        rnums = [5, 6, 7, 1, 2, 3, 4]
        self.assertEqual(Solution().rotate(nums, k), rnums)

    def test_rotate2(self):
        nums = [1, 2]
        k = 0
        rnums = [1, 2]
        self.assertEqual(Solution().rotate(nums, k), rnums)

if __name__ == '__main__':
    unittest.main()

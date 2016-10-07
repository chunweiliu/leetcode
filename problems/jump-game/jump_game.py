class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Just check the reachable place
        max_approach = 0
        for i, num in enumerate(nums):
            if i > max_approach:
                return False
            max_approach = max(i + num, max_approach)
        return True

        # TLE
        # farest = [0] * len(nums)
        # for i, num in enumerate(nums):
        #     approach = max(farest[:i]) if i > 0 else num
        #     farest[i] = max(i + num, approach) if approach >= i else 0
        # return len(farest) == 1 or max(farest[:-1]) >= len(nums) - 1

if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    # nums = [3, 2, 1, 0, 4]
    # nums = [0, 2, 3]
    # nums = [0]
    print Solution().canJump(nums)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 4 5 6 7 0 1 2
        # Divide the nums to two part, make sure which part is in order.
        i, j = 0, len(nums) - 1
        while i <= j:
            m = i + (j - i) / 2
            if nums[m] == target:
                return m

            # Aware the corner case: When m == i, we can't advance i without =.
            # Think about the case [3, 1], target 1. What's the reason behind?
            if nums[i] < nums[m]:  # MUST USE '='.
                if nums[i] <= target < nums[m]:
                    j = m - 1
                else:
                    i = m + 1
            else:  # The post part is in order.
                if nums[m] < target <= nums[j]:
                    i = m + 1
                else:
                    j = m - 1
        return -1

if __name__ == '__main__':
    nums = [3, 1]
    target = 1
    print Solution().search(nums, target)

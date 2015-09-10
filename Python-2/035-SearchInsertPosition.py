class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # A modified binary search
        insert_position = 0  # The corner case should be set as 0.
        i, j = 0, len(nums) - 1
        while i <= j:
            m = i + (j - i) / 2
            if nums[m] == target:
                return m

            # How to record the index we just found before? The trick is when
            # to update the `insert_position`. Because we are going to insert
            # the target "after" the closest number, we only update when we
            # find a smaller candidate. The defalut insert position is 0.
            if nums[m] < target:
                i = m + 1
                insert_position = i
            else:
                j = m - 1
        return insert_position

if __name__ == '__main__':
    nums = [0, 2]
    target = -1
    print Solution().searchInsert(nums, target)

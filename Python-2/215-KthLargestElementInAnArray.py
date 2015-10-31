import random


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start < end:
            pivot_index = self.partition(nums, start, end)
            if pivot_index < k:
                # We don't want to change the rank before the pivot_index,
                # if it's smaller than k.
                # [-----------|---------|-----]
                #  (ranked)   pivot     k
                #              start
                start = pivot_index + 1
            else:
                # [-----------|---------|-----]
                #  (unranked) k         pivot
                #                      end
                end = pivot_index - 1
        return nums[k - 1]

    def partition(self, nums, start, end):
        pivot_index = random.randrange(start, end + 1)
        pivot = nums[pivot_index]

        bottom, middle, upper = start, start, end
        while middle <= upper:
            if nums[middle] > pivot:
                nums[bottom], nums[middle] = nums[middle], nums[bottom]
                bottom += 1
                middle += 1
            elif nums[middle] == pivot:
                middle += 1
            else:
                nums[middle], nums[upper] = nums[upper], nums[middle]
                upper -= 1
        return bottom

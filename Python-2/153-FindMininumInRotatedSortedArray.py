class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = -1, len(nums)
        min_num = nums[0]
        while end - start > 1:
            mid = (end - start) / 2 + start

            # For this problem, if we want to use the binary search framework,
            # which start and end are not the part of the solution, we have to
            # use a variable for updating what we saw everytime.
            min_num = min(min_num, nums[mid])

            # nums[start + 1:end - 1] is always not sorted.
            if nums[mid] > nums[end - 1]:
                start = mid
            else:
                end = mid
        return min_num

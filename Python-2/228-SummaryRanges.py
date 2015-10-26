class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return nums

        def check_range(left, right, ranges):
            if left != right:
                ranges.append(str(left) + '->' + str(right))
            else:
                ranges.append(str(left))

        ranges = []
        left, right = nums[0], nums[0]
        for num in nums[1:]:
            if num - right == 1:
                right = num
            else:
                check_range(left, right, ranges)
                left, right = num, num
        # Becareful about the last range.
        check_range(left, right, ranges)
        return ranges

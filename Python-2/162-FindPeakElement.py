class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums) - 1
        while i + 1 < j:  # Maintain three elements at least
            m = i + (j - i) / 2

            if nums[m-1] < nums[m] and nums[m] > nums[m+1]:
                return m

            if nums[m-1] < nums[m]:
                i = m + 1
            else:
                j = m - 1

        # If the number of elements is less than three
        return i if nums[i] > nums[j] else j

if __name__ == '__main__':
    nums = [2, 1, 2]
    print Solution().findPeakElement(nums)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = -1, len(nums)
        while end - start > 1:
            mid = (end - start) / 2 + start

            # This loop invariant is complicated, so we
            # return immediately when we found the target.
            if nums[mid] == target:
                return mid

            if nums[start + 1] <= nums[mid]:
                if nums[start + 1] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target <= nums[end - 1]:
                    start = mid
                else:
                    end = mid
        return -1

if __name__ == '__main__':
    nums = [3, 31]
    target = 1
    print Solution().search(nums, target)

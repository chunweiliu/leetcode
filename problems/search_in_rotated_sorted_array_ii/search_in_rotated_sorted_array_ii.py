class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # Search in a duplicatedly and rotately sorted array.
        # [1, 6, 1, 1, 1, 1] search 6
        i, j = 0, len(nums) - 1
        while i <= j:
            m = i + (j - i) / 2
            if nums[m] == target:
                return True

            if nums[i] < nums[m]:  # left half is sorted.
                if nums[i] <= target < nums[m]:
                    j = m - 1
                else:
                    i = m + 1
            elif nums[i] > nums[m]:  # right half is sorted.
                if nums[m] < target <= nums[j]:
                    i = m + 1
                else:
                    j = m - 1
            else:
                # If nums[i] == nums[m]: 1) All numbers betwen i, j are same.
                # 2) Different numbers might existed. We can't distinguish them
                # Therefore, repeat the process again by adding 1 to the left.
                i += 1
        return False


if __name__ == '__main__':
    nums = [3, 1, 1]
    target = 3
    print Solution().search(nums, target)

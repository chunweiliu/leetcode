class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Dutch flag algorithm: O(log n)
        # Partition in three categories:
        # 00011122222
        #   i  jk
        i, j, k = 0, 0, len(nums) - 1
        while j <= k:  # Test every element between j and k.
            if nums[j] == 1:
                j += 1
            elif nums[j] < 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1

if __name__ == '__main__':
    nums = [0, 1, 2, 0, 1, 2]
    Solution().sortColors(nums)
    print nums

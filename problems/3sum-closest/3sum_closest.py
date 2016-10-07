class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Reduce the problem to TwoSum. But modify the condition in it.
        nums.sort()

        closest = nums[0] + nums[1] + nums[2]  # Use an feasiable solution.
        for i, num in enumerate(nums):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                x = num + nums[j] + nums[k]
                if x == target:
                    return target
                else:
                    if abs(closest - target) > abs(x - target):
                        closest = x
                    if x > target:
                        k -= 1
                    else:
                        j += 1
        return closest

if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    print Solution().threeSumClosest(nums, target)

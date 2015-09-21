class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # TwoSum -> O(n). If we apply TwoSum for each element, we have a three
        # sum algo in O(n ** 2). However, dependsing on how we implment TwoSum,
        # the speed is different. Recreate a hash table each time getting a TLE
        # Duplicates need to be deleted.
        nums.sort()

        ans = list()
        for i, num in enumerate(nums):
            candidates = self.TwoSum(nums[i + 1:], -num)
            if len(candidates) > 0:
                for (first, second) in candidates:
                    candidate = [num, first, second]
                    if candidate not in ans:
                        ans.append(candidate)
        return ans

    def TwoSum(self, nums, target):
        # Assume the nums has been sorted.
        ans = list()
        i, j = 0, len(nums) - 1
        while i < j:
            x = nums[i] + nums[j]
            if x == target:
                ans.append((nums[i], nums[j]))
                i += 1
                j -= 1
            elif x < target:
                i += 1
            else:
                j -= 1
        return ans

    # def TwoSum(self, nums, target):
    #     # Assume there is no duplicate element.
    #     index = defaultdict(lambda: -1)
    #     for i, num in enumerate(nums):
    #         index[num] = i
    #     for i, num in enumerate(nums):
    #         j = index[target - num]
    #         if j != i and j != -1:  # Duplicates detected
    #             return min(num, target - num), max(num, target - num)
    #     return None, None

if __name__ == "__main__":
    nums = [-2, 0, 1, 1, 2]
    print Solution().threeSum(nums)

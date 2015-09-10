from collections import defaultdict


class Solution(object):
    def fourSum(self, nums, target):
        # Time: O(n ** 2) in average
        # Space: O(n ** 2)
        # Reduce to TwoSum of elements. Each element is a pair sum.
        nums.sort()

        pairs = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums)):
                key = nums[i] + nums[j]
                if i < j and [i, j] not in pairs[key]:
                    pairs[key].append([i, j])

        ans = list()
        for key in sorted(pairs.keys()):
            if len(pairs[target - key]) > 0:
                indices = [first + second
                           for first in pairs[key]
                           for second in pairs[target - key]
                           if len(set(first + second)) == 4]
                for index in indices:
                    index.sort()
                    candidate = [nums[i] for i in index]
                    if candidate not in ans:
                        ans.append(candidate)
        return ans

    def FourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Reduce to 3Sum O(n ** 2)
        # Time: O(n ** 3)
        # Space: O(1)
        nums.sort()

        ans = list()
        for i in range(len(nums)):
            three_sum = self.ThreeSum(nums[i + 1:], target - nums[i])
            if len(three_sum) > 0:
                for (f, s, t) in three_sum:
                    x = [nums[i], f, s, t]
                    if x not in ans:
                        ans.append(x)
        return ans

    def ThreeSum(self, nums, target):
        ans = list()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                x = nums[i] + nums[j] + nums[k]
                if x == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif x < target:
                    j += 1
                else:
                    k -= 1
        return ans

if __name__ == "__main__":
    nums = [-3, -2, -1, 0, 0, 1, 2, 3]
    target = 0
    print Solution().fourSum(nums, target)

from collections import defaultdict


class Solution(object):
    def fourSum(self, nums, target):
        # Time: O(n ** 2) in average
        # Space: O(n ** 2)
        # Reduce to TwoSum of elements. Each element is a pair sum.
        nums.sort()

        # Take each pair as a new element for two sum problem
        pairs = defaultdict(list)
        for i, n in enumerate(nums):
            for j in range(i, len(nums)):
                key = n + nums[j]
                if [i, j] not in pairs[key]:
                    pairs[key].append([i, j])

        # Solve the two sum problem
        ans = []
        for key in sorted(pairs.keys()):
            if pairs[target - key]:
                indicies = [first + second
                            for first in pairs[key]
                            for second in pairs[target - key]
                            if len(set(first + second)) == 4]
                for index in indicies:
                    index.sort()
                    candidate = [nums[i] for i in index]
                    if candidate not in ans:
                        ans.append(candidate)
        return ans

    def four_sum(self, nums, target):
        # O(n^3)
        nums.sort()
        ans = []
        for i, n in enumerate(nums):
            if i >= 1 and nums[i] == nums[i-1]:  # [BUG] i > 1
                continue
            ans_three_sum = self.three_sum(nums[i+1:], target - n)
            if ans_three_sum:
                ans += [[n] + pair for pair in ans_three_sum]
        return ans

    def three_sum(self, nums, target):
        # sort the nums if need.
        # nums.sort()
        ans = []
        for i, n in enumerate(nums):
            if i >= 1 and nums[i] == nums[i-1]:  # [BUG] i > 1
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                x = n + nums[j] + nums[k]
                if x == target:
                    ans.append([n, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif x < target:
                    j += 1
                else:
                    k -= 1
        return ans

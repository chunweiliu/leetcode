class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # O(n) time, O(k) space sliding windows (better implementation)
        window = {}
        for i, num in enumerate(nums):
            if num in window and i - window[num] <= k:
                return True
            window[num] = i
        return False

        # O(n) time, O(k) space sliding windows
        # if not nums:
        #     return False
        #
        # from collections import Counter
        # window = Counter(nums[:k+1])
        # if any([value > 1 for value in window.values()]):
        #     return True
        #
        # for i in range(k + 1, len(nums)):
        #     window[nums[i - k - 1]] -= 1
        #     window[nums[i]] += 1
        #     if window[nums[i]] > 1:
        #         return True
        # return False

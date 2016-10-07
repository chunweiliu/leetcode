class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return nums

        from collections import deque
        # The queue stores the index of useful elements which might
        # be the largest element in the sliding window. The queue is
        # maintained in a decending order of values.
        q = deque()

        for i in range(k):
            # The previous smaller element is useless.
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        maxs = []
        for i in range(k, len(nums)):
            # The element in the front is the largest element.
            maxs.append(nums[q[0]])

            # Remove the out of window elements in the front.
            while q and q[0] <= i - k:
                q.popleft()

            # Remove smaller elements from the back.
            while q and nums[i] >= nums[q[-1]]:
                q.pop()

            q.append(i)

        # Deal with the last window.
        maxs.append(nums[q[0]])
        return maxs

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Find the kth element for two cases
        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            return self.find_kth(nums1, nums2, total / 2 + 1)
        else:
            return 0.5 * (self.find_kth(nums1, nums2, total / 2) +
                          self.find_kth(nums1, nums2, total / 2 + 1))

    def find_kth(self, nums1, nums2, k):
        # The stop conditions for the recursion
        if len(nums1) < len(nums2):
            return self.find_kth(nums2, nums1, k)
        if len(nums2) == 0:
            return nums1[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        # Eleminate the impossible part of the array by testing two elements
        # nums1[n - 1] and nums2[m - 1]. If nums1[n - 1] is smaller than the
        # other, means the 1th to the Nth elements of nums1 are impossible for
        # containing the solution, which has to be the Kth element (K > N).
        m = min(k / 2, len(nums2))
        n = k - m
        if nums1[n - 1] < nums2[m - 1]:
            return self.find_kth(nums1[n:], nums2, k - n)
        return self.find_kth(nums1, nums2[m:], k - m)

if __name__ == "__main__":
    nums1 = [1, 2, 3, 4]
    nums2 = [5]
    print Solution().findMedianSortedArrays(nums1, nums2)


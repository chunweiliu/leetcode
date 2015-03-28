class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        # Using recursive to find the kth element
        # Time: O(log(m + n)), m = len(A), n = len(B)
        # Space: O(log(m + n)), recursive
        total = len(A) + len(B)
        if (total % 2) != 0:
            return self.findKth(A, B, total/2 + 1)
        else:
            return .5 * (self.findKth(A, B, total/2) + self.findKth(A, B, total/2 + 1))

    def findKth(self, A, B, k):
        # assume |A| > |B|
        if len(A) < len(B):
            return self.findKth(B, A, k)
        if len(B) == 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])

        pb = min(k / 2, len(B))
        pa = k - pb
        if A[pa - 1] < B[pb - 1]:
            return self.findKth(A[pa:], B, k - pa)
        else:
            return self.findKth(A, B[pb:], k - pb)

if __name__ == "__main__":
    A = [1]
    B = [2, 3, 4, 5, 6]
    print Solution().findMedianSortedArrays(A, B)

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        """Max continous product. DP: A[i], A[i]*pre_min, A[i]*pre_max
        Time: O(n)
        Space: O(1)
        Conner cases: len(A) == 0, 1
        """
        if len(A) == 0:
            return A

        max_so_far = A[0]
        pre_min = A[0]
        pre_max = A[0]

        for x in A[1:]:
            min_now = min(min(pre_min*x, pre_max*x), x)
            max_now = max(max(pre_min*x, pre_max*x), x)
            max_so_far = max(max_so_far, max_now)
            pre_min = min_now
            pre_max = max_now

        return max_so_far

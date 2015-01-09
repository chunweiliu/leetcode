class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        # Binary search using more conditions to eliminate candidates
        # Time: O(log n)
        # Space: O(1)
        p, q = 0, len(A) - 1
        while p <= q:
            m = p + (q - p) / 2
            if A[m] == target:
                return m
            # Check order outside
            if A[p] <= A[m]:  # WA: if wrote A[p] < A[m]
                # write down the easy if, and let else handle other cases
                if A[p] <= target and target <= A[m]:
                    q = m - 1
                else:
                    p = m + 1
            else:
                if A[m] <= target and target <= A[q]:
                    p = m + 1
                else:
                    q = m - 1
        return -1

if __name__ == "__main__":
    A = [3, 1]
    target = 1
    print Solution().search(A, target)

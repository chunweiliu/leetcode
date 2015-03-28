class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        p = m - 1
        q = n - 1

        if p < 0:
            while q >= 0:
                A[q] = B[q]
                q -= 1

        # array can be indexed from the end
        while p + q >= -1:  # BOUDUARY CONDTION!
            if p < 0:
                A[p + q + 1] = B[q]
                q -= 1
            elif q < 0:
                A[p + q + 1] = A[p]
                p -= 1
            elif A[p] < B[q]:
                A[p + q + 1] = B[q]
                q -= 1
            else:
                A[p + q + 1] = A[p]
                p -= 1

        print A

if __name__ == "__main__":
    A = [2, 0]
    m = 1
    B = [1]
    n = 1
    Solution().merge(A, m, B, n)

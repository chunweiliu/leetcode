class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if A == []:
            return 0

        p = 0
        q = len(A)
        while p < q:
            if A[p] == elem:
                q -= 1
                # swap two elements
                A[p], A[q] = A[q], A[p]
            else:
                p += 1
        return p

if __name__ == "__main__":
    A = [4]
    elem = 4
    Solution().removeElement(A, elem)

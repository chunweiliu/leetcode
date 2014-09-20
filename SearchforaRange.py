class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        # Binary search, do it twice
        # Time: O(log n)
        # Space: O(n)
        pivot = self.binarySearch(A, target)

        # search for left bound
        prev = pivot
        if pivot != 0:
            left = A[:pivot]  # A[start_index,len,dir]
            while left:
                l = self.binarySearch(left, target)
                if l == -1:
                    break
                else:
                    if l == 0:  # prevent negative index
                        left = []
                    else:
                        left = A[:l]
                    prev = l
        l = prev

        # search for right bound, be aware of the right index
        prev = pivot
        if pivot != len(A) - 1:
            right = A[pivot + 1:]
            while right:
                r = self.binarySearch(right, target)
                if r == -1:
                    break
                else:
                    r += (prev + 1)  # correct indexing
                    right = A[r + 1:]
                    prev = r
        r = prev

        return [l, r]

    def binarySearch(self, A, target):
        p, q = 0, len(A) - 1
        while p <= q:
            m = p + (q - p) / 2
            if A[m] == target:
                return m
            elif A[m] < target:
                p = m + 1
            else:
                q = m - 1
        return -1

if __name__ == "__main__":
    A = [0,0,0,0,0,1,1,2,2,3,4,4,5,5,5,5,6,7]
    target = 0
    print Solution().searchRange(A, target)

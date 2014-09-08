class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        # trivial case
        if target < min(A):
            return 0
        if target > max(A):
            return len(A)

        # x in the middle
        for x in range(len(A)):
            if target == A[x]:
                return x
            elif target > A[x] and target < A[x + 1]:
                return x + 1

if __name__ == "__main__":
    A = [1, 3, 5, 6]
    target = 0
    print Solution().searchInsert(A, target)

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        padding = 0
        p = 0
        for x in range(len(A) - 1):
            if A[x] == A[x + 1]:
                padding += 1
            else:
                p += 1
            A[p] = A[p + padding]
        return len(A) - padding

if __name__ == "__main__":
    A = [0, 0, 0, 1, 2, 2, 3, 4]
    print Solution().removeDuplicates(A)
    print A

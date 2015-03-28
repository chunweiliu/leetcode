class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        appears = [0] * 1000   # Constant space :P
        for x in A:
            if x > 0:
                appears[x - 1] = 1

        for x in range(len(appears)):
            if appears[x] == 0:
                return x + 1

if __name__ == "__main__":
    A = [3, 4, -1, 1]
    print Solution().firstMissingPositive(A)

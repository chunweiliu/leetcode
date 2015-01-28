class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        # Do you have both positive and negative integers?
        # Does A sorted?
        # A = [1 1 2 3 3] -> find 2
        # A = [1 2 3 3 1] -> find 2
        # A = [3 2 1 3 1] -> find 2
        # XOR

        single = 0
        for x in range(len(A)):
            single ^= A[x]
        return single

if __name__ == "__main__":
    A = [2, 2]
    print Solution().singleNumber(A)

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        # The array is an ORDER one!
        # Time: O(n), Space: O(1) using order, O(n) (hashmap)
        if len(A) <= 2:
            return len(A)
        p = 2
        for x in range(2, len(A)):
            if A[x] != A[p - 2]:
                A[p] = A[x]
                p += 1
        return p



if __name__ == "__main__":
    A = [1, 1, 1, 2, 2, 3, 4, 4, 4]
    print Solution().removeDuplicates(A)

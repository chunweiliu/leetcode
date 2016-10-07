class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int

        Example: 
        A    = [a, b, c, d]
        B(4) =  0  1  2  3
        B(3) =  3  0  1  2
        B(2) =  2  3  0  1
        B(1) =  1  2  3  0

        hint: 
        F(4) - F(3) = b + c + d - 3a
                    = (a + b + c + d) - 4a
        => F(k) - F(k-1) = sum(A) - len(A) * A[-k]
        => F(k) = F(k-1) + sum(A) - len(A) * A[-k]

        Time:
        O(n^2) for brute force, since F is O(n).
        Reduce F to O(1) by the hint.

        """
        array_sum = sum(A)
        max_value = previous = sum([i * number for i, number in enumerate(A)])
        for i in range(1, len(A)):
            previous += array_sum - len(A) * A[-i]
            max_value = max(max_value, previous)
        return max_value

A = [1,2]
print Solution().maxRotateFunction(A)
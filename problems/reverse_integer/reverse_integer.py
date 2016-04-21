class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Conner cases? If don't care, just use Python's big integer class.
        sign = -1 if x < 0 else 1
        x *= sign

        n = 0
        while x > 0:
            n += x % 10
            x /= 10
            n *= 10

        ans = sign * n / 10
        if ans > 2 ** 31 - 1:
            return 0
        if ans < -2 ** 31:
            return 0
        return ans


if __name__ == "__main__":
    x = -123  # This statement created a new number object.
    # The function created a new variable point to the same object above, but
    # use a new name. So If you do some class operation directly on the object
    # in the function, the global x will be changed. Otherwise, the numerical
    # operations like +=, -=, /=, *= won't change the global scope x.
    print Solution().reverse(x)
    print x  # No, the x won't change.

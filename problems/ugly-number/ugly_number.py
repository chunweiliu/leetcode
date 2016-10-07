class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # If a number has any prime factor other than 2, 3, 5, it's a ugly one.
        if num == 0:
            return False

        prime_factors = [2, 3, 5]
        for prime_factor in prime_factors:
            while num % prime_factor == 0:
                num //= prime_factor
        return True if num == 1 else False

if __name__ == '__main__':
    num = 0
    print Solution().isUgly(num)

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int

        Problem: Given an integer n, return the number of trailing zeroes in n!.
        Your solution should be in logarithmic time complexity.

        The number of trailing zeros 
        = how many fives in the n!

        Example: 
        numbers: 5 ... 10 ... 15 ... 20 ... 25 ... 30
        fives:   1      1      1      1      1      1  (first iteration)
                                             1         (second interation)

        Since 5 x 2 = 10, and we definitely have more 2s than 5s in factorial.
        """
        fives = 0
        while n > 0:
            fives += n / 5
            n /= 5
        return fives

if __name__ == "__main__":
	print Solution().trailingZeroes(30)

        
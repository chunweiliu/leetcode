class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.is_happy(n, set())

    def is_happy(self, number, exist):
        number_square_sum = self.square_sum(number)

        if number_square_sum == 1:
            return True
        elif number_square_sum in exist:
            return False
        else:
            exist.add(number_square_sum)
            return self.is_happy(number_square_sum, exist)

    def square_sum(self, number):
        ss = 0
        while number:
            ss += (number % 10) ** 2
            number /= 10
        return ss

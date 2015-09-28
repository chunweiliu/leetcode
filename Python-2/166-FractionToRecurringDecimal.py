class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'

        if numerator * denominator < 0:
            return '-'+self.fractionToDecimal(abs(numerator), abs(denominator))

        # Get the quotient.
        num = str(numerator / denominator)

        # Get the residual.
        residual = numerator % denominator
        if residual == 0:
            return num
        else:
            num += '.'

        # Process the residual.
        existed_position = {}
        while residual:
            if residual in existed_position:
                num = (num[:existed_position[residual]] + '(' +
                       num[existed_position[residual]:] + ')')
                return num
            else:
                existed_position[residual] = len(num)
                residual *= 10
                num += str(residual / denominator)
                residual %= denominator
        return num

if __name__ == '__main__':
    numerator = 1
    denominator = 3
    print Solution().fractionToDecimal(numerator, denominator)

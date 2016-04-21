class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # The maximum number is 3999
        forth = ['', 'M', 'MM', 'MMM']
        third = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        second = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        first = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        return (forth[num / 1000] + third[num % 1000 / 100] +
                second[num % 100 / 10] + first[num % 10])

if __name__ == "__main__":
    print Solution().intToRoman(19)

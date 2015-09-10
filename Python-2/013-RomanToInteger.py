class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Input is from 1 to 3999
        forth = ['', 'M', 'MM', 'MMM']
        third = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        second = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        first = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

        num = 0
        k = 0
        romans = [first, second, third, forth]
        for i, roman in reversed(list(enumerate(romans))):
            for j, number in reversed(list(enumerate(roman))):
                if number == s[k:k + len(number)]:
                    num += j * 10 ** i
                    k += len(number)
        return num

if __name__ == "__main__":
    print Solution().romanToInt('XXX')

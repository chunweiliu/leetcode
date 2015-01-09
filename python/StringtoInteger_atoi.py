class Solution:
    # @return an integer
    def atoi(self, str):
        """Conner cases
        Valid:
        1. space in the front
        2. sign
        3. digits
        4. characters in the end
        5. range
        Not valid:
        1. empty string
        2. first element is character
        """
        if len(str) == 0:
            return 0

        # skip leading space
        p = 0
        while p < len(str) and str[p] == ' ':
            p += 1

        # sign check
        sign = 1
        if str[p] == '-':
            sign = -1
            p += 1
        elif str[p] == '+':
            p += 1

        digits = 0
        while p < len(str) and str[p].isdigit():
            digits = digits*10 + int(str[p])
            p += 1

        if p == 0:
            return 0
        else:
            # range check for integer
            ret = sign * digits
            if ret > 2147483647:
                return 2147483647
            if ret < -2147483648:
                return -2147483648
            return ret

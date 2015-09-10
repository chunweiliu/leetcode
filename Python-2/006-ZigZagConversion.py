class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        array = ['' for x in range(numRows)]
        i = 0
        for x in s:
            array[i] += x
            if i == 0:
                d = 1
            elif i == numRows - 1:  # How about numRows == 1?
                d = -1
            i += d
        return ''.join(array)

if __name__ == "__main__":
    print "AB" == Solution().convert("AB", 1)

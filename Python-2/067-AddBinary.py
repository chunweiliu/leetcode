class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Big number addition. If possible, use bit operation.
        s = ''
        i, j = -1, -1
        n, m = len(a), len(b)
        c = 0
        while i >= -n or j >= -m:
            x = (int(a[i]) if i >= -n else 0) + \
                (int(b[j]) if j >= -m else 0) + c
            s += str(x % 2)
            c = x // 2
            i -= 1
            j -= 1
        if c > 0:
            s += '1'
        return s[::-1]

if __name__ == '__main__':
    a = '11'
    b = '10'
    print Solution().addBinary(a, b)

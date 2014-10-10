class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        """Bit operation
        Time: O(n)
        Space: O(1)
        Corner: carry
        """
        if a is None:
            return b
        if b is None:
            return a

        # add as binary
        a, b = list(a), list(b)
        c = list()
        s = 0
        while a or b:
            s /= 2
            if a:
                s += a[-1]
                a.pop()
            if b:
                s += b[-1]
                b.pop()
            c.append(s % 2)
        if s/2 > 0:
            c.append(1)
        return ''.join(map(str, c[::-1]))

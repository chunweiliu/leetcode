# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        total_char_read = 0
        while total_char_read < n:
            buf4 = [''] * 4
            num_char = read4(buf4)
            if num_char == 0:
                return total_char_read
            buf[total_char_read:total_char_read+num_char+1] = buf4
            total_char_read += num_char

        if total_char_read > n:
            buf = buf[:n-total_char_read]
        return n

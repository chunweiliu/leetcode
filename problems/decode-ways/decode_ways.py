class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 'A' -> 1
        # 'B' -> 2 ...
        # 'Z' -> 26
        # DP, Similar to Climbing Stairs
        # Count[i] = Count[i - 1] + Count[i - 2], if s[i - 2: i - 1] is vaild.
        #          = Count[i - 1] Otherwise, if s[i - 1] is vaild.
        prev, curr = 0, int(s > '')
        p = ''
        for d in s:
            temp = curr
            curr = curr * (d > '0') + prev * ('10' <= p+d <= '26')
            prev = temp  # Use the non-update one as the previous one.
            p = d
        return curr


if __name__ == '__main__':
    s = '111'  # AAA, AK, KA
    print Solution().numDecodings(s)

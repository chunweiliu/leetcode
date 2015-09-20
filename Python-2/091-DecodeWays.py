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
        # Count[i] = Count[i - 1]
        #          | Count[i - 1] + Count[i - 2], if s[i - 2: i - 1] is vaild.

        prev_ways = 0
        curr_ways = int(s > '')  # If no input, return this value without loop.
        p = ''  # as previous digit
        for d in s:
            prev_ways, curr_ways, p = (
                curr_ways,
                (d > '0') * curr_ways + (9 < int(p+d) < 27) * prev_ways,
                d)
        return curr_ways

if __name__ == '__main__':
    s = '111'  # AAA, AK, KA
    print Solution().numDecodings(s)

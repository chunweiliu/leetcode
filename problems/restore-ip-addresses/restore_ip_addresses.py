class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        for i in range(1, len(s)):
            for j in range(i + 1, i + 4):
                for k in range(j + 1, j + 4):
                    if k < len(s):
                        ip = [s[:i], s[i:j], s[j:k], s[k:]]

                        # Valid numbers and valid string
                        if (all([0 <= int(x) <= 255 for x in ip]) and
                                all([x == '0' or x[0] != '0' for x in ip])):
                            ans.append('.'.join(ip))
        return ans

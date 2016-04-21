class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest_lenght = 1000
        shortest_string = ""
        for s in strs:
            if len(s) < shortest_lenght:
                shortest_lenght = len(s)
                shortest_string = s

        for i in range(shortest_lenght):
            common = True
            for s in strs:
                common = s[i] == shortest_string[i]
                if not common:
                    return shortest_string[:i]
        return shortest_string

if __name__ == "__main__":
    strs = ['ab', 'ab', 'ab', 'abc']
    print Solution().longestCommonPrefix(strs)

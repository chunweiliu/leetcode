class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        # Conner cases: no string, only one string, many empty strings
        # different lengths of strings
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        common_index = -1
        done = False
        while not done:
            common_index += 1
            try:
                s = strs[0][common_index]
            except IndexError:
                break

            for string in strs:
                try:
                    if string[common_index] != s:
                        done = True
                except IndexError:
                    done = True
                    break
        return strs[0][:common_index]

if __name__ == "__main__":
    strs = ['aa', 'aaa']
    print Solution().longestCommonPrefix(strs)

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        # Walk from the end to detect space
        # Time: O(n)
        # Space: O(1)
        sr = s[::-1]
        count = 0
        for x in range(len(sr)):
            if sr[x] == " " and count == 0:  # special case
                pass
            elif sr[x] == " ":
                break
            else:
                count += 1
        return count

if __name__ == "__main__":
    s = "a bbb   "
    print Solution().lengthOfLastWord(s)

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Find the edit distance between two words
        # 1) insert
        # 2) delete
        # 3) replace
        # table[i][j] = min(table[i-1][j] + 1, table[i][j-1] + 1,
        #                    table[i-1][j-1] + 1 if not match else 0)
        #   0 a
        # 0 0 1
        # b 1 1
        m, n = len(word1), len(word2)
        if m == 0:
            return n
        if n == 0:
            return m

        table = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            table[i][0] = i
        for j in range(n + 1):
            table[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                table[i][j] = \
                    min(min(table[i-1][j] + 1, table[i][j-1] + 1),
                        table[i-1][j-1] + (word1[i-1] != word2[j-1]))
        return table[-1][-1]

if __name__ == '__main__':
    word1, word2 = 'ab', 'bc'
    print Solution().minDistance(word1, word2)

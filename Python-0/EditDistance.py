class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        """DP
        cost(word1, word2) =
        if word1[-1] == word2[-1]:
            cost(word1[:m-1], word2[:n-1])
        else:
            1 + min of
            cost(word1[:m-1], word2[:n-1])  # substitute last w1 with last w2
            cost(word1[:m-1], word2)  # insert the last of w1
            cost(word1, word2[:n-1])  # delete the last of w2
        Time: O(mn)
        Space: O(n), n is the smaller one
        Conners: word2 is empty string
        """
        if len(word1) < len(word2):
            word1, word2 = word2, word1

        columns = len(word2) + 1
        last_costs = range(columns)
        for i, w1 in enumerate(word1):
            this_costs = [i + 1] * columns
            for j, w2 in enumerate(word2):
                if w1 == w2:
                    this_costs[1 + j] = last_costs[j]
                else:
                    this_costs[1 + j] = 1 + min(this_costs[j], min(
                        last_costs[j], last_costs[1 + j]))
            last_costs = this_costs
        return last_costs[-1]

if __name__ == "__main__":
    word1 = 'a'
    word2 = 'cb'
    print Solution().minDistance(word1, word2)

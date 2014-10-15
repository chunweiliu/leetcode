class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        # assume the words in dictionary do not appear twice in s
        all_sentences = []
        data = []
        for word in dict:
            p = s.index(word)
            if p >= 0:
                data.append((p, len(word), word))
        sorted(data, key=lambda k: k[1])

        return data


if __name__ == "__main__":
    s = "catsanddog"
    dict = set(["cat", "cats", "and", "sand", "dog"])
    print Solution().wordBreak(s, dict)

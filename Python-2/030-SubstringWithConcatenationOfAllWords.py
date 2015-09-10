class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # Generate a permutation for all posible substrings.
        # Time: O(#words! * #s)
        # from itertools import permutations
        # ans = list()
        # for indices in permutations(range(len(words))):
        #     substring = ''.join([words[i] for i in indices])
        #     index = s.find(substring)
        #     if index != -1:
        #         ans.append(index)
        # return ans

        # hash('foo') + hash('bar') == hash('bar') + hash('foo')
        # Time: O(#s * #total_char)
        # ans = list()
        # hash_sum = sum([hash(x) for x in words])  # Duplicates make it slow.
        # num_word = len(words)
        # num_char = len(words[0])
        # for i in range(len(s) - num_word * num_char + 1):
        #     hash_substring = [hash(s[i + j*num_char:i + (j + 1)*num_char])
        #                       for j in range(num_word)]
        #     if sum(hash_substring) == hash_sum:
        #         ans.append(i)
        # return ans

        # Histogram
        # Time: O(#s * #total_char)
        ans = list()
        histogram = dict((x, words.count(x)) for x in set(words))
        num_word = len(words)
        num_char = len(words[0])
        for i in range(len(s) - num_char * num_word + 1):
            counter = dict(histogram)
            j = 0
            while j < num_word:
                word = s[i + j * num_char: i + (j + 1) * num_char]
                if word in counter and counter[word] > 0:
                    counter[word] -= 1
                else:
                    break  # This makes the program faster.
                j += 1
            if j == num_word:
                ans.append(i)
        return ans


if __name__ == '__main__':
    s = 'barfoothefoobarman'
    words = ['foo', 'bar']
    print Solution().findSubstring(s, words)

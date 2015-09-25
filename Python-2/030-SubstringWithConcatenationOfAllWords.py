from collections import defaultdict


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        length_word = len(words[0])
        word_hist = dict([(word, words.count(word)) for word in set(words)])

        # We only need to check offset form [0, length_word - 1].
        # Time O(|s|) = O(|word| * |s| / |word|)
        ans = []
        for offset in range(length_word):
            left = offset
            counter = defaultdict(int)
            count = 0

            # Check each substring.
            for i in range(offset, len(s) - length_word + 1, length_word):
                word = s[i:i+length_word]
                if word in word_hist:
                    counter[word] += 1
                    count += 1

                    # If it is a valid word but has seen before
                    # (i.e. a duplicate), forward begin pointer 'left' until
                    # previous one is removed from the current window.
                    # So we don't need to startover and count again.
                    while counter[word] > word_hist[word]:
                        counter[s[left:left+length_word]] -= 1
                        left += length_word
                        count -= 1

                    if count == len(words):
                        ans.append(left)
                else:
                    left = i + length_word
                    counter = defaultdict(int)
                    count = 0
        return ans

        # length_word = len(words[0])
        # number_word = len(words)
        # # Lookup O(1) using dictionary (using set to delete duplicate keys)
        # word_hist = dict([(x, words.count(x)) for x in set(words)])
        # ans = []
        # for i in range(len(s) - length_word * number_word + 1):
        #     j = 0
        #     counter = defaultdict(int)
        #     while j < number_word:
        #         word = s[i+j*length_word:i+(j+1)*length_word]
        #         if word in word_hist and counter[word] < word_hist[word]:
        #             counter[word] += 1
        #         else:
        #             break
        #         j += 1
        #     if j == number_word:
        #         ans.append(i)
        # return ans

        # Histogram
        # Time: O(#s * #total_char)
        # ans = list()
        # histogram = dict((x, words.count(x)) for x in set(words))
        # num_word = len(words)
        # num_char = len(words[0])
        # for i in range(len(s) - num_char * num_word + 1):
        #     counter = dict(histogram)
        #     j = 0
        #     while j < num_word:
        #         word = s[i + j * num_char: i + (j + 1) * num_char]
        #         if word in counter and counter[word] > 0:
        #             counter[word] -= 1
        #         else:
        #             break  # This makes the program faster.
        #         j += 1
        #     if j == num_word:
        #         ans.append(i)
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

        # Generate a permutation for all posible substrings.
        # Time: O(#s * #words!)
        # from itertools import permutations
        # ans = list()
        # for indices in permutations(range(len(words))):
        #     substring = ''.join([words[i] for i in indices])
        #     index = s.find(substring)
        #     if index != -1:
        #         ans.append(index)
        # return ans

if __name__ == '__main__':
    s = 'foobarfoo'
    words = ['foo', 'bar']
    print Solution().findSubstring(s, words)

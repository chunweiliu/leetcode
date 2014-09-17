class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        if words[0] == "":
            return [" " * L]

        num_words = len(words)
        p = 0
        out = list()
        while p < num_words:
            chars = 0
            words_in_line = 0
            line = list()
            first_word = True
            while chars < L:
                if first_word:
                    first_word = False
                    line.append(words[p])
                    chars += len(words[p])
                    p += 1
                    words_in_line += 1
                elif 1 + len(words[p]) + chars <= L:
                    # add words
                    line.append(' ')
                    line.append(words[p])
                    chars += (1 + len(words[p]))
                    p += 1
                    words_in_line += 1
                else:
                    # pad space
                    # if only one word, padding right
                    if words_in_line == 1:
                        line.append(' ')
                        chars += 1
                    # else padding as usual
                    for a in range(len(line)):
                        if chars == L:
                            break
                        if a % 2 == 1:
                            line[a] += ' '
                            chars += 1
                if p >= num_words:  # for the indexing
                    break
            if chars < L:  # for padding end
                line.append(' ' * int(L - chars))
            out.append("".join(line))
        return out

if __name__ == "__main__":
    # words = ["This", "is", "an", "example", "of", "text", "justification."]
    # L = 16
    # words = ["Listen", "to", "many,", "speak", "to", "a", "few."]
    # L = 6
    # words = ["a"]
    # L = 2
    words = ["Here", "is", "an", "example", "of", "text", "justification."]
    L = 14
    print Solution().fullJustify(words, L)

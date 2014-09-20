class Solution:
    # @return a list of strings, [s1, s2]
    num_to_key = dict()
    num_to_key['1'] = ''
    num_to_key['2'] = 'abc'
    num_to_key['3'] = 'def'
    num_to_key['4'] = 'ghi'
    num_to_key['5'] = 'jkl'
    num_to_key['6'] = 'mno'
    num_to_key['7'] = 'pqrs'
    num_to_key['8'] = 'tuv'
    num_to_key['9'] = 'wxyz'
    num_to_key['0'] = ' '

    def letterCombinations(self, digits):
        # Enumerate all possibles through recursive (ref: Permutations.py)
        # Time: O(n!)
        # Space: O(n)
        if len(digits) == 0:
            return [""]
        elif len(digits) == 1:
            chars = self.num_to_key[digits]
            return [c for c in chars]
        else:
            chars = self.num_to_key[digits[0]]
            old_letters = self.letterCombinations(digits[1:])
            new_letters = list()  # need a new container for combinations
            for l in old_letters:
                for c in chars:
                    new_letters.append(c + l)
            return new_letters

if __name__ == "__main__":
    digits = ''
    print Solution().letterCombinations(digits)

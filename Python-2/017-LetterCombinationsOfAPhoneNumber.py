class Solution(object):
    buttons = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
               '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ' '}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Recursively append the letters
        # Time: O(n!)
        # Space: O(n)
        if not digits:
            return list()
        elif len(digits) == 1:
            return list(self.buttons[digits[0]])
        else:
            combinations = self.letterCombinations(digits[1:])
            # List comprehension
            # combinations_ = list()
            # for letter in self.buttons[digits[0]]:
            #     for post in combinations:
            #         combinations_.append(letter + post)
            # return combinations_
            return [letter + post
                    for letter in self.buttons[digits[0]]  # Outer loop
                    for post in combinations]  # Inner loop

if __name__ == "__main__":
    print Solution().letterCombinations("234")

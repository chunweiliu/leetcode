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
            return []

        if len(digits) == 1:
            try:
                return [char for char in self.buttons[digits[0]]]
            except KeyError:
                return []

        combinations = self.letterCombinations(digits[1:])
        try:
            ans = []
            for char in self.buttons[digits[0]]:
                for combination in combinations:
                    ans.append(char + combination)
            return ans
        except KeyError:
            return combinations

        # return [letter + post
        #         for letter in self.buttons[digits[0]]  # Outer loop
        #         for post in combinations]  # Inner loop

if __name__ == "__main__":
    print Solution().letterCombinations("")

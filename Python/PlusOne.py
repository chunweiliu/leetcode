class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        """Classic question
        Time: O(n)
        Space: O(1)
        """
        if not digits:
            return []

        carry = 10
        for i, d in enumerate(reversed(digits)):  # iterative backword
            carry /= 10
            carry += d
            digits[-i-1] = carry % 10
        if carry >= 10:
            digits.insert(0, carry/10)
        return digits

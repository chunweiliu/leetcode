class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # [9, 9] -> [1, 0, 0]

        ans = []
        carry = 1
        for n in reversed(digits):
            x = n + carry
            ans.append(x % 10)
            carry = x // 10
        if carry > 0:
            ans.append(1)
        return ans[::-1]

if __name__ == '__main__':
    digits = [9, 9]
    print Solution().plusOne(digits)

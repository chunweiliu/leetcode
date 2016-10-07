class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num or num < 10:
            return num
        return self.addDigits(sum(map(int, list(str(num)))))

        # next_num = 0
        # while num > 0:
        #     next_num += num % 10
        #     num /= 10
        # return self.addDigits(next_num)

if __name__ == '__main__':
    num = 38
    print Solution().addDigits(num)

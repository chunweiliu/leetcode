class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 1, 11, 21, 1211, 111221, ...
        if n == 1:
            return '1'
        if n == 2:
            return '11'

        ans = ''
        count, previous_number = 1, self.countAndSay(n - 1)
        for i in range(1, len(previous_number)):
            if previous_number[i - 1] == previous_number[i]:
                count += 1
            else:
                ans += str(count) + previous_number[i - 1]
                count = 1
        ans += str(count) + previous_number[-1]
        return ans

if __name__ == '__main__':
    n = 5
    print Solution().countAndSay(n)

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Given a number n, return the n-bit gray code sequence
        # E.g n = 2, [00, 01, 11, 10]. "Mirror" rule
        def gray_code(n):
            if n == 0:
                return ['0']
            if n == 1:
                return ['0', '1']
            prev = gray_code(n - 1)
            return ['0' + n for n in prev] + ['1' + n for n in reversed(prev)]

        # The lambda function will take each element in the iterable behind.
        return map(lambda s: int(s, 2), gray_code(n))

        # Iterative solution.
        # start, gray_code: [0]
        # i = 0, gray_code: [0, 1]
        # i = 1, gray_code: [0, 1, 3, 2]
        # ...
        # gray_code = [0]
        # for i in range(n):
        #     gray_code += [2 ** i + n for n in reversed(gray_code)]
        # return gray_code


if __name__ == '__main__':
    n = 2
    print Solution().grayCode(n)

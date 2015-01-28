class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        # inverse string for computing
        num1 = num1[::-1]
        num2 = num2[::-1]
        ans = [0] * (len(num1) + len(num2))

        # sum up each digit without folding
        for x in range(len(num1)):
            n = int(num1[x])
            for y in range(len(num2)):
                m = int(num2[y])
                ans[x + y] += n * m

        # folding
        for x in range(len(ans)):
            if ans[x] >= 10:
                ans[x + 1] += (ans[x] / 10)
                ans[x] = ans[x] % 10
        ans = ans[::-1]

        # eleminate 0s
        none_zero = 0
        for x in range(len(ans)):
            if ans[x] == 0:
                none_zero += 1
            else:
                break
        if none_zero == len(ans):
            ans = [0]
        else:
            ans = ans[none_zero:len(ans)]
        return ''.join(str(d) for d in ans)

    def multiply2(self, num1, num2):
        """Reverse and multiply
        Time: O(nm)
        Space: O(n+m-1)
        Corner: empty string, all zeros
        """
        N, M = len(num1), len(num2)
        if N == 0 and M == 0:
            return None
        if N == 0:
            return num2
        if M == 0:
            return num1

        # num1, num2 = reversed(num1), reversed(num2)  # this wrong, why?
        num1, num2 = num1[::-1], num2[::-1]
        num = [0] * (N + M)
        for i, m in enumerate(num1):
            for j, n in enumerate(num2):
                num[i + j] += int(n) * int(m)

        for i, d in enumerate(num):
            if d >= 10:  # prevent i+1 overflow
                num[i + 1] += num[i] / 10
                num[i] %= 10

        # delete leading zeros
        num = num[::-1]
        non_zero_digit = 0
        while non_zero_digit < M + N and num[non_zero_digit] == 0:
            non_zero_digit += 1

        # deal with all zeros
        if non_zero_digit == M + N:
            return '0'
        return ''.join(map(str, num[non_zero_digit:]))


if __name__ == "__main__":
    num1 = '98'
    num2 = '9'
    print Solution().multiply2(num1, num2)

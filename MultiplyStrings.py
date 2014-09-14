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

if __name__ == "__main__":
    num1 = '99'
    num2 = '11'
    print Solution().multiply(num1, num2)

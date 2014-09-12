# 1, 11, 21, 1211, 111221, 312211


class Solution:
    # @return a string
    def countAndSay(self, n):
        num = [1]
        while n > 1:
            num = self.count(num)
            n -= 1
        strnum = ''.join(map(str, num))
        return strnum

    def count(self, num):
        out = list()
        if len(num) == 1:
            out = [1, 1]
        else:
            d = num[0]
            c = 1
            for x in range(1, len(num)):
                if num[x] == d:
                    c += 1
                else:
                    out.append(c)
                    out.append(d)
                    c = 1
                    d = num[x]
            out.append(c)
            out.append(d)

        return out

if __name__ == "__main__":
    print Solution().countAndSay(3)

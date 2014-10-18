class Solution:
    # @return a string
    def countAndSay(self, n):
        """Sequence of
        1, 11, 21, 1211, 111221, 312211, ...
        """
        def count(numbers):
            out = list()

            if len(num) == 1:
                return [1, 1]

            count = 1
            digit = numbers[0]
            for i in range(1, len(numbers)):
                if numbers[i] == digit:  # how about equal in the end?
                    count += 1
                else:
                    out.append(count)
                    out.append(digit)
                    count = 1
                    digit = numbers[i]

            out.append(count)
            out.append(digit)
            return out

        if n < 1:
            return None
        if n == 1:
            return '1'

        num = [1]
        while n > 1:
            num = count(num)
            n -= 1
        return ''.join(map(str, num))

if __name__ == "__main__":
    print Solution().countAndSay(4)

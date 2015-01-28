class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        P = [[0] * (y + 1) for y in range(numRows)]
        for y in range(len(P)):
            for x in range(len(P[y])):
                if x == 0 or x == y:
                    P[y][x] = 1
                    continue
                P[y][x] = P[y - 1][x] + P[y - 1][x - 1]
        return P

if __name__ == "__main__":
    print Solution().generate(4)

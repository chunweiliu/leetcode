class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if matrix == []:
            return 0

        maxy = -1
        miny = len(matrix)
        maxx = -1
        minx = len(matrix[0])
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == "1":
                    if maxy < y:
                        maxy = y
                    if miny > y:
                        miny = y
                    if maxx < x:
                        maxx = x
                    if minx > x:
                        minx = x
        if maxy == -1:
            area = 0
        else:
            area = (maxy - miny + 1) * (maxx - minx + 1)
        return area


if __name__ == "__main__":
    matrix = ["01",
              "10"]
    print Solution().maximalRectangle(matrix)

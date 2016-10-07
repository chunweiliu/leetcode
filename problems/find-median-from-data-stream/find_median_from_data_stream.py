from heapq import *


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.large = []  # Min-heap
        self.small = []  # Max-heap with negative elements

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        # O(log n)
        if len(self.large) == len(self.small):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.large) == len(self.small):
            return (self.large[0] - self.small[0]) * 0.5
        return self.large[0]

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()

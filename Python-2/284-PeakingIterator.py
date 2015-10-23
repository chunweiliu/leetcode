# Below is the interface for Iterator, which is already defined for you.
class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.index = 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.index < len(self.nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        to_return = self.nums[self.index]
        self.index += 1
        return to_return


class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peeking_element = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing
        the iterator.
        :rtype: int
        """
        if not self.peeking_element:
            self.peeking_element = self.iterator.next()
        return self.peeking_element

    def next(self):
        """
        :rtype: int
        """
        if self.peeking_element:
            to_return = self.peeking_element
            self.peeking_element = None
            return to_return
        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peeking_element:
            return True
        return self.iterator.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

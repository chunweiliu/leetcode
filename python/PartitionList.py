# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        """Partition list into 3 parts and relink them
        Time: O(n)
        Space: O(1)
        """
        if not head:
            return None

        small = small_head = ListNode(0)
        large = large_head = ListNode(0)
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next
        large.next = None  # not always true, need to set it up
        small.next = large_head.next
        return small_head.next

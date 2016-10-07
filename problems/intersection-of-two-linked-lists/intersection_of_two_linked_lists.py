# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution(object):
    def getIntersectionNode(self, head1, head2):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        c1 = self.count(head1)
        c2 = self.count(head2)
        if c1 > c2:
            head1 = self.advance(head1, c1 - c2)  # [BUG]
        else:
            head2 = self.advance(head2, c2 - c1)

        while head1 and head2:
            if head1 is head2:
                return head1
            head1 = head1.next
            head2 = head2.next
        return None

    def count(self, head):
        c = 0
        while head:
            head = head.next
            c += 1
        return c

    def advance(self, head, d):
        while head and d:
            head = head.next
            d -= 1
        return head  # [BUG] N/A

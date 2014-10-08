# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        """End advance front with n nodes
        Time: O(#node)
        Space: O(1)
        Conner cases: n = 0, 1
        """
        if n == 0:
            return head

        # Need dummy for special case
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        front = end = head

        # advance end
        while n > 0:
            end = end.next
            n -= 1

        # advance both
        while end:
            prev = front
            front = front.next
            end = end.next

        # remove front
        prev.next = front.next
        front.next = None

        return dummy.next

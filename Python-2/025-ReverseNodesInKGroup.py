# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k <= 1:
            return head

        # Check if the list is long enough to be reversed
        curr, n = head, 0
        while curr and n < k:
            curr = curr.next
            n += 1
        if n < k:
            return head

        # Set the label
        dummy = ListNode(0)
        dummy.next = head

        # ^-----------v
        # 0     1<----2      3
        #       v------------^
        # prev, last, curr
        prev = dummy
        last = prev.next
        curr = last.next

        # Reverse k - 1 pairs
        for _ in range(k - 1):
            last.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = last.next

        last.next = self.reverseKGroup(last.next, k)
        return dummy.next

    def reverse_k_group_alternatively(self, head, k, advance=False):
        if not head or k <= 1:
            return head

        # Check length and record last if need to advance
        n = 0
        last, curr = None, head
        while curr and n < k:
            last = curr
            curr = curr.next
            n += 1
        if n < k:
            return head

        dummy = ListNode(0)
        dummy.next = head

        # Reverse k nodes
        if not advance:
            prev, last, curr = dummy, head, head.next
            for _ in range(k - 1):
                last.next = curr.next
                curr.next = prev.next
                prev.next = curr
                curr = last.next

        last.next = self.reverse_k_group_alternatively(
            last.next, k, not advance)
        return dummy.next

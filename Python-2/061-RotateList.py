# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        # Figure out the lenght of the list first
        curr, n = head, 0
        while curr:
            curr = curr.next
            n += 1
        k %= n

        if k == 0:
            return head

        # Assume 0 < k < length of the list
        prev_fast = ListNode(0)
        prev_fast.next = head
        fast = head
        for _ in range(k):
            prev_fast = fast
            fast = fast.next

        # Advance both cursers
        prev_slow = ListNode(0)
        prev_slow.next = head
        slow = head
        while fast:
            prev_slow = slow
            slow = slow.next
            prev_fast = fast
            fast = fast.next
        prev_fast.next = head
        prev_slow.next = None

        return slow

if __name__ == '__main__':
    # head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = ListNode(1)
    k = 1
    rotated_head = Solution().rotateRight(head, k)
    while rotated_head:
        print rotated_head.val,
        rotated_head = rotated_head.next

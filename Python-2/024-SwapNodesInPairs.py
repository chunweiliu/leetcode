# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution(object):
    def swapPairs(self, head):
        if not (head and head.next):
            return head
        new_head = head.next
        head.next = self.swapPairs(head.next.next)
        new_head.next = head
        return new_head

    def swapPairs0(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # previous -> a -> b -> b.next
        # previous -> b -> a -> b.next
        previous, previous.next = ListNode(0), head
        dummy = previous
        while previous.next and previous.next.next:
            a = previous.next
            b = previous.next.next
            previous.next = b
            a.next = b.next
            b.next = a
            # Use a swap statement can do these all without the ordering issue
            # previous.next, b.next, a.next = b, a, b.next
            previous = a
        return dummy.next

if __name__ == '__main__':
    l0 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    l = Solution().swapPairs(l0)
    while l:
        print l.val
        l = l.next

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left, right = ListNode(0), ListNode(0)
        head_l, head_r = left, right
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        right.next = None
        left.next = head_r.next if head_r.next else None
        return head_l.next


if __name__ == '__main__':
    head = ListNode(2, ListNode(1))
    x = 1
    head = Solution().partition(head, x)
    while head:
        print head.val,
        head = head.next

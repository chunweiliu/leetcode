# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = dummy = ListNode(-1)
        while l1 and l2:
            curr.next = l1 if l1.val < l2.val else l2
            curr = curr.next
            if l1.val < l2.val:
                l1 = l1.next
            else:
                l2 = l2.next
        curr.next = l1 if l1 else l2
        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(3, ListNode(5)))
    l2 = ListNode(2, ListNode(4, ListNode(6)))
    l = Solution().mergeTwoLists(l1, l2)
    while l:
        print l.val,
        l = l.next

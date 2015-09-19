# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = prev = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next  # Advance to the node that has different val.
                prev.next = head
            else:
                prev = prev.next
                head = head.next
        return dummy.next

if __name__ == '__main__':
    head = ListNode(1, ListNode(2))
    head = Solution().deleteDuplicates(head)
    while head:
        print head.val,
        head = head.next

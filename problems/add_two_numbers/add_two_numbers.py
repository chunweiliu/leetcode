# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(-1)
        curr = head
        carry = 0
        while l1 or l2 or carry:
            current_sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            curr.next = ListNode(current_sum % 10)
            carry = current_sum / 10

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next

if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(9, ListNode(9))
    l = Solution().addTwoNumbers(l1, l2)
    while l:
        print l.val,
        l = l.next

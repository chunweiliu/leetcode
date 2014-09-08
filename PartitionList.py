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
        if head is None:
            return head

        les_tail = ListNode(0)  # key
        lrg_tail = ListNode(0)

        # store the heads of linked lists (no difference)
        les_head = les_tail
        lrg_head = lrg_tail

        while head is not None:
            if head.val < x:
                les_tail.next = ListNode(head.val)  # key
                les_tail = les_tail.next
            else:
                lrg_tail.next = ListNode(head.val)
                lrg_tail = lrg_tail.next
            head = head.next
        lrg_tail.next = None  # key
        les_tail.next = lrg_head.next
        return les_head.next

    def print_list(self, head):
        if head.next is not None:
            print head.val
            self.print_list(head.next)
        else:
            print head.val


if __name__ == "__main__":
    # a = ListNode(1)
    # a.next = ListNode(4)
    # a.next.next = ListNode(3)
    # a.next.next.next = ListNode(2)
    # a.next.next.next.next = ListNode(5)
    # a.next.next.next.next.next = ListNode(2)
    a = ListNode(2)
    a.next = ListNode(1)
    x = 2
    Solution().print_list(a)
    print "+++"
    b = Solution().partition(a, x)
    Solution().print_list(b)

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
        # Check if the list need to be reversed.
        if not head or k <= 1:
            return head

        # Check if the list is long enough to be reversed.
        curr, n = head, 0
        while curr and n < k:
            curr = curr.next
            n += 1
        if n < k:
            return head

        # Reverse the first k nodes (k and the lenght of list are at least 2)
        # ^---------v
        # 0    1 <- 2    3
        #      v---------^
        # prev last curr
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        last = prev.next
        curr = last.next

        n = 0
        while last and n < k - 1:  # k - 1, two nodes only need one reverse.
            last.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = last.next
            n += 1

        # Recursively do for the next group.
        last.next = self.reverseKGroup(last.next, k)
        return dummy.next

if __name__ == '__main__':
    # head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = ListNode(1, ListNode(2, ListNode(3)))
    k = 3
    reversed_head = Solution().reverseKGroup(head, k)
    while reversed_head:
        print reversed_head.val
        reversed_head = reversed_head.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        m = 1
        n = k
        not_reverse = k
        last = head
        while last and not_reverse:
            last = last.next
            not_reverse -= 1
            if not_reverse:
                pass
            else:
                head = self.reverseBetween(head, m, n)  # must be head
                not_reverse = k
                m += k
                n += k
        return head

    def reverseBetween(self, head, m, n):
        # 0 -> 1 -> 2 -> 3 -> 4 -> 5
        # prev m         n
        # 0 -> 3 -> 2 -> 1 -> 4 -> 5
        #                last
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head
        step = 0
        while step < m - 1:
            prev = curr
            curr = curr.next
            step += 1

        last = prev.next  # last must be the first node after prev
        while step < n - 1:
            # do reverse
            curr = last.next
            last.next = curr.next
            curr.next = prev.next
            prev.next = curr
            step += 1
        return dummy.next

    def reverse(self, head):
        # 1 -> 2 -> 3 -> 4
        # 4 -> 3 -> 2 -> 1
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    # head = ListNode(1, ListNode(2))
    # head = Solution().reverse(head)
    head = Solution().reverseKGroup(head, 2)
    #head = Solution().reverseBetween(head, 1, 5)
    while head:
        print head.val
        head = head.next

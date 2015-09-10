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
        # Check if we need to reverse by advancing the tail k-times.
        # 1 -> 2 -> 3 -> 4 -> 5, k = 3
        # head           tail
        # 1 -> 2 -> 3 -> None, k = 3 (conner case)
        # head           tail
        tail = head
        count = 0
        while count < k:
            if tail:
                tail = tail.next
            else:
                break
            count += 1
        if count != k:
            return head

        # Reverse the k nodes in the front.
        # None 1 -> 2 -> 3 -> 4 -> 5, before loop
        # prev curr
        # None<1    2 -> 3 -> 4 -> 5, after _ = 0
        #      prev curr next
        # None<1 <- 2 -> 3 -> 4 -> 5, after _ = 1
        #           prev curr next
        # None<1 <- 2 <- 3    4 -> 5, after _ = 2
        #                prev curr next
        previous_node, current_node = None, head
        for _ in range(k):
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        # Connect this k-group to the next.
        # v----1 <- 2 <- 3    4 -> 5
        # --------------------^
        head.next = self.reverseKGroup(tail, k) if tail else None

        return previous_node


if __name__ == '__main__':
    # head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = ListNode(1, ListNode(2, ListNode(3)))
    k = 3
    reversed_head = Solution().reverseKGroup(head, k)
    while reversed_head:
        print reversed_head.val
        reversed_head = reversed_head.next

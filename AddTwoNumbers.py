# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
            """Advance l1 and l2 together, aware carry
            Time: O(n)
            Space: O(1)
            Corner: empty list, carry > 0
            """
            curr1, curr2 = l1, l2
            curr = dummy = ListNode(0)
            num = 0
            while curr1 or curr2:
                num /= 10  # as carry
                if curr1:
                    num += curr1.val
                    curr1 = curr1.next
                if curr2:
                    num += curr2.val
                    curr2 = curr2.next
                curr.next = ListNode(num % 10)
                curr = curr.next

            if num / 10 == 1:  # max
                curr.next = ListNode(1)
            return dummy.next

if __name__ == "__main__":
    l1 = ListNode(9, ListNode(9, ListNode(9)))
    l2 = ListNode(1)
    l = Solution().addTwoNumbers(l1, l2)
    while l:
        print l.val
        l = l.next

import unittest


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        # 1 -> 2 -> 3 -> 4 -> 5, m = 2, n = 4
        # prev
        prev = dummy
        for _ in range(m - 1):
            prev = prev.next

        # ^---------v
        # 1    2 <- 3    4 -> 5
        #      v---------^
        # prev last curr
        last = prev.next
        curr = last.next
        for _ in range(n - m):
            last.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = last.next
        return dummy.next


class TestCase(unittest.TestCase):
    def test_case1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        expected = ListNode(1, ListNode(4, ListNode(3,
                            ListNode(2, ListNode(5)))))
        m, n = 2, 4
        solution = Solution().reverseBetween(head, m, n)

        result = True
        while solution:
            result &= solution.val == expected.val
            solution = solution.next
            expected = expected.next
        self.assertTrue(result, True)

    def test_case2(self):
        head = ListNode(1)
        expected = ListNode(1)

        m, n = 1, 1
        solution = Solution().reverseBetween(head, m, n)
        result = True
        while solution:
            result &= solution.val == expected.val
            solution = solution.next
            expected = expected.next
        self.assertTrue(result, True)

if __name__ == '__main__':
    unittest.main()

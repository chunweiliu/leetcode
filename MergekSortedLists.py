# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        import heapq
        heap = []
        for x in lists:
            if x is not None:
                heap.append((x.val, x))  # tuple for heap key
        heapq.heapify(heap)

        head = ListNode(0)
        curr = head
        while len(heap) > 1:
            # move the current node
            min_node = heap[0][1]
            curr.next = min_node
            curr = curr.next
            # update the heap
            if min_node.next:
                heapq.heappushpop(heap, (min_node.next.val, min_node.next))
            else:
                heapq.heappop(heap)
        if heap:
            curr.next = heap[0][1]
        return head.next

if __name__ == "__main__":
    lists = [ListNode(5, ListNode(6)), ListNode(4), ListNode(2, ListNode(3))]
    #lists = [[]]
    head = Solution().mergeKLists(lists)
    while head:
        print head.val
        head = head.next

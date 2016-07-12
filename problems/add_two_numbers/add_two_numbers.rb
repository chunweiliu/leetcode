# Definition for singly-linked list.
class ListNode
  attr_accessor :val, :next
  def initialize(val)
      @val = val
      @next = nil
  end
end

# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
  dummy = ListNode.new(nil)
  current = dummy
  carry = 0
  while l1 || l2 || carry != 0
    sum = carry + (l1 ? l1.val : 0) + (l2 ? l2.val : 0)
    current.next = ListNode.new(sum % 10)
    carry = sum / 10

    current = current.next
    l1 = l1 ? l1.next : nil
    l2 = l2 ? l2.next : nil
  end
  dummy.next
end

def print_list(l)
  while l
    p l.val
    l = l.next
  end
end
l1 = ListNode.new(10)
l2 = ListNode.new(9)
print_list(add_two_numbers(l1, l2))

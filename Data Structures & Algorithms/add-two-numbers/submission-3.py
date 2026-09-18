# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        cur = dummy

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            digit = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10

            cur.next = ListNode(digit)
            
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry == 1:
            cur.next = ListNode(1)

        return dummy.next
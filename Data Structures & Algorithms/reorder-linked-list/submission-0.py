# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        step = 0

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev, cur = None, slow.next
        slow.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        l1, l2 = head, prev

        while l2:
            l1_next, l2_next = l1.next, l2.next
            l1.next = l2
            l2.next = l1_next
            l1, l2 = l1_next, l2_next

        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur0 = dummy

        cur1 = list1
        cur2 = list2

        while cur1 and cur2:
            if cur1.val > cur2.val:
                cur0.next = cur2
                cur0 = cur0.next
                cur2 = cur2.next
            else:
                cur0.next = cur1
                cur0 = cur0.next
                cur1 = cur1.next
        
        while cur1:
            cur0.next = cur1
            cur1 = cur1.next
            cur0 = cur0.next

        while cur2:
            cur0.next = cur2
            cur2 = cur2.next
            cur0 = cur0.next

        return dummy.next




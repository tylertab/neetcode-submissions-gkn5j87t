# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode(1,None)
        point = res
        carry = 0
        while l1 or l2:
            val = 0
            if l1:
                val += l1.val
            if l2:
                val += l2.val
            val += carry
            carry = 0
            carry = val // 10
            valc = val % 10
            point.next = ListNode(valc,None)
            print(point.val)
            point = point.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            point.next = ListNode(carry,None)
        return res.next

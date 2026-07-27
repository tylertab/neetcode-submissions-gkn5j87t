# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ahead = head
        for i in range(n):
            ahead = ahead.next
        prev = None
        curr = head
        while ahead is not None:
            ahead = ahead.next
            prev = curr
            curr = curr.next
        if prev is None:
            head = head.next
        elif prev.next is not None:
            prev.next = prev.next.next
        
        return head
        
            
        
        


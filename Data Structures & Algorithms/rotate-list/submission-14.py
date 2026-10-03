# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        if head.next == None:
            return head
        if k == 0:
            return head

        last = head
        #last index
        count = 1
        while last.next != None:
            count += 1
            last = last.next
        k = k % count
        if k == 0:
            return head
        #make cycle last -> head
        last.next = head
        #get curr k forward from head
        curr = head
        for _ in range(k):
            curr = curr.next
        #get newhead to k from head
        newhead = head
        prev = None
        while curr != head: 
            prev = newhead
            newhead = newhead.next
            curr = curr.next
        prev.next = None

        
        return newhead


        
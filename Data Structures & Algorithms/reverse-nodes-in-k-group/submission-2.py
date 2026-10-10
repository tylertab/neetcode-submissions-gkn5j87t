# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        newhead = ListNode(None)
        newtail = newhead
        def reverse(head):
            prev = None
            last = head
            count = 0
            while head != None and count != k:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
                count += 1
            
            return prev, last

        curr = head

        def move_k(ahead):
            for _ in range(k):
                if ahead == None:
                    return -1
                ahead = ahead.next
            return ahead
        
        while curr != None:
            ahead = move_k(curr)
            if ahead != -1:
                rhead, rend = reverse(curr)
                newtail.next = rhead
                newtail = rend
                curr = ahead
            else:
                newtail.next = curr
                break
        return newhead.next
                

            




         

        

           


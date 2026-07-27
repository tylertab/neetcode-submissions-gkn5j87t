# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def pri(head):
            ans = []
            while head != None:
                ans.append(head.val)
                head = head.next
            print(ans)
        
        
        mid = head
        end = head.next
        #get midpoint
        while end is not None and end.next is not None:
            mid = mid.next
            end = end.next.next
        print(f'mp val: {mid.val}')
        #reverse second half
        prev = None
        curr = mid
        while curr is not None:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
        
        rev = prev
        curr = head
        while curr is not None and curr != rev:
            #save rev head, move rev to next
            back = rev
            if rev.next:
                rev =  rev.next 
    
            back.next = curr.next
            curr.next = back

            curr = back.next
        return None


        
        


        
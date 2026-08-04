# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        prev = ListNode(None,None)
        head = prev
        k = len(lists)

        if k == 0:
            return prev.next
        
        i = 0
        while len(lists) > 0:
            m = sys.maxsize
            li = 0
            for i in range(len(lists)):
                l = lists[i]
                if l is None:
                    continue
                if l.val < m:
                    li = i
                    m = l.val
            t = lists[li]
            if t is None:
                break
            lists[li] = t.next
            t.next = None
            prev.next = t
            prev = prev.next

        return head.next
            

                
                
                



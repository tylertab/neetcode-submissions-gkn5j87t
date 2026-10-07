# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sortedHead = None
        while head != None:
            n = head.next
            head.next = None
            if sortedHead == None:
                sortedHead = head
            else:
                prev = None
                curr = sortedHead
                while curr != None and curr.val < head.val:
                    prev = curr
                    curr = curr.next
                if prev == None:
                    head.next = sortedHead
                    sortedHead = head
                else:
                    t = prev.next
                    prev.next = head
                    head.next = t   
            head = n
        return sortedHead
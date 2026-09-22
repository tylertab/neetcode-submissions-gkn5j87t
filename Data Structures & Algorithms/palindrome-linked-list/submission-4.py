# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def getmid(head):
            one,two = head, head

            while two != None and two.next != None:
                one = one.next
                two = two.next.next
            return one, two == None
        
        mid, even = getmid(head)

        def reverseuptomid(head,mid):
            prev = None

            while head != mid:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
              
            return prev
        r = reverseuptomid(head, mid)

        if r == None:
            return True

        if not even:
            mid = mid.next
        
        while r != None or mid != None:
            if r == None:
                return False
            if mid == None:
                return False
            if mid.val != r.val:
                return False
            mid = mid.next
            r = r.next
        return True


        
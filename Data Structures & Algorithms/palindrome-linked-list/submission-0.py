# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def palindrome(it):
            start = 0
            end = len(it) - 1
            while start <= end:
                if it[start] != it[end]:
                    return False
                start +=1
                end -=1
            return True
        l = []
        while head != None:
            l.append(head.val)
            head = head.next
        return palindrome(l)
        
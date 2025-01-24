# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tem=head
        a=[]
        while tem!=None:
            a.append(tem.val)
            tem=tem.next
        r=a[::-1]
        return a==r

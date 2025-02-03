# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=head
        b=[]
        while a!=None:
            b.append(a.val)
            a=a.next
        
        b.sort()
        a=head
        for i in range(len(b)):
            a.val=b[i]
            a=a.next
        return head
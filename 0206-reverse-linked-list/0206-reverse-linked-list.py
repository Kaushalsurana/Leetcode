# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        temp=head
        while temp != None:
            l.append(temp.val)
            temp=temp.next
        l=l[::-1]
        temp=head
        for i in range (len(l)):
            temp.val=l[i]
            temp=temp.next
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=head
        b=head
        s=0
        while b.next:
            if b.val==0 and b !=head:
                s+=b.val
                a.val=s
                a=a.next
                s=0
            s+=b.val
            b=b.next
        a.val=s
        a.next=None
        return head
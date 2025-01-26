# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        od=head
        ev=head.next
        a=ev
        while ev and ev.next:
            od.next=ev.next
            od=od.next
            ev.next=od.next
            ev=ev.next
        od.next=a
        return head
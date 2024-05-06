# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = []
        c = head

        while c:
            while s and s[-1].val < c.val:
                s.pop()
            
            s.append(c)
            c = c.next

        d = ListNode(0)
        p = d

        for n in s:
            p.next = n
            p = p.next

        p.next = None

        return d.next

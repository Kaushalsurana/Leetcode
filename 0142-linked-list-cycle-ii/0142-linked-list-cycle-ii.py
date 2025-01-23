# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        curr=head
        while curr!=None:
            if curr in a:
                return curr
            a.append(curr)
            curr=curr.next
        return None
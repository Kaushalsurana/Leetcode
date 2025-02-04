# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a=set()
        while headA:
            if headA not in a:
                a.add(headA)
            headA=headA.next
        while headB:
            if headB in a:
                return headB
            headB=headB.next
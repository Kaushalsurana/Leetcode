# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r = head
        if head.val >= 5:
            r = ListNode(1, head)
        while head:
            head.val = head.val * 2 % 10
            if head.next and head.next.val >= 5:
                head.val += 1
            head = head.next
        return r
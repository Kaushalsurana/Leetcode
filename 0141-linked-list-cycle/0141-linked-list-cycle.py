# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a=set()
        ran=head
        while ran.next!=None:
            a.add(ran)
            if ran in a:
                return True
            ran=ran.next
        return False

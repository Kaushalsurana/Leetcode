# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        count=1
        while curr.next!=None:
            count+=1
            curr=curr.next
        curr=head
        h=count//2 +1
        for i in range(h-1):
            curr=curr.next
        return curr
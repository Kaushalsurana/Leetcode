# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp=list1
        temp2=list1
        for i in range(a-1):
            temp=temp.next
        for i in range(b+1):
            temp2=temp2.next
        temp.next=list2
        while(temp.next!=None):
            temp=temp.next
        temp.next=temp2
        return list1
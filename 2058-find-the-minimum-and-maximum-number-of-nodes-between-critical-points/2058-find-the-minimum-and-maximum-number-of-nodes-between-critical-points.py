# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return []

        dists = []
        cur = head
        prev = None
        idx = 1

        while cur and cur.next:
            if cur.val < cur.next.val:
                if prev and prev.val > cur.val:
                    dists.append(idx)
            if cur.val > cur.next.val:
                if prev and prev.val < cur.val:
                    dists.append(idx)
            prev = cur
            cur = cur.next
            idx += 1
        # print(dists)
        if len(dists) < 2 or not dists:
            return [-1, -1]
        minDist = float("inf")

        for i in range(1, len(dists)):
            minDist = min(minDist, dists[i] - dists[i - 1])
        return [minDist, dists[-1] - dists[0]]
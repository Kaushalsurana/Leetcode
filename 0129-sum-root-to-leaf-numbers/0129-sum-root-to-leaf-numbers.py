# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nsum = 0
        if not root: return nsum
        l = [(str(root.val), root)]
        while l: 
            s, n = l.pop() 
            if not n.left and not n.right:
                nsum += int(s); continue
            if n.right:
                l.append((s+str(n.right.val), n.right))
            if n.left:
                l.append((s+str(n.left.val), n.left))
        return nsum
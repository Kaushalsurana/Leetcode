# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = [0]
        def k(node):
            if not node:
                return 
            if node.right:
                k(node.right)
            s[0]+=node.val
            node.val=s[0]
            if node.left:
                k(node.left)
        k(root)
        return root
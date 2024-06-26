# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        def build(l,h,arr):
            if l>h:
                return None
            m=(l+h)//2
            r=TreeNode(arr[m])
            r.left=build(l,m-1,arr)
            r.right=build(m+1,h,arr)
            return r
        arr=[]
        inorder(root)
        low = 0
        high = len(arr)-1
        root = build(low,high,arr)
        return root
    
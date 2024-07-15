# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        a={}
        b=set()
        for pa,ch,le in descriptions:
            b.add(ch)
            if pa not in a:
                a[pa]=TreeNode(pa)
            if ch not in a:
                a[ch]=TreeNode(ch)
            if le:
                a[pa].left=a[ch]
            else:
                a[pa].right=a[ch]
        for pa,ch,le in descriptions:
            if pa not in b:
                return a[pa]
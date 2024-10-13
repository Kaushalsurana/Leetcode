# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        arr=[]
        def ord(node):
            if not node:
                return True,0
            b,c=ord(node.left)
            d,e=ord(node.right)
            if b and d and c==e:
                si=1+c+e
                arr.append(si)
                return True,si
            else:
                return False,0
        ord(root)
        arr.sort(reverse=True)
        if len(arr)>=k:
            return arr[k-1]
        else:
            return -1
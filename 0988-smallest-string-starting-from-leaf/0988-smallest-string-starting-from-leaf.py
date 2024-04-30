# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        strings = []

        def recursion(node, string):
            if not node: return  ''

            if not node.left and not node.right:
                string = string + chr(ord('a') + node.val)
                strings.append(string[::-1])
                return
            
            recursion(node.left, string + chr(ord('a') + node.val))
            recursion(node.right, string + chr(ord('a') + node.val))
        
        recursion(root, '')

        strings.sort()
        
        return strings[0]
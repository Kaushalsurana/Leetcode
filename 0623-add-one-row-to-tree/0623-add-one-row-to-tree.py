# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # DFS function
        def dfs(root, index, val, depth):
            if not root:
                return
            if index == depth-1:
                new_left = TreeNode(val)
                new_left.left = root.left
                root.left = new_left
                
                new_right = TreeNode(val)
                new_right.right = root.right
                root.right = new_right
 
            elif index < depth-1:
                dfs(root.left, index + 1, val, depth)
                dfs(root.right, index + 1, val, depth)
 
        if depth==1:
             return TreeNode(val, root)
        else:
            dfs(root, 1, val, depth)
            return root
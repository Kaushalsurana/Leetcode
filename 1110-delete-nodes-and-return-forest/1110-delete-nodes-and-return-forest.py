# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        a=[]
        def ab(root):
            if root is None:
                return None
            root.left=ab(root.left)
            root.right=ab(root.right)
            if root.val in to_delete:
                if root.right is None and root.left is None:
                    return None
                else:
                    if root.left:
                        a.append(root.left)
                    if root.right:
                        a.append(root.right)
                    return None
            return root

        to_delete=set(to_delete)
        node=ab(root)
        if node:
            a.append(node)
        return a
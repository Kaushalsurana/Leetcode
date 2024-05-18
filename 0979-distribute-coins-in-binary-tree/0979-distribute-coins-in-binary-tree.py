class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.total_moves = 0

        def balance(node):
            if not node:
                return 0
            left_balance = balance(node.left)
            right_balance = balance(node.right)
            self.total_moves += abs(left_balance) + abs(right_balance)
            return node.val + left_balance + right_balance - 1

        balance(root)
        return self.total_moves
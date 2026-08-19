# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dfs(r, pr):
            if r == None:
                return 0
            if (r, pr) in memo:
                return memo[r, pr]
            left = dfs(r.left, False)
            right = dfs(r.right, False)
            if pr:
                #memo[(r, False)] = left + right
                return left + right
            op2 = left + right
            left = dfs(r.left, True)
            right = dfs(r.right, True)
            op1 = left + right + r.val
            memo[(r, False)] = max(op2, op1)
            return max(op2, op1)

            
        return dfs(root,False)

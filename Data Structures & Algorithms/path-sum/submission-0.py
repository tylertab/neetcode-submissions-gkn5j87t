# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(r, val):
            if r is None:
                return False
            
            isleaf = r.right == None and r.left == None;

            if isleaf and  val + r.val == targetSum:
                return True

            left = dfs(r.left, val + r.val)
            right = dfs(r.right, val + r.val)

            return  left or right
        return dfs(root, 0)
        

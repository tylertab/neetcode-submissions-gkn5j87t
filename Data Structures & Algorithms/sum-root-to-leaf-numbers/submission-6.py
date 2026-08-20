# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        isleaf = lambda x: x.left == None and x.right == None
        res = [0]
        currnums = [0]


        if root == None:
            return 0
        def dfs(root):
            if isleaf(root):
                currnums[0] = (currnums[0] * 10) + root.val
                res[0] +=   currnums[0]
                currnums[0] = (currnums[0] // 10)
                return
            else:
                currnums[0] = (currnums[0] * 10) + root.val
                if root.left:
                    dfs(root.left)
                if root.right:
                    dfs(root.right)
                currnums[0] = (currnums[0] // 10)
                return
        dfs(root)

        return res[0]
        
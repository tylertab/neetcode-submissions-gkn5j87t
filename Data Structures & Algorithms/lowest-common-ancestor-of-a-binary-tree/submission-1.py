# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = []
        path2 = []
        def dfs(root, target, path):
            if root == None:
                return False
            path.append(root)
            if root == target:
                return True
            if not dfs(root.left,target,path) and not dfs(root.right,target,path):

                path.pop(-1)
                return False
            return True
        
        dfs(root,p,path1)
        dfs(root,q,path2)
        lcs = None
        for i in range(min(len(path1),len(path2))):
            if path1[i] != path2[i]:
                break
            lcs = path1[i]
        return lcs
            






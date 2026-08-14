# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(r):
            if r == None:
                return 
            inorder(r.left)
            res.append(r.val)
            inorder(r.right)
        inorder(root)
        return res
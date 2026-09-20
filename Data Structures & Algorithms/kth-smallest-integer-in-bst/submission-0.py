# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ka = [0]
        ans = []
        def inorder(root,k):
            if root == None:
                return
            inorder(root.left,k)
            ans.append(root.val)
            inorder(root.right,k)
            

        inorder(root,k)
        print(ans)
        return ans[k - 1]
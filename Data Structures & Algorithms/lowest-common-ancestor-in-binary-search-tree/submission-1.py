# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def buildpath(root, search):
            if root == None:
                return []
            else:
                if root == search:
                    return [root]
                elif root.val > search.val:
                    return [root] + buildpath(root.left,search)
                else:
                    return [root] + buildpath(root.right,search)
        
        qpath = buildpath(root, q)
        ppath = buildpath(root, p)

        index = min(len(qpath),len(ppath)) - 1

        while qpath[index] != ppath[index]:
            index -= 1
        return qpath[index]
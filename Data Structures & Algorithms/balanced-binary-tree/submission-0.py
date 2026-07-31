# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        mp = {None:0}
        if root is None:
            return True
        stack = [root]

        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:

                node = stack.pop()

                l = mp[node.left]
                r = mp[node.right]
                
                if l-r not in [0,1,-1]:
                    return False
                
                mp[node] = max(l,r) + 1

        return True


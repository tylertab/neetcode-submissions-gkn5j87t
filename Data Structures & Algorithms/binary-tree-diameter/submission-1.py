# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mp = {None:(0,0)} #node -> (h, d)
        stack = [root]
        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()

                leftHeight, leftDiameter = mp[node.left]
                rightHeight,rightDiameter = mp[node.right]

                mp[node] = (max(leftHeight, rightHeight) + 1, max(leftHeight + rightHeight, leftDiameter, rightDiameter))

            
        return mp[root][1]
        
       
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    
    def _find_subroot(self, root, subroot, roots):
        if root == None:
            return
        if root.val == subroot.val:
            roots.append(root)
        checkleft = self._find_subroot(root.left, subRoot,roots)
        checkright = self._find_subroot(root.right, subRoot,roots)

        
    def _same_tree(self, root, subroot):
        if root == None and subroot == None:
            return True
        if root == None or subroot == None:
            return False
        if root.val != subroot.val:
            return False
            
        return self._same_tree(root.left,subroot.left) and self._same_tree(root.right,subroot.right)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        roots = []
        self._find_subroot(root, subRoot, roots)
        if roots == []:
            return False
        for root in roots:
            if self._same_tree(root, subRoot):
                return True
        return False
        

        
            
            
            

        
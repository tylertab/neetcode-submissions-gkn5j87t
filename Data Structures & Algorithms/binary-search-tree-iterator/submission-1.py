# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    #inorder
    #if root == None:
    #    return
    #inorder(left)
    #print(root)
    #inorder(right)

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pointer = root

    def next(self) -> int:
        root = self.pointer
        if root == None:
            return None
        while root.left:
            self.stack.append(root)
            root = root.left
        nextNode = root
        if nextNode.right:
            self.pointer = nextNode.right
        else:
            if len(self.stack) > 0:
                self.pointer = self.stack.pop(-1)
                self.pointer.left = None
            else:
                self.pointer = None

        return nextNode.val

        

    

        

    def hasNext(self) -> bool:
        return self.pointer != None or len(self.stack) > 0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
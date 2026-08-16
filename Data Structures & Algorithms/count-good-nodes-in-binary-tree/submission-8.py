# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        heap = []
        count = [0]
        def dfs(r):
            if r is None:
                return
            pushed = False

            if len(heap) == 0 or -heap[0] <= r.val:
                count[0] += 1
                heapq.heappush(heap,-r.val)
                pushed = True
            dfs(r.left)
            dfs(r.right)
            if pushed:
                heapq.heappop(heap)

        dfs(root)
        return count[0]

            
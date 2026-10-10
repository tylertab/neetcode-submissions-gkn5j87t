class DS:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
    
    def _find(self,a):
        if a == self.parent[a]:
            return a
        return self._find(self.parent[a])
    def union(self, a ,b):
        rank = self.rank
        parent = self.parent
        parent_a = self._find(a)
        parent_b = self._find(b)

        if parent_a == parent_b:
            return False
        
        if rank[parent_a] > rank[parent_b]:
            parent[parent_b] = parent_a
        elif rank[parent_b] > rank[parent_a]:
            parent[parent_a] = parent_b
        else:
            parent[parent_b] = parent_a
            rank[parent_a] += 1
        return True

        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        vertices = set()
        for (u,v) in edges:
            vertices.add(u)
            vertices.add(v)
        ds = DS(len(vertices))
        notneeded = []
        for (u,v) in edges:
            if not ds.union(u,v):
                notneeded.append([u,v])

        return notneeded[-1] 














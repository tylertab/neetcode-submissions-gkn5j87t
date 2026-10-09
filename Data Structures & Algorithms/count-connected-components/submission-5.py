class DS:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [0] * n
        self.num_sets = n
    def _find_parent(self,a):
        if self.parent[a] == a:
            return a
        return self._find_parent(self.parent[a])
    
    def union(self,a, b):
        a_parent = self._find_parent(a)
        b_parent = self._find_parent(b)

        if a_parent == b_parent:
            return False

        if self.rank[a_parent] < self.rank[b_parent]:
            self.parent[a_parent] = b_parent
        elif self.rank[a_parent] > self.rank[b_parent]:
            self.parent[b_parent] = a_parent
        else:
            self.parent[b_parent] = a_parent
            self.rank[a_parent] += 1
        self.num_sets -= 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ds = DS(n)

        for (a,b) in edges:
            ds.union(a,b)

        return ds.num_sets
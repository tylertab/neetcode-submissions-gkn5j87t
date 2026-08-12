class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #how do we know if it is a valide tree?
        #no cycles 
        #every node needs to be connected 
        #create adjecency list for each node
        #must have n - 1 edges
        if len(edges) != n - 1:
            return False
        
        #create adj list
        adj = {}
        for edge in edges:
            u, v = edge
            adj[u] = adj.get(u, []) + [v]
            adj[v] = adj.get(v, []) + [u]

        #visited set
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            for j in adj.get(i,[]):
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        dfs(0, -1)
        


        return len(visit) == n



class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #okay so first we want to create and adjacency list
        #then we start with the k node and do dijkstras algo which will give us the min distance to each node from k
        #Then we want to return the max distance found

        adj = {}

        def genadj():
            for i in range(len(times)):
                source, target, t = times[i]
                edge = (t, target)
                if source not in adj:
                    adj[source] = [edge]
                else:
                    adj[source].append(edge)
        genadj()

        dist = [None] * n
        heap = [(0, k)]
        visited = set()
        m = 0
        while len(heap) > 0:
            d, source = heapq.heappop(heap)
            if len(visited) == n:
                break
            if source in visited:
                continue
            else:
                visited.add(source)
            dist[source - 1] = d
            currdist = dist[source - 1]
            m = max(m, currdist)

            edges = adj.get(source, [])
            for edge in edges:
                heapq.heappush(heap,(currdist + edge[0], edge[1]))
            
        if len(visited) < n:
            return -1
        return m


            
        

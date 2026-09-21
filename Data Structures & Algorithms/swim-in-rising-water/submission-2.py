class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0],(0,0))]
        t = 0
        visited = set()
        while len(heap) > 0:
            elevation, point = heapq.heappop(heap)
            visited.add(point)
            while elevation > t:
                t += 1
            if point == (len(grid) - 1, len(grid) - 1):
                return t
            i = point[0]
            j = point[1]
            u,d,r,l = None,None,None,None
            if i > 0:
                u = (i-1,j)
            if i < len(grid) - 1:
                d = (i+1,j)
            if j > 0:
                l = (i,j - 1)
            if j < len(grid) - 1:
                r = (i,j + 1)
            for point in [u,d,r,l]:
                if point != None and point not in visited:
                    elevation = grid[point[0]][point[1]]
                    heapq.heappush(heap,(elevation,point))
            
            
            
            

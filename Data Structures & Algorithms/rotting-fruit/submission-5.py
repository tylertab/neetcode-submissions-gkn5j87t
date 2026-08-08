class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def pr(q, cord):
            i = cord[0]
            j = cord[1]
            if i in range(len(grid)) and j in range(len(grid[i])):
                if grid[i][j] == 1:
                    q.append(cord)
                    grid[i][j] = 2


        q = deque()
        totalcount = 0
        #append rotten to queue
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    totalcount += 1
                if grid[i][j] == 2:
                    q.append((i,j))


        visited = set()
        
        leastminutes = -1
        while len(q) > 0:
            currlength = len(q)
            for i in range(currlength):
                cur = q.popleft()
                if cur not in visited:
                    visited.add(cur)
                    pr(q,(cur[0] + 1, cur[1]))
                    pr(q,(cur[0] - 1, cur[1]))
                    pr(q,(cur[0], cur[1] + 1))
                    pr(q,(cur[0], cur[1] - 1))
            leastminutes += 1
        if len(visited) != totalcount:
            return -1
        return max(leastminutes, 0)
                

                

            

                
            
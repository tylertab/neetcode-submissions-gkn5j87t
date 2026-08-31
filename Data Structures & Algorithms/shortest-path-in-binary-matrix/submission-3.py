class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = [(0,0,1)]
        target = (len(grid) - 1, len(grid) - 1)
        vis = set()
        def addtoq(i, j, l):
            if i not in range(len(grid)) or j not in range(len(grid)):
                return
            if (i,j) in vis:
                return
            if grid[i][j] == 0:
                q.append((i,j,l))

        while len(q) != 0:
            n = len(q)
            while n != 0:
                i,j,l = q.pop(0)
                vis.add((i,j))
                if grid[i][j] != 0:
                    return -1
                if (i,j) == target:
                    return l

                addtoq(i-1,j-1, l +1)
                addtoq(i-1,j, l + 1)
                addtoq(i, j-1, l + 1)
                addtoq(i + 1, j, l + 1)
                addtoq(i, j + 1, l + 1)
                addtoq(i + 1, j + 1, l + 1)
                addtoq(i - 1, j + 1, l + 1)
                addtoq(i + 1, j - 1, l + 1)
        
                n -= 1

        return -1


            
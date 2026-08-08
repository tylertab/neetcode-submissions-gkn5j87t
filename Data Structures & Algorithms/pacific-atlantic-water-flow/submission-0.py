class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        canreachfrompacific = set()
        canreachfromatlantic = set()

        def dfs(i, j, prevheight, s):
            if i not in range(len(heights)):
                return
            if j not in range(len(heights[i])):
                return
            if (i,j) in s:
                return
            currheight = heights[i][j]
            if currheight >= prevheight:
                s.add((i,j))
                
                dfs(i + 1, j,currheight,s)
                dfs(i - 1, j,currheight,s)
                dfs(i, j + 1,currheight,s)
                dfs(i, j - 1,currheight,s)
        
        for i in range(len(heights)):
            dfs(i,0,0,canreachfrompacific)
            dfs(i,len(heights[i])-1,0,canreachfromatlantic)
        
        for i in range(len(heights[0])):
            dfs(0,i,0,canreachfrompacific)
        for i in range(len(heights[-1])):
            dfs(len(heights) - 1,i,0,canreachfromatlantic)
        
        res = [x for x in (canreachfrompacific & canreachfromatlantic)]
        return res



class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        def checkFromCorner(curr, length):
            row = curr[0]
            col = curr[1]
            #print(curr, length)
            if row not in range(len(matrix)):
                return 0
            if col not in range(len(matrix[0])):
                return 0
            tlength = length
            tcol = col
            #check row
            while tlength >= 0 and tcol >= 0:
                if matrix[row][tcol] != "1":
                    #print("fail check col", row, tcol)
                    return 0
                    
                tcol -= 1
                tlength -= 1
            
            if tlength != -1:
                #print("length check ",tlength, row, tcol)
                return 0
                

            tlength = length
            trow = row
            #check col
            while tlength >= 0 and trow >= 0:
                if matrix[trow][col] != "1":
                    #print("fail check row", row, tcol)
                    return 0
                    
                trow -= 1
                tlength -= 1

            if tlength != -1:
                #print("length check 2",length, row, trow)
                return 0
                

            return 1 + checkFromCorner((row + 1, col + 1), length + 1)

        res = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "1":
                    l = checkFromCorner((row,col),0)
                    res = max(res, l * l)
        return res

                

            


            
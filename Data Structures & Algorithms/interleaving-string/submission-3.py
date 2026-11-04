class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        #so lets say we have a pointer at the begining of each string
        #okay so if one of the pointers matches the large pointer then we want to say we are using that pointer and then move to the next char in to updated pointer and the large one
        #we will also keep track the counts of how many breaks we have from each string
        if len(s1) + len(s2) != len(s3):
            return False
        #s breaks
        sb = [None, 0, 0]

        #char pointers
        p = [None, 0, 0, 0]

        def backtrack():
            #so if all three pointers are at the end then we know it is complete
            if p[1] == len(s1) and p[2] == len(s2) and p[3] == len(s3):
                return True
            if (sb[0],sb[1],sb[2],p[0],p[1],p[2],p[3]) in memo:
                return  memo[(sb[0],sb[1],sb[2],p[0],p[1],p[2],p[3])]
            #now we need to start picking sides
            #if the pointer at 1 is valid and the char can be used in the string then we can update that pointer
            #if it is a new string being used then we need to check if it is valid first
            #we need to update break counter
            v1, v2 = False, False
            if p[1] < len(s1) and s1[p[1]] == s3[p[3]]:
                if sb[0] != 1:
                    if sb[1] == sb[2] - 1 or sb[1] == sb[2]:
                        p[1] += 1
                        p[3] += 1
                        sb[0] = 1
                        sb[1] += 1
                        v1 = backtrack()
                        p[1] -= 1
                        p[3] -= 1
                        sb[0] = 2
                        sb[1] -= 1
                else:
                    p[1] += 1
                    p[3] += 1
                    v1 = backtrack()
                    p[1] -= 1
                    p[3] -= 1
            
            if p[2] < len(s2) and s2[p[2]] == s3[p[3]]:
                if sb[0] != 2:
                    if sb[2] == sb[1] - 1 or sb[2] == sb[1]:
                        p[2] += 1
                        p[3] += 1
                        sb[0] = 2
                        sb[2] += 1
                        v2 = backtrack()
                        p[2] -= 1
                        p[3] -= 1
                        sb[0] = 1
                        sb[2] -= 1
                else:
                    p[2] += 1
                    p[3] += 1
                    v2 = backtrack()
                    p[2] -= 1
                    p[3] -= 1
            memo[(sb[0],sb[1],sb[2],p[0],p[1],p[2],p[3])] = v1 or v2
            return memo[(sb[0],sb[1],sb[2],p[0],p[1],p[2],p[3])]

        return backtrack()



        

            

                


            
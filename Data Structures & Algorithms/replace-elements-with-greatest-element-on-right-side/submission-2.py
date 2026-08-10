class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #so first max is -1
        m = arr[-1]
        #set last num to -1 which is curr max
        arr[-1] = -1
        #iterate backward
        for i in range(len(arr) - 2, -1,-1):
            #save current
            temp = arr[i]
            #update curr with max
            arr[i] = m
            #update max
            m = max(temp, m)
            
            
        return arr
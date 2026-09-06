class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp = {}
        for i in range(len(arr2)):
            mp[arr2[i]] = i

        i = 0
        indexes = set()
        for i in range(len(arr1)):
            m = i
            for j in range(i, len(arr1)):
                val = arr1[j]
                minval = arr1[m]
                
                if mp.get(val, sys.maxsize) < mp.get(minval, sys.maxsize):
                    m = j
            temp = arr1[i]
            arr1[i] = arr1[m]
            arr1[m] = temp

        tosort = [x for x in arr1 if x not in mp]
        tosort.sort()
        for i in range(len(tosort)):
            arr1[-i-1] = tosort[-i-1]
        return arr1

                    


        


            
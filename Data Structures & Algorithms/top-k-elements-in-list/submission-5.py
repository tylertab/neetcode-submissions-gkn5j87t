class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create array of array of nums where index is frequency
        farr = [[]] * (len(nums) + 1)
        #create frequency mapping to keep track 
        fmp = {}
        for n in nums:
            fmp[n] = fmp.get(n, 0) + 1
        for n in fmp:
            farr[fmp[n]] = farr[fmp[n]] + [n]
        a = []
        for i in range(len(farr) - 1, 0, -1):
            l = farr[i]
            print(l)
            for j in range(len(l)):
                a = a + [l[j]]
                if len(a) == k:
                    return a
        
        return a



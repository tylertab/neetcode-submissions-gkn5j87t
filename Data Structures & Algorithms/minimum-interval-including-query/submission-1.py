class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        #checks query for valid query ininterval, pops if found, returns original query index before mutation.
        qinrange = lambda q, i: q in range(i[0], i[1] + 1)
        qlessthanrange = lambda q, i: q < i[0]
        inlength = lambda i: i[1] - i[0] + 1
        def binarysearch(interval):
            l = 0
            r = len(queries) - 1
            while l <= r:
                mid = (l + r) // 2
                val, ind = queries[mid]
                
                if qinrange(val,interval):
                    queries.pop(mid)
                    return ind
                elif qlessthanrange(val,interval):
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
                


        
        n = len(queries)
        out = [-1] * n
        
        #sort intervals by size and queries ascending (n log n + m log m) 
        #save index in queries first before mutating (enumerate) O(n)
        #for each interval binary search query for results inbetween interval until nothing is returned o(nlogn)
        #if something found add interval length to index in output
        #if nothing found move to next sized interval

        for i in range(n):
            queries[i] = (queries[i],i)
        queries.sort()
        intervals.sort(key = inlength)
        for interval in intervals:
            querymatch = binarysearch(interval)
            while querymatch != -1:
                out[querymatch] = inlength(interval)
                querymatch = binarysearch(interval)
            
        return out



    
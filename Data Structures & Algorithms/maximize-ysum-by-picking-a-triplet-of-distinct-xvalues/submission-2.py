class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        #say we use the value of x[i] as a key and the then y[i] is the max value of that key
        #then we can heapify the values adn ensure that each one maps to a unique value in x

        mp = {}
        n = len(x)
        for i in range(n):
            key = x[i]
            val = y[i]
            ind = i
            mp[key] = max(mp.get(key, 0), val)

        values = list(map(lambda x: -x,list(mp.values())))
        heapq.heapify(values)
       

        s = 0
        if values != None:
            for i in range(3):
                if len(values) > 0:
                    s += -heapq.heappop(values)
                else:
                    return -1
        else:
            return -1
        return s
            


            
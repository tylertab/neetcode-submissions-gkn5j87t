class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        #divide matbles into k bags
        #No empty Bags
        #Marbles in bag need to be consecutive
        #beginning and end of stream is weight
        #Return diff between max and minimum scores amongst dfistribution (score is sum of weights)

        #So for each we want to find the k windows with either the highest or smallest weights 
        minheap = []
        maxheap = []

        if k == 1:
            return 0

        for i in range(len(weights) - 1):
            score = weights[i] + weights[i+1]
            if len(minheap) < k - 1:
                heapq.heappush(minheap, score)
            else:
                heapq.heappushpop(minheap, score)
            if len(maxheap) < k - 1:
                heapq.heappush(maxheap, -score)
            else:
                heapq.heappushpop(maxheap,-score)
        maxsum = sum(minheap)
        minsum = -sum(maxheap)

        return maxsum - minsum



        
        #so how do we get the min we need to find a window with ends that add up to a small number 
        #if we get the smallest k + 1 that are consecutive then we can make k -1 groups of self and k with 2
        
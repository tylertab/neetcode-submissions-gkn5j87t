class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #at each person we can either send them to city a or city b as long not more than n people are at each city
        
        n = len(costs) // 2

        memo = {}
        def helper(i, a, b, n):
            if i not in range(len(costs)):
                return 0
            if (a,b,i) in memo:
                return memo[(a,b,i)]
            #option1
            option1 = sys.maxsize
            option2 = sys.maxsize

            if a < n:
                option1 = costs[i][0] + helper(i + 1, a + 1, b, n)
            #option2
            if b < n:
                option2 = costs[i][1] + helper(i + 1, a, b + 1, n)
            m = min(option1, option2)
            memo[(a, b, i)] = m 
            return min(option1, option2)
        
        return helper(0, 0, 0, n)
            

            




class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        #customers[i] is customers that enter then leave at ith minute and 
        #grumpy[i] (min = i) is 1 if owner grumpy
        #not grumpy trick switch grumpy to not grumpy for minutes

        #we know that when grumpy is 0 those customers are alawys going to be satisfied
        #so lets focus on when grumpy is not 0
        #use grumpy minutes as window, keep track of unsatisified customers
        #when unsatisified customers in window is max, that is the window we will use minutes 
        #on and we add those as satisifed customers 

        start = 0 
        satisfied = 0
        unsatisfied = 0
        most_unsatisified_in_a_window = 0
        for i in range(minutes - 1):
            if grumpy[i] == 0:
                satisfied += customers[i]
            if grumpy[i] == 1:
                unsatisfied += customers[i]

        for end in range(minutes - 1, n):
            if grumpy[end] == 0:
                satisfied += customers[end]
            if grumpy[end] == 1:
                unsatisfied += customers[end]
            
            most_unsatisified_in_a_window = max(unsatisfied,most_unsatisified_in_a_window)
            if grumpy[start] == 1:
                unsatisfied -= customers[start]
            start += 1
        return satisfied + most_unsatisified_in_a_window


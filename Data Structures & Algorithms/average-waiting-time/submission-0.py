class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_waiting_time = 0 
        idletime = 0
        for (a,t) in customers:
            if a >= idletime:
                total_waiting_time += t
                idletime = a + t
            else:
                time_to_start = idletime - a 
                total_waiting_time += time_to_start + t
                idletime += t
        return total_waiting_time / len(customers)
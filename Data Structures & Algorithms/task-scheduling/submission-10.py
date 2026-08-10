class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #so what we want to do is always schedule the task is most frequent
        
        cyclecount = 0
        tasksinfo = {}#"task":{"freq":3, "nextcycle":37}
        readytasks = []
        unreadytasks = []

        for task in tasks:
            tasksinfo[task] = tasksinfo.get(task,{"f":0,"nc":0})
            tasksinfo[task]["f"] += 1
        for task in tasksinfo:
            readytasks.append((-tasksinfo[task]["f"], task))
        heapq.heapify(readytasks)

        while len(readytasks) > 0 or len(unreadytasks) > 0:
            if len(readytasks) > 0:
                freq, task = heapq.heappop(readytasks)
                tasksinfo[task]["f"] -= 1
                tasksinfo[task]["nc"] = cyclecount + n
                if tasksinfo[task]["f"] != 0:
                    heapq.heappush(unreadytasks, (tasksinfo[task]["nc"],-tasksinfo[task]["f"], task))

            

            while len(unreadytasks) > 0 and unreadytasks[0][0] <= cyclecount:
                nc, negfreq, task = heapq.heappop(unreadytasks)
                heapq.heappush(readytasks,(negfreq, task))
            

            cyclecount += 1

            
        return cyclecount






            

            



        

                




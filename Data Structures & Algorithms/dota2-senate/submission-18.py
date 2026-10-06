class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)
        count = {"D":0,"R":0}
        while len(queue) > 1:
            curr = queue.popleft()
            if curr == "R":
                if count["D"]== 0:
                    count["R"]+= 1
                    queue.append(curr)
                else:
                    count["D"] -= 1


            elif curr == "D":
                if count["R"] == 0:
                    count["D"] += 1
                    queue.append(curr)
                else:
                    count["R"] -= 1
            if count["D"] > len(queue):
                return "Dire"
            if count["R"] > len(queue):
                return "Radiant"
                
    
        if queue[0] == "R":
            return "Radiant"
        return "Dire"
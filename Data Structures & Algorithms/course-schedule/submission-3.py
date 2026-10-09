class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prn = [0] * numCourses #preReqsNeeded


        #count prereqs needed for each course
        for (a,b) in prerequisites:
            prn[a] += 1
        #make queue with all course that dont need
        queue = deque()
        for i in range(len(prn)):
            if prn[i] == 0:
                queue.append(i)
        #make mapping of prereq to course
        prereqfor = {}
        for (a,b) in prerequisites:
            prereqfor[b] = prereqfor.get(b,[]) + [a]

        while len(queue) > 0:
            curr = queue.popleft()
            for course in prereqfor.get(curr, []):
                prn[course] -= 1
                if prn[course] == 0:
                    queue.append(course)

        #check if all are 0
        for num in prn:
            if num != 0:
                return False
        return True



        

        






            




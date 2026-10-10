class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        #create arr that shows how many prereqs needed for each
        prc = [0] * numCourses

        for (a,b) in prerequisites:
            prc[a] += 1
        #create mp of prereq to course
        unlocks = {}

        for (a,b) in prerequisites:
            unlocks[b] = unlocks.get(b, []) + [a]

        #queue those with 0
        queue = deque()
        
        for i in range(len(prc)):
            if prc[i] == 0:
                queue.append(i)
                res.append(i)
      
        #bfs while updating queue once we can take a course
        while len(queue) > 0:
            curr = queue.popleft()
            for course in unlocks.get(curr,[]):
                prc[course] -= 1
                if prc[course] == 0:
                    res.append(course)
                    queue.append(course)
        
        #check that all course have no prereq
        if len(res) == numCourses:
            return res
        return []

        


        
        
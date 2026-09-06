class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        tup = lambda i: (timestamp[i],username[i],website[i])

        #Okay so for each user we can build there sequence
        #Then from these sequences we can build patterns keeping track of the count of 
        #this pattern for each user
        
        #for each user create a list that had the website visits
        sequences = {}
        for i in range(len(username)):
            sequences[username[i]] = sequences.get(username[i],[]) + [tup(i)]
        #sort by timestamp
        for user in sequences:
            sequences[user].sort()

        patterns = {}
        
        for user in sequences:
            usersequences = sequences[user]
            userpatterns = set()
            i = 0
            while i in range(len(usersequences)):
                j = i + 1
                while j in range(len(usersequences)):
                    k = j + 1
                    while k in range(len(usersequences)):
                        currpattern = (usersequences[i][2],usersequences[j][2],usersequences[k][2])                    
                        userpatterns.add(currpattern)                        
                        k += 1
                    j += 1
                i += 1
            print(user, userpatterns)
            print()
            for pattern in userpatterns:
                patterns[pattern] = patterns.get(pattern, 0) + 1
                # print(pattern, patterns[pattern])
                # print()
        print(patterns)
        print()
        res = []
        for pattern in patterns:
            res.append((patterns[pattern], pattern))
        print(res)
        print()
        res.sort(reverse = True)
        print(res)
        print()
        maxcount = res[0][0]
        res = [x[1] for x in res if x[0] == maxcount]
        print(res)
        print()
        res.sort()
        print (res)
        return [x for x in res[0]]


        
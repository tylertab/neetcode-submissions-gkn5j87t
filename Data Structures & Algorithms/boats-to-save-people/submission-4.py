class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        curronboard = 0
        currweight = 0
        boats = 0
        lightest = 0
        heaviest = len(people) - 1
        while lightest <= heaviest:
            l = people[lightest]
            h = people[heaviest]
            addheavy = currweight + h
            addlight = currweight + l
            if addheavy <= limit:
                heaviest -= 1
                currweight = addheavy
                curronboard += 1
            elif addlight <= limit:
                lightest += 1
                currweight = addlight
                curronboard += 1
            if curronboard == 2:
                curronboard, currweight = 0, 0
                boats += 1
            elif curronboard == 1 and people[lightest] + currweight > limit:
                curronboard, currweight = 0, 0
                boats += 1
            else:
                curronboard, currweight = 0, 0
                boats += 1
                lightest += 1
            

            

        return boats



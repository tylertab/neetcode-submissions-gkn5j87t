class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        for i in range(len(names)):
            names[i] = (heights[i], names[i])
        names.sort(reverse = True)
        for i in range(len(names)):
            names[i] = names[i][1]
        return names
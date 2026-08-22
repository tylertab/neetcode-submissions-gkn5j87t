class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s = set()
        s.add((0,0))
        curr = [0,0]
        for d in path:
            if d == 'N':
                curr[0] += 1
            elif d == 'S':
                curr[0] -= 1
            elif d == 'W':
                curr[1] -= 1
            elif d == 'E':
                curr[1] += 1
            if (curr[0], curr[1]) in s:
                return True
            s.add((curr[0],curr[1]))
        return False
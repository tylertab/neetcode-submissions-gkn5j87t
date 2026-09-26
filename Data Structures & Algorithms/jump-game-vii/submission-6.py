class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        stack = [0]
        visited = set()
        while len(stack) > 0:
            curr = stack.pop(-1)
            while curr in visited and len(stack) > 0:
                curr = stack.pop(-1)
            visited.add(curr)
            if curr == len(s) - 1:
                return True
            for j in range(curr + minJump, min(curr + maxJump, len(s) - 1) + 1):
                if s[j] == '0':
                    stack.append(j)
        return False


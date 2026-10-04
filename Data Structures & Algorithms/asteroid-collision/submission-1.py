class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            if a < 0:
                addtostack = True
                while len(stack) > 0 and stack[-1] > 0:
                    if stack[-1] > abs(a):
                        addtostack = False
                        break
                    elif stack[-1] < abs(a):
                        stack.pop(-1)
                    elif stack[-1] == abs(a):
                        stack.pop(-1)
                        addtostack = False
                        break
                if addtostack:
                    stack.append(a)
        return stack
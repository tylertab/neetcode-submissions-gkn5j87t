class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        while len(out) < numRows:
            out.append([0] * (len(out[-1]) + 1))
            out[-1][0] = 1
            out[-1][-1] = 1
            for i in range(1,len(out[-1]) - 1):
                upleft = out[-2][i - 1]
                upright = out[-2][i]
                out[-1][i] = upleft + upright
        return out


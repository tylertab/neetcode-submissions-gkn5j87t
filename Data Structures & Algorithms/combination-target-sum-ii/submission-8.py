class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        currsum = [0]
        out = []
        currlist = []
        n = len(candidates)
        def backtrack(i):
            if currsum[0] == target:
                out.append(currlist.copy())
                return
            if i == n:
                return
            if currsum[0] + candidates[i] > target:
                return
            #take
            
            currsum[0] += candidates[i]
            currlist.append(candidates[i])
            backtrack(i + 1)
            currsum[0] -= candidates[i]
            currlist.pop(-1)

            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            #skip
            backtrack(i + 1)
        backtrack(0)
        return out



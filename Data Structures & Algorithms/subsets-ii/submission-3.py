class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []
        curr = []
        currfreq = {}
        memo = set()
        def stringifyfreq():

            return ",".join([f'{x[0]},{x[1]}'for x in sorted(list(currfreq.items()))])
        def backtrack(i):
            if stringifyfreq() not in memo:
                out.append(curr.copy())
                memo.add(stringifyfreq())
    
            if i not in range(len(nums)):
                return
            
            curr.append(nums[i])
            currfreq[str(nums[i])] = currfreq.get(str(nums[i]), 0) + 1
            backtrack(i + 1)
            currfreq[str(nums[i])] = currfreq.get(str(nums[i]), 0) - 1
            if currfreq[str(nums[i])] == 0:
                del currfreq[str(nums[i])] 
            curr.pop(-1)
            backtrack(i + 1)

        backtrack(0)

        return out


            
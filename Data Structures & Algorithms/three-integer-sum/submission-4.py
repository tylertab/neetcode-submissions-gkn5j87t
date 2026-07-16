class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cim = {} #map complement to list of 2 pair indexes
        #c -> [[x,y][z,x]] where x + y = c
        #we want to find - c
        for i in range(len(nums)):
            n1 = nums[i]
            for j in range(len(nums)):
                if j == i:
                    continue
                n2 = nums[j]
                c = n1 + n2
                pair = sorted([i, j])
                rpairs = cim.get(c, [])
                if pair not in rpairs:
                    cim[c] = rpairs + [pair]
        ans = []
        for i in range(len(nums)):
            n1 = nums[i]
            if -n1 in cim:
                p = cim[-n1]
                for l in p:
                    if i not in l:
                        trip = sorted(l + [i])
                        if trip not in ans:
                            ans.append(trip)
        nans = []
        for i in range(len(ans)):
            trip = ans[i]
            vtrip = [nums[trip[0]],nums[trip[1]],nums[trip[2]]]
            svtrip = sorted(vtrip)
            if svtrip not in nans:
                nans.append(svtrip)
        return nans
            

            
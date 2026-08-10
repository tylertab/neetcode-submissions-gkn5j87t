class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        #we want to find indices i and j where the values are equal in nums,
        #and the distance between the two is less than or equal to k  

        lastseen = {}
        for i in range(len(nums)):
            if nums[i] not in lastseen:
                lastseen[nums[i]] = i
                continue
            if i - lastseen[nums[i]] <= k:
                return True
            lastseen[nums[i]] = i    
        return False
            
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        heapq.heapify(nums)
        first = heapq.heappop(nums)
        while len(nums) >= 2 and len(res) != 2:
            second = heapq.heappop(nums)
            if first != second:
                res.append(first)
                first = second
            elif first == second:
                first = heapq.heappop(nums)
            

            

        if len(res) != 2:
            res += nums
        if len(res) != 2:
            res += [first]
                
                
        return res

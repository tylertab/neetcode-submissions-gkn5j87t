class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, 0)
        return self.res

    def backtrack(self, perm: List[int], nums: List[int], mask: int):
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return
        for i in range(len(nums)):
            if not (mask & (1 << i)):
                perm.append(nums[i])
                self.backtrack(perm, nums, mask | (1 << i))
                perm.pop()
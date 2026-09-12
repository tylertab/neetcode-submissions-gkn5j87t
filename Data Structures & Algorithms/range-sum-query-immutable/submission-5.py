class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0] * (len(nums))
        s = 0
        for i in range(len(self.sums)):
            s += nums[i]
            self.sums[i] = s



    def sumRange(self, left: int, right: int) -> int:
        sums = self.sums
        preleft = None
        if left == 0:
            preleft = 0
        else:
            preleft = sums[left - 1]
        
        return sums[right] - preleft


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
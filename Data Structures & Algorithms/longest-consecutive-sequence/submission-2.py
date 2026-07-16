class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        m = 0
        print(s)
        for n in nums:
            if n-1 not in s:
                count = 0
                while n in s:
                    print(n, count)
                    count += 1
                    n += 1
                m = max(count, m)
        return m
            



            

            

        
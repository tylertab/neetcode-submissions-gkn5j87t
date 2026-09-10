class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def checkneighbors(i, s, e):
            l = True
            r = True

            if i + 1 in range(s, e + 1):
                r = nums[i] > nums[i + 1]

            if i - 1 in range(s, e + 1):
                l = nums[i] > nums[i - 1]
            
            return (l, r)

        def findpeakhelper(s, e):
            if s > e:
                return None
            mid = (s + e) // 2
            l, r = checkneighbors(mid, s ,e)
            if l and r:
                return mid
            elif l:
                return findpeakhelper(mid + 1,e)
            elif r:
                return findpeakhelper(s, mid - 1) 
            else:
                le = findpeakhelper(s, mid)
                ri = findpeakhelper(mid ,e)
                if le:
                    return le
                return ri

        return findpeakhelper(0, len(nums) - 1)


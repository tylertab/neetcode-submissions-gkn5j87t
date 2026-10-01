class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort intervals
        intervals.sort()
        #iterate through sorted intervals with a last end.
        #if last end is greater then start of next interval
        #add to merge list
        #make curr interval new last merge list entry

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            currend = intervals[i][1]
            lastend = res[-1][1]

            if lastend >= start:
                res[-1][1] = max(currend, lastend)
            else:
                res.append(intervals[i])
        return res
            
        
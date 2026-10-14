class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == []:
            return [newInterval]
        start = None
        end = None
        for i in range(len(intervals)):
            s, e = intervals[i]
            if s in range(newInterval[0], newInterval[1] + 1) or e in range(newInterval[0], newInterval[1] + 1):
                start = i
                break
        for i in range(len(intervals) - 1, -1, -1):
            s, e = intervals[i]
            if s in range(newInterval[0], newInterval[1] + 1) or e in range(newInterval[0], newInterval[1] + 1):
                end = i
                break

        if start != None and end != None:

            intervals = intervals[:start] + [[min(intervals[start][0],newInterval[0]), max(intervals[end][1], newInterval[1])]] + intervals[end + 1:]
        else:

            if intervals[0][0] > newInterval[1]:
                intervals = [newInterval] + intervals
            elif intervals[-1][1] < newInterval[0]:
                intervals = intervals + [newInterval]
            else:
                for i in range(len(intervals) - 1):
                    ns = intervals[i + 1][0]
                    s, e = intervals[i]
                    if ns > newInterval[1] and e < newInterval[0]:
                        intervals.insert(i + 1,newInterval)

        return intervals
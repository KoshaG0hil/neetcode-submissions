class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        count = 0

        for i in intervals[1:]:
            if i[0] >= end:      # NO overlap!
                end = i[1]
            else:                # OVERLAP!
                count += 1

        return count


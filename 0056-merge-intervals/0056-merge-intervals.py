class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals = sorted(intervals, key=lambda t: t[0])
        
        result.append(intervals[0])
        i = 1
        while i < len(intervals):
            c_i, c_j = result[-1]
            tmp_i, tmp_j = intervals[i]

            if c_j >= tmp_i:
                result[-1][1] = max(c_j, tmp_j)
            else:
                result.append(intervals[i])
            i+=1
            
        return result
        
        
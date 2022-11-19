# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        lo, hi = 0, mountain_arr.length() - 1
        while lo < hi:
            mi = (lo + hi) // 2
            if mountain_arr.get(mi) < mountain_arr.get(mi+1):
                lo = mi + 1
            else:
                hi = mi
        if mountain_arr.get(lo) == target:
            return lo
        idx = -1
        i, j = 0, lo
        while i < j:
            mid = (i + j) // 2
            if mountain_arr.get(mid) == target:
                idx = mid if idx == -1 else min(idx, mid)
            if mountain_arr.get(mid) < target:
                i = mid + 1
            else:
                j = mid
        
        i, j = lo, mountain_arr.length()
        while i < j:
            mid = (i + j) // 2
            if mountain_arr.get(mid) == target:
                idx = mid if idx == -1 else min(idx, mid)
            if mountain_arr.get(mid) < target:
                j = mid
            else:
                i = mid + 1
        
        return idx
        
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        result = 0
        i = 0
        while truckSize > 0 and i < len(boxTypes):
            num_box, num_unit = boxTypes[i]
            if num_box >= truckSize:
                result += truckSize * num_unit
                truckSize = 0
            else:
                truckSize -= num_box
                result += num_box * num_unit
            i+=1
                
        return result
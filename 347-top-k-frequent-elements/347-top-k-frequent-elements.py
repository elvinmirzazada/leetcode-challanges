from queue import PriorityQueue

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for item in nums:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1

        p_queue = PriorityQueue()
        for key, v in freq.items():
            p_queue.put((v, str(key)))     

        result = []
        
        for i in range(p_queue.qsize()):
            result.append(p_queue.get()[1])
            
        return result[-k:]
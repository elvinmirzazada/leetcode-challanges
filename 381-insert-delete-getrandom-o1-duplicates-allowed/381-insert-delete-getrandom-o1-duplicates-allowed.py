from collections import defaultdict
from random import choice
class RandomizedCollection:

    def __init__(self):
        self.dict = defaultdict(set)
        self.list = []

    def insert(self, val: int) -> bool:
        self.dict[val].add(len(self.list))
        self.list.append(val)
        return len(self.dict[val]) == 1

    def remove(self, val: int) -> bool:
        
        if self.dict[val]:
            last_el, idx = self.list[-1], self.dict[val].pop()
        
            self.list[idx] = last_el
            self.dict[last_el].add(idx)
            self.dict[last_el].discard(len(self.list)-1)
            self.list.pop()
            return True
        else:
            return False
            
            
            
    def getRandom(self) -> int:
        
        return choice(self.list)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
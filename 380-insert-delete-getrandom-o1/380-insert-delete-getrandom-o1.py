class RandomizedSet:

    def __init__(self):
        self.random_dict = {}

    def insert(self, val: int) -> bool:
        if val in self.random_dict:
            return False
        else:
            self.random_dict[val] = 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.random_dict:
            del self.random_dict[val]
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        from random import randint
        rand_int = randint(0, len(self.random_dict)-1)
        return list(self.random_dict.keys())[rand_int]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.numbers = {i: False for i in range(maxNumbers)}
        self.max_num = maxNumbers

    def get(self) -> int:
        for n in range(self.max_num):
            if not self.numbers[n]:
                self.numbers[n] = True
                return n
        return -1
        

    def check(self, number: int) -> bool:
        return not self.numbers[number]

    def release(self, number: int) -> None:
        
        self.numbers[number] = False
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
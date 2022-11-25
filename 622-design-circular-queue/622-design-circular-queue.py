class MyCircularQueue:

    def __init__(self, k: int):
        self.limit = k
        self.queue = []
        

    def enQueue(self, value: int) -> bool:
        if len(self.queue) < self.limit:
            self.queue.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if len(self.queue) > 0:
            del self.queue[0]
            return True
        return False

    def Front(self) -> int:
        return self.queue[0] if not self.isEmpty() else -1        

    def Rear(self) -> int:
        return self.queue[len(self.queue) - 1] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def isFull(self) -> bool:
        return len(self.queue) == self.limit



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
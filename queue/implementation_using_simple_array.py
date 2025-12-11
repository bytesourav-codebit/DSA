class myQueue:
    def __init__ (self, capacity):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def enqueue(self, x):
        if self.isFull():
            print("Queue is Full")
            return
        self.arr[self.size] = x
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        for i in range(1, self.size):
            self.arr[i - 1] = self.arr[i]
        self.size -= 1

    def getFront(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        return self.arr[0]
    
    def getRear(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        return self.arr[self.size - 1]
    
if __name__ == "__main__":
    queue = myQueue(3)

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Is Empty", queue.isEmpty())

    print("Is Full", queue.isFull())

    print("Front", queue.getFront())

    print("Rear", queue.getRear())

    queue.dequeue()

    print("After dequeue")

    print("Front", queue.getFront())

    print("Rear", queue.getRear())

    print("Is Empty", queue.isEmpty())

    print("Is Full", queue.isFull())
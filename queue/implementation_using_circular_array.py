class myQueue:
    def __init__ (self, cap):
        # Fixed-size array
        self.arr = [0] * cap
        # Index of front element
        self.front = 0
        # Current number of element
        self.size = 0
        # Maximum capacity
        self.capacity = cap

    # Insert an element at the rear
    def enqueue (self, x):
        if self.size == self.capacity:
            print("Queue is full")
            return
        
        rear = (self.front + self.size) % self.capacity
        self.arr[rear] = x
        self.size += 1

    # Remove an element from the front
    def dequeue (self):
        if self.size == 0:
            print("Queue is Empty")
            return
        
        res = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        return res
    
    # Get the front element
    def getFront (self):
        if self.size == 0:
            return -1
        return self.arr[self.front]
    
    # Get the rear element
    def getRear (self):
        if self.size == 0:
            return -1
        
        rear = (self.front + self.size - 1) % self.capacity

        return self.arr[rear]
    
if __name__ == "__main__":
    queue = myQueue(4)

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)

    print("Front: ", queue.getFront())

    print("Rear: ",queue.getRear())

    queue.dequeue()

    print("Front: ", queue.dequeue())

    print("Rear: ",queue.getRear())
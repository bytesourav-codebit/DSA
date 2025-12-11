class Node:
    def __init__ (self, new_data):
        self.data = new_data
        self.next = None

class myQueue:
    def __init__ (self):
        self.front = None
        self.rear = None
        self.currSize = 0

    def isEmpty (self):
        return self.front is None
    
    def enqueue (self, new_data):
        new_node = Node(new_data)
        if self.isEmpty():
            self.front = self.rear = new_node
        
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.currSize += 1

    def dequeue (self):
        if self.isEmpty():
            print("Queue Underflow")
            return -1
        
        removedData = self.front.data
        self.front = self.front.next
        
        if self.front is None:
            self,rear = None

        self.currSize -= 1

        return removedData
    
    def getFront (self):
        if self.isEmpty():
            print("Queue is Empty")
            return -1
        
        return self.front.data
    
    def size(self):
        return self.currSize
    

if __name__ == "__main__":
    queue = myQueue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)

    print("Size of queue:", queue.size())

    queue.dequeue()

    print("Size of queue:", queue.size())

    print("Front: ", queue.getFront())
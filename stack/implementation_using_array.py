
class myStack:
    #constructor
    def __init__(self, cap):
        self.capacity = cap
        self.arr = [0] * self.capacity
        self.top = -1

    #push operation
    def push(self, x):
        if self.top == self.capacity - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.arr[self.top] = x

    #pop operation
    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return -1
        val = self.arr[self.top]
        self.top -= 1
        return val
    
    #peek(or top) operation
    def peek(self):
        if self.top == -1:
            print("Stack Underflow")
            return -1
        return self.arr[self.top]
    
    #Check if stack is Empty
    def isEmpty(self):
        return self.top == -1
    
    #Check if stack is Full
    def isFull(self):
        return self.top == self.capacity - 1
    

if __name__ == "__main__":
    st = myStack(4)

    #pushing elements
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    st.push(5)

    #popping one element
    print("Popped: ", st.pop())

    #Checking top element
    print("Top element: ", st.peek())

    #Checking if stack is empty
    print("Is stack empty: ", "Yes" if st.isEmpty() else "No")

    #Checking if stack is full
    print("Is stack full: ", "Yes" if st.isFull() else "No")

class myStack:
    #Constructor
    def __init__(self):
        self.arr = []

    #Push Operation
    def push(self, x):
        self.arr.append(x)

    #Pop Operation
    def pop(self):
        if not self.arr:
            print("Stack Underflow")
            return -1
        return self.arr.pop()
    
    #Peek Operation
    def peek(self):
        if not self.arr:
            print("Stack is Empty")
            return -1
        return self.arr[-1]
    
    #Check if Stack is Empty
    def isEmpty(self):
        return len(self.arr) == 0
    
    #Current size
    def size(self):
        return len(self.arr)
    
if __name__ == "__main__":
    st = myStack()

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

    #Checking current size
    print("Current size:", st.size())

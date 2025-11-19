
#Create a Constructor
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

#Function to insert a new node at the beginning of the list
def insertAtFront(head, x):
    newNode = Node(x)
    newNode.next = head
    return newNode

#Printing the Linked List
def printList(head):
    curr = head

    while curr is not None:
        print(curr.data, end = " ")
        if curr.next is not None:
            print("->", end = " ")
        curr = curr.next
    print()

if __name__ == "__main__":
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)

    #Insert a new node at the front of the list
    x = 1
    head = insertAtFront(head, x)

    #Print the updated list
    printList(head)
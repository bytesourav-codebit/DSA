
#Construct to create a Node
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

#Function to remove the last node of the list
def deleteHead(head):
    #Check of the list is empty
    if head is None:
        return None
    
    #Move the head pointer to the next node
    head = head.next

    return head

# Print
def printList(head):
    curr = head

    while curr is not None:
        print(curr.val, end = "")
        if curr.next is not None:
            print("->", end = "")
        curr = curr.next 

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(6)
    head.next.next.next = Node(9)
    head.next.next.next.next = Node(2)

    head = deleteHead(head)

    printList(head)

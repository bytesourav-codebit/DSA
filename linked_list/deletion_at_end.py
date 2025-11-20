
# Constructor to create Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Function to delete a node at the end
def removeLastNode(head):
    # Check if the list is empty
    if head is None:
        return None
    
    # If the list has only one element, delete it and return None
    if head.next is None:
        return None
    
    # Find the second last node
    secondLast = head
    while secondLast.next.next is not None:
        secondLast = secondLast.next
    
    # Delete the last node by making the second_last pointer to None
    secondLast.next = None

    return head

# Print
def printList(head):
    curr = head
    while curr is not None:
        print(curr.data, end = "")
        if curr.next is not None:
            print("->", end = "")
        curr = curr.next

if __name__ == "__main__":
    head = Node(3)
    head.next = Node(7)
    head.next.next = Node(2)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(8)
    head.next.next.next.next.next = Node(5)

    head = removeLastNode(head)

    printList(head)


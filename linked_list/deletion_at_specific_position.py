
# Construct to create Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Function to delete node at a specific position
def deleteNode(head, position):
    temp = head
    # Head is to be deleted
    if position == 1:
        head = temp.next
        return head
    
    # Traverse the node before the one to be deleted
    prev = None
    for i in range(1, position):
        prev = temp
        temp = temp.next

    #Delete the node at the position
    prev.next = temp.next

    return head

# Print
def printList(head):
    while head is not None:
        print(f"{head.data} -> ", end = "")
        head = head.next
    print("nullptr")


if __name__ == "__main__":
    head = Node(3)
    head.next = Node(5)
    head.next.next = Node(2)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(4)
    head.next.next.next.next.next = Node(7)

    position = 3

    head = deleteNode(head, position)

    printList(head)
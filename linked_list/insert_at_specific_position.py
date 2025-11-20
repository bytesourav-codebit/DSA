

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def insertPos(head, pos, val):
    if pos < 1:
        return head
    
    #head will change if pos = 1
    if pos == 1:
        newNode = Node(val)
        newNode.next = head
        return newNode
    
    curr = head

    #Traverse to the node just before the new node
    for i in range(1, pos - 1):
        if curr is None:
            return head
        curr = curr.next

    #If position is greater than number of nodes
    if curr is None:
        return head
    
    newNode = Node(val)

    #Update the next pointers
    newNode.next = curr.next
    curr.next = newNode

    return head

def printList(head):
    curr = head
    while curr is not None:
        print(curr.val, end = "")
        if curr.next is not None:
            print("->", end = "")
        curr = curr.next
    print()

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(4)

    #Insert new Node at a specific position
    val, pos = 3, 3
    head = insertPos(head, pos, val)

    printList(head)
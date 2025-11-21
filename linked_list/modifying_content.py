
# Constructor to create Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Count the number of nodes
def countNodes(head):
    count = 0
    curr = head
    
    while curr is not None:
        count += 1
        curr = curr.next
    return count

# Convert the Linked List to an Array
def linkedListToArray(head, arr, n):
    curr = head

    for i in range(n):
        arr[i] = curr.data
        curr = curr.next

# Convert the Array to Linked List
def arrayToLinkedList(arr, head, n):
    curr = head

    for i in range(n):
        curr.data = arr[i]
        curr = curr.next

# Modify the array
def modifyArray(arr, n):
    for i in range(n // 2):
        x = arr[i]
        arr[i] = arr[n - i - 1] - x
        arr[n - i - 1] = x

# Modify the list
def modifyTheList(head):
    if head.next is None:
        return head
    
    # Count number of nodes
    n = countNodes(head)

    # Create an array
    arr = [0] * n

    # Convert Linked List to Array
    linkedListToArray(head, arr, n)

    # Modify the Array
    modifyArray(arr, n)

    # Convert Array back to Linked List
    arrayToLinkedList(arr, head, n)

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
    head = Node(10)
    head.next = Node(4)
    head.next.next = Node(5)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(6)

    head = modifyTheList(head)

    printList(head)
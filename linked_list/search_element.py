
# Constructor to create new node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Function to find if an element exist in a linked list or not
def searchElement(head, key):
    curr = head

    # Iterate over the whole list
    while curr is not None:
        # If the key is found, return true
        if curr.data == key:
            return True
        # Move to the next node
        curr = curr.next
        # If key not found, return false
    return False

if __name__ == "__main__":
    head = Node(3)
    head.next = Node(5)
    head.next.next = Node(2)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(4)
    head.next.next.next.next.next = Node(7)

    key = 3

    if searchElement(head, key):
        print("Element is present")
    else:
        print("Element is not present")
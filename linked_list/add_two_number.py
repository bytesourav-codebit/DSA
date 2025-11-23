# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummyNode = ListNode()   # Dummy head
        res = dummyNode          # Pointer to return the final list

        carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            num = total % 10
            carry = total // 10

            dummyNode.next = ListNode(num)
            dummyNode = dummyNode.next

        return res.next


# Helper function to create a linked list from a Python list
def createLinkedList(arr):
    dummy = ListNode()
    cur = dummy
    for num in arr:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next


# Helper function to print a linked list
def printLinkedList(head):
    cur = head
    result = []
    while cur:
        result.append(str(cur.val))
        cur = cur.next
    print(" -> ".join(result))


# Driver code (main)
if __name__ == "__main__":
    # Example: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    l1 = createLinkedList([2, 4, 3])
    l2 = createLinkedList([5, 6, 4])

    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)

    print("Result:")
    printLinkedList(result)

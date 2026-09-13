
# LINKED LIST PROBLEMS 


# Node of Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Create Linked List 
def createList(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    curr = head

    for value in arr[1:]:
        curr.next = ListNode(value)
        curr = curr.next

    return head


# Print Linked List
def printList(head):
    curr = head

    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next

    print("None")


# Reverse Linked List


def reverseList(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


#  17. Middle of Linked List

def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


#  Linked List Cycle


def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


#  Merge Two Sorted Lists


def mergeTwoLists(list1, list2):
    dummy = ListNode(0)
    curr = dummy

    while list1 and list2:

        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next

        else:
            curr.next = list2
            list2 = list2.next

        curr = curr.next

    # Attach remaining nodes
    if list1:
        curr.next = list1
    else:
        curr.next = list2

    return dummy.next


# Remove Nth Node From End


def removeNthFromEnd(head, n):

    dummy = ListNode(0, head)

    slow = dummy
    fast = dummy

    # Move fast n steps ahead
    for _ in range(n):
        fast = fast.next

    # Move both pointers
    while fast.next:
        slow = slow.next
        fast = fast.next

    # Remove node
    slow.next = slow.next.next

    return dummy.next




if __name__ == "__main__":

   
    print("\n Reverse Linked List")

    head = createList([1, 2, 3, 4, 5])

    print("Original:")
    printList(head)

    head = reverseList(head)

    print("Reversed:")
    printList(head)


    print("\n Middle of Linked List")

    head = createList([1, 2, 3, 4, 5])

    print("Linked List:")
    printList(head)

    middle = middleNode(head)

    print("Middle:", middle.val)


    

    print("\n Linked List Cycle")

    head = createList([1, 2, 3, 4, 5])

    # Create a cycle:
    # 5 -> 3
    node3 = head.next.next
    node5 = head.next.next.next.next

    node5.next = node3

    print("Cycle exists:", hasCycle(head))


   

    print("\n Merge Two Sorted Lists")

    list1 = createList([1, 3, 5])
    list2 = createList([2, 4, 6])

    print("List 1:")
    printList(list1)

    print("List 2:")
    printList(list2)

    merged = mergeTwoLists(list1, list2)

    print("Merged:")
    printList(merged)


    

    print("\n Remove Nth Node From End")

    head = createList([1, 2, 3, 4, 5])

    print("Original:")
    printList(head)

    n = 2

    head = removeNthFromEnd(head, n)

    print("After removing", n, "node from end:")
    printList(head)
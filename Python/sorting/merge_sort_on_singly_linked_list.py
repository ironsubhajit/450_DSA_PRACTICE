class LinkedListNode:
    """Linked list class"""
    def __init__(self, value=0, next=None):
        self.value = value,
        self.next = next


def merge_sort(head):
    if head is None or head.next is None:
        return head

    # Find middle and split the list into two parts
    middle = find_middle(head)
    left_half = head
    right_half = middle.next
    middle.next = None

    # Sort both halves recursively
    left_sorted_list = merge_sort(left_half)
    right_sorted_list = merge_sort(right_half)

    # merging left and right sorted halves
    return merge(left_sorted_list, right_sorted_list)


def find_middle(temp_head):
    """Runner Algorithm: for each move of slow pointer fast pointer will move two moves"""
    slow = temp_head
    fast = temp_head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    # Returning middle node
    return slow


def merge(left, right):
    """Checking two node value and rearrange linking as per the minimum value"""
    result = LinkedListNode()
    current = result

    while left is not None and right is not None:
        # Checking which node value is minimum and link it with current node then update current node
        if left.value < right.value:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next

        current = current.next

    # Checking if any of the halves had any value left
    if left is not None:
        # link remaining left half with current node
        current.next = left
    else:
        # link remaining right half wth current node
        current.next = right

    # returning result next value as head of the sorted list
    return result.next


def print_linked_list(list_head):
    current = list_head
    while current:
        print(current.value, end="-> ")
        current = current.next
    print("None")


head = LinkedListNode(3)
head.next = LinkedListNode(1)
head.next.next = LinkedListNode(4)
head.next.next.next = LinkedListNode(2)
head.next.next.next.next = LinkedListNode(6)

print("Original linked list: ")
print_linked_list(head)

print("Sorted Linked List")
sorted_head = merge_sort(head)
print_linked_list(sorted_head)

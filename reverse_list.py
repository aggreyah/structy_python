from node import *
from linked_list_values import *


def reverse_list(head):
    previous = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous


def reverse_list_recursive(head, previous = None):
    if head is None:
        return previous
    next_node = head.next
    head.next = previous
    return reverse_list_recursive(next_node, head)
    

if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # print(linked_list_values_recursion(a))

    # reverse_list_recursive(a)

    # print("** reversed **")

    print(linked_list_values_recursion(reverse_list_recursive(a)))

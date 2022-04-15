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


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    reverse_list(a)

    # print((reverse_list(a)).value)clear

    print(linked_list_values_recursion(d))

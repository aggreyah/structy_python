from linked_list_values import linked_list_values
from node import *


def insert_node(head, value, index):
    if index == 0:
        value_node = Node(value)
        value_node.next = head
        return value_node

    count = 0
    current = head
    while current is not None:
        if count == index - 1:
            value_node = Node(value)
            temp = current.next
            current.next = value_node
            value_node.next = temp
            break
        current = current.next
        count += 1
    return head


def insert_node_recursive(head, value, index, count = 0):
    if index == 0:
        value_node = Node(value)
        value_node.next = head
        return value_node

    if head is None:
        return  None

    if count == index - 1:
        value_node = Node(value)
        temp = head.next
        head.next = value_node
        value_node.next = temp
        return

    insert_node_recursive(head.next, value, index, count + 1)
    return head


if __name__ == "__main__":
    # a = Node("a")
    # b = Node("b")
    # c = Node("c")
    # d = Node("d")
    #
    # a.next = b
    # b.next = c
    # c.next = d

    # a -> b -> c -> d

    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    # insert_node(a, 'm', 4)
    # a -> b -> c -> d -> m

    print(linked_list_values(insert_node_recursive(a, 'm', 4)))
    # a -> b -> x -> c -> d

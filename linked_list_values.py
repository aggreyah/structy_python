from node import *


def linked_list_values(head):
    nodes_values_list = []
    while head is not None:
        nodes_values_list.append(head.value)
        head = head.next
    return nodes_values_list


def recursive_list_update(head, node_list):
    if head is None:
        return
    node_list.append(head.value)
    recursive_list_update(head.next, node_list)


def linked_list_values_recursion(head):
    nodes_values_list = []
    recursive_list_update(head, nodes_values_list)
    return nodes_values_list


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d
    print(linked_list_values(a))
    print(linked_list_values_recursion(a))

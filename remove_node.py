from linked_list_values import linked_list_values
from node import *


def remove_node(head, target_val):
    if head.value == target_val:
        return head.next

    previous_node = None
    current_node = head
    while current_node is not None:
        if current_node.value == target_val:
            previous_node.next = current_node.next
            break
        else:
            previous_node = current_node
            current_node = current_node.next
    return head


def remove_node_recursive(head, target_val):
    if head is None:
        return None
    if head.value == target_val:
        return head.next
    head.next = remove_node_recursive(head.next, target_val)
    return head


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    # a -> b -> c -> d -> e -> f
    print(linked_list_values(remove_node_recursive(a, "c")))

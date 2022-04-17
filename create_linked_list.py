from linked_list_values import linked_list_values
from node import Node


def create_linked_list(values):
    if not values:
        return None
    dummy = Node(None)
    tail = dummy
    for current in values:
        current_node = Node(current)
        tail.next = current_node
        tail = tail.next
    return dummy.next


def create_linked_list_recursive(values, i=0):
    if i == len(values):
        return None
    head = Node(values[i])
    head.next = create_linked_list_recursive(values, i + 1)
    return head


if __name__ == "__main__":
    print(linked_list_values(create_linked_list_recursive(["a", "b", "c", "d", "e"])))
    # h -> e -> y

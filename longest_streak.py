from node import *


def longest_streak(head):
    maximum_streak = 0
    current_streak = 0
    previous_node_value = None
    current_node = head
    while current_node is not None:
        if current_node.value == previous_node_value:
            current_streak += 1
        else:
            previous_node_value = current_node.value
            current_streak = 1
        if current_streak > maximum_streak:
            maximum_streak = current_streak
        current_node = current_node.next
    return maximum_streak


if __name__ == "__main__":
    a = Node(7)
    b = Node(7)
    c = Node(7)
    d = Node(7)
    e = Node(7)
    f = Node(9)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    print(longest_streak(a))

from linked_list_values import *


def zipper_lists(head_1, head_2):
    tail = head_1
    current_1 = head_1.next
    current_2 = head_2
    count = 0
    while current_1 is not None and current_2 is not None:
        if count % 2 == 0:
            tail.next = current_2
            current_2 = current_2.next
        else:
            tail.next = current_1
            current_1 = current_1.next
        tail = tail.next
        count += 1
    if current_1 is not None:
        tail.next = current_1
    if current_2 is not None:
        tail.next = current_2
    return head_1


def zipper_lists_recursive(head_1, head_2):
    if head_1 is None and head_2 is None:
        return None
    if head_1 is None:
        return head_2
    if head_2 is None:
        return head_1
    next_1 = head_1.next
    next_2 = head_2.next
    head_1.next = head_2
    head_2.next = zipper_lists_recursive(next_1, next_2)
    return head_1


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    x = Node("x")
    y = Node("y")
    z = Node("z")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    x.next = y
    y.next = z

    # a = Node("a")
    # b = Node("b")
    # c = Node("c")
    # a.next = b
    # b.next = c
    # a -> b -> c

    # x = Node("x")
    # y = Node("y")
    # z = Node("z")
    # x.next = y
    # y.next = z
    # x -> y -> z

    print(linked_list_values(zipper_lists_recursive(x, a)))

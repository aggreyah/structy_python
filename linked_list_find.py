from node import *


def linked_list_find(head, target):
    while head is not None:
        if head.value == target:
            return True
        else:
            head = head.next
    return False


def linked_list_find_recursion(head, target):
    if head is None:
        return False
    if head.value == target:
        return True
    return linked_list_find_recursion(head.next, target)


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    print(linked_list_find(a, "d"))
    print(linked_list_find(a, "z"))

    print(linked_list_find_recursion(a, "d"))
    print(linked_list_find_recursion(a, "z"))

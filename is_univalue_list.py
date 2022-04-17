from node import *


def is_univalue_list(head):
    head_value = head.value
    current = head.next
    while current is not None:
        if current.value != head_value:
            return False
        else:
            current = current.next
    return True


def is_univalue_list_recursive(head, prev=None):
    if head is None:
        return True
    if prev is not None and head.value != prev.value:
        return False
    return is_univalue_list_recursive(head.next, head)


if __name__ == "__main__":
    a = Node(7)
    b = Node(7)
    c = Node(8)

    a.next = b
    b.next = c

    # 7 -> 7 -> 4

    print(is_univalue_list(a))

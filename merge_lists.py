from linked_list_values import *


def merge_lists(head_1, head_2):
    dummy = Node(None)
    tail = dummy
    current_1 = head_1
    current_2 = head_2

    while current_1 is not None and current_2 is not None:
        if current_1.value < current_2.value:
            tail.next = current_1
            current_1 = current_1.next
        else:
            tail.next = current_2
            current_2 = current_2.next
        tail = tail.next
    if current_1 is not None:
        tail.next = current_1
    if current_2 is not None:
        tail.next = current_2
    return dummy.next


def merge_lists_recursive(head_1, head_2):
    if head_1 is None and head_2 is None:
        return None
    if head_1 is None:
        return head_2
    if head_2 is None:
        return head_1

    if head_1.value < head_2.value:
        temp = head_1.next
        head_1.next = merge_lists_recursive(temp, head_2)
        return head_1
    else:
        temp = head_2.next
        head_2.next = merge_lists_recursive(head_1, temp)
        return head_2


if __name__ == "__main__":
    a = Node(5)
    b = Node(7)
    c = Node(10)
    d = Node(12)
    e = Node(20)
    f = Node(28)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # 5 -> 7 -> 10 -> 12 -> 20 -> 28

    q = Node(1)
    r = Node(8)
    s = Node(9)
    t = Node(10)
    q.next = r
    r.next = s
    s.next = t
    # 1 -> 8 -> 9 -> 10

    print(linked_list_values(merge_lists_recursive(a, q)))
    # 1 -> 5 -> 7 -> 8 -> 9 -> 10 -> 10 -> 12 -> 20 -> 28

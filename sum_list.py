from node import *


def sum_list(head):
    sum_values = 0
    while head is not None:
        sum_values += head.value
        head = head.next
    return sum_values


def sum_list_recursive(head):
    if head is None:
        return 0
    return head.value + sum_list_recursive(head.next)


if __name__ == "__main__":
    z = Node(100)
    y = Node(45)
    x = Node(89)

    x.next = y
    y.next = z

    # 100

    print(sum_list(x))
    print(sum_list_recursive(x))

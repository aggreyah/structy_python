from linked_list_values import linked_list_values
from node import Node


def add_lists(head_1, head_2):
    current_1 = head_1
    current_2 = head_2
    dummy = Node(None)
    tail = dummy
    carry = 0
    while current_1 is not None and current_2 is not None:
        current_sum = current_1.value + current_2.value + carry
        sum_node = Node(current_sum % 10)
        tail.next = sum_node
        tail = tail.next
        if current_sum >= 10:
            carry = 1
        else:
            carry = 0
        current_1 = current_1.next
        current_2 = current_2.next
    if current_1 is not None:
        while current_1 is not None:
            current_sum_1 = current_1.value + carry
            sum_node = Node(current_sum_1 % 10)
            tail.next = sum_node
            tail = tail.next
            if current_sum_1 >= 10:
                carry = 1
            else:
                carry = 0
            current_1 = current_1.next

    if current_2 is not None:
        while current_2 is not None:
            current_sum_2 = current_2.value + carry
            sum_node = Node(current_sum_2 % 10)
            tail.next = sum_node
            tail = tail.next
            if current_sum_2 >= 10:
                carry = 1
            else:
                carry = 0
            current_2 = current_2.next

    if carry == 1:
        carry_node = Node(carry)
        tail.next = carry_node

    return dummy.next


def add_lists_recursive(head_1, head_2, carry=0):
    if head_1 is None and head_2 is None and carry == 0:
        return None
    head_1_value = head_1.value if head_1 is not None else 0
    head_2_value = head_2.value if head_2 is not None else 0
    node_values_sum = head_1_value + head_2_value + carry
    sum_node = Node(node_values_sum % 10)
    carry = 0 if node_values_sum < 10 else 1
    sum_node.next = add_lists_recursive(head_1.next if head_1 is not None else None,
                                        head_2.next if head_2 is not None else None, carry)
    return sum_node


def add_lists(head_1, head_2):
    if head_1 is None and head_2 is None:
        return None
    result = Node(None)
    carry = 0
    tail = result
    while True:
        head_1_value = 0 if head_1 is None else head_1.value
        head_2_value = 0 if head_2 is None else head_2.value
        node_sum = head_1_value + head_2_value + carry
        sum_node = Node(node_sum % 10)
        carry = 0 if node_sum < 10 else 1
        tail.next = sum_node
        tail = tail.next
        head_1 = head_1.next if head_1 is not None else None
        head_2 = head_2.next if head_2 is not None else None
        if head_1 is None and head_2 is None and carry == 0:
            break
    return result.next


if __name__ == "__main__":
    a1 = Node(9)
    a2 = Node(9)
    a3 = Node(9)
    a1.next = a2
    a2.next = a3
    # 9 -> 9 -> 9

    b1 = Node(8)
    b2 = Node(9)
    b1.next = b2
    # 6

    print(linked_list_values(add_lists_recursive(a1, b1)))

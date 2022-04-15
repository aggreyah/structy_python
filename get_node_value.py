from node import Node


def get_node_value(head, index):
    count = 0
    while head is not None:
        if count == index:
            return head.value
        else:
            count += 1
            head = head.next
    return None


def get_node_value_recursive(head, index):
    if index == 0:
        return head.value
    if head is None:
        return None
    
    return get_node_value_recursive(head.next, index - 1)

        
if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

print(get_node_value(a, 3))
print(get_node_value(a, 7))
print("*** recursive ***")
print(get_node_value(a, 3))
print(get_node_value(a, 7))
print(get_node_value(a, 2))

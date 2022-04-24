from treenode import TreeNode


def depth_first_values(root):
    if root is None:
        return []

    stack = [root]
    result = []
    while stack:
        current_stack_node = stack.pop()
        result.append(current_stack_node.value)
        if current_stack_node.right:
            stack.append(current_stack_node.right)
        if current_stack_node.left:
            stack.append(current_stack_node.left)
    return result


def depth_first_values_recursive(root):
    if root is None:
        return []
    result = [root.value]
    result.extend(depth_first_values_recursive(root.left))
    result.extend(depth_first_values_recursive(root.right))
    return result


if __name__ == "__main__":
    a = TreeNode('a')
    b = TreeNode('b')
    c = TreeNode('c')
    d = TreeNode('d')
    e = TreeNode('e')
    f = TreeNode('f')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f

    print(depth_first_values_recursive(a))
    #   -> ['a', 'b', 'd', 'e', 'c', 'f']

from treenode import TreeNode


def leaf_list(root):
    if root is None:
        return []
    if not root.left and not root.right:
        return [root.value]
    left_list = leaf_list(root.left)
    right_list = leaf_list(root.right)
    return left_list + right_list


def leaf_list_iterative(root):
    if root is None:
        return []
    stack = [root]
    leaves = []
    while stack:
        current = stack.pop()
        if not current.left and not current.right:
            leaves.append(current.value)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return leaves


if __name__ == "__main__":
    a = TreeNode("a")
    b = TreeNode("b")
    c = TreeNode("c")
    d = TreeNode("d")
    e = TreeNode("e")
    f = TreeNode("f")
    g = TreeNode("g")
    h = TreeNode("h")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /       \
    #   g         h

    print(leaf_list_iterative(a))  # -> [ 'd', 'g', 'h' ]

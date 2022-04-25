from treenode import TreeNode


def tree_includes(root, target):
    if root is None:
        return False
    if root.value == target:
        return True
    return tree_includes(root.left, target) or tree_includes(root.right, target)


def tree_includes_iterative(root, target):
    if not root:
        return False
    if root.value == target:
        return True
    stack = [root]
    while stack:
        current = stack.pop()
        if current.value == target:
            return True
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return False


if __name__ == "__main__":
    a = TreeNode("a")
    b = TreeNode("b")
    c = TreeNode("c")
    d = TreeNode("d")
    e = TreeNode("e")
    f = TreeNode("f")

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

    print(tree_includes_iterative(a, "e"))  # -> True

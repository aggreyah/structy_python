from treenode import TreeNode


def path_finder(root, target):
    if _path_finder(root, target):
        return _path_finder(root, target)[::-1]
    else:
        return None


def _path_finder(root, target):
    if root is None:
        return None

    if root.left is None and root.right is None and root.value != target:
        return None

    if root.value == target:
        return [target]

    right_result = _path_finder(root.right, target)
    if right_result:
        right_result.append(root.value)
        return right_result
    left_result = _path_finder(root.left, target)
    if left_result:
        left_result.append(root.value)
        return left_result


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

    print(path_finder(a, "c"))  # -> ['a', 'c']

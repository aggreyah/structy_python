from treenode import TreeNode


def how_high(node):
    if node is None:
        return -1
    left_height = how_high(node.left)
    right_height = how_high(node.right)
    return 1 + max(left_height, right_height)


if __name__ == "__main__":
    a = TreeNode('a')
    b = TreeNode('b')
    c = TreeNode('c')
    d = TreeNode('d')
    e = TreeNode('e')
    f = TreeNode('f')
    g = TreeNode('g')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /
    #   g

    print(how_high(a))  # -> 3

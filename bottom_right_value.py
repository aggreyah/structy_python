from collections import deque

from treenode import TreeNode


def bottom_right_value(root):
    current = None
    queue = deque([root])
    while queue:
        current = queue.pop()
        if current.left:
            queue.appendleft(current.left)
        if current.right:
            queue.appendleft(current.right)
    return current.value


if __name__ == "__main__":
    a = TreeNode(-1)
    b = TreeNode(-6)
    c = TreeNode(-5)
    d = TreeNode(-3)
    e = TreeNode(-4)
    f = TreeNode(-13)
    g = TreeNode(-2)
    h = TreeNode(6)
    i = TreeNode(7)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h
    f.left = i

    #        -1
    #      /   \
    #    -6    -5
    #   /  \     \
    # -3   -4   -13
    #     / \    /
    #    -2  6  7

    print(bottom_right_value(a))  # -> 7

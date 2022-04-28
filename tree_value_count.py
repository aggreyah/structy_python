from collections import deque

from treenode import TreeNode


def tree_value_count(root, target):
    if root is None:
        return 0
    root_match = 1 if root.value == target else 0
    return root_match + tree_value_count(root.right, target) + tree_value_count(root.left, target)


def tree_value_count_iterative(root, target):
    if root is None:
        return 0
    match = 0
    queue = deque([root])
    while queue:
        current = queue.pop()
        if current.value == target:
            match += 1
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return match


if __name__ == "__main__":
    a = TreeNode(7)
    b = TreeNode(5)
    c = TreeNode(1)
    d = TreeNode(1)
    e = TreeNode(8)
    f = TreeNode(7)
    g = TreeNode(1)
    h = TreeNode(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      7
    #    /   \
    #   5     1
    #  / \     \
    # 1   8     7
    #    /       \
    #   1         1

    print(tree_value_count_iterative(a, 1))  # -> 4

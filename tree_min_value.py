import math
from collections import deque

from treenode import TreeNode


def tree_min_value(root):
    if root is None:
        return math.inf
    return min(root.value, tree_min_value(root.left), tree_min_value(root.right))


def tree_min_value_iterative(root):
    queue = deque([root])
    minimum_value = root.value
    while queue:
        current = queue.pop()
        if current.value < minimum_value:
            minimum_value = current.value
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return minimum_value


if __name__ == "__main__":
    a = TreeNode(3)
    b = TreeNode(11)
    c = TreeNode(4)
    d = TreeNode(4)
    e = TreeNode(-2)
    f = TreeNode(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       3
    #    /    \
    #   11     4
    #  / \      \
    # 4   -2     1
    print(tree_min_value_iterative(a))  # -> -2

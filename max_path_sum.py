import math

from treenode import TreeNode


def max_path_sum(root):
    if root is None:
        return -math.inf
    if root.left is None and root.right is None:
        return root.value
    return root.value + max(max_path_sum(root.left), max_path_sum(root.right))


if __name__ == "__main__":
    a = TreeNode(5)
    b = TreeNode(11)
    c = TreeNode(54)
    d = TreeNode(20)
    e = TreeNode(15)
    f = TreeNode(1)
    g = TreeNode(3)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    e.left = f
    e.right = g

    #        5
    #     /    \
    #    11    54
    #  /   \
    # 20   15
    #      / \
    #     1  3

    print(max_path_sum(a))  # -> 59

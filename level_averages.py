from tree_levels import *


def level_averages(root):
    levels = tree_levels(root)
    return [sum(level) / len(level) for level in levels]


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

    print(level_averages(a))  # -> [ 5, 32.5, 17.5, 2 ]

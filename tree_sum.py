from treenode import TreeNode


def tree_sum(root):
    if root is None:
        return 0
    return root.value + tree_sum(root.left) + tree_sum(root.right)


def tree_sum_depth_first(root):
    if root is None:
        return 0
    total_sum = 0
    stack = [root]
    while stack:
        current = stack.pop()
        total_sum += current.value
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return total_sum


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

    print(tree_sum_depth_first(a))  # -> 21

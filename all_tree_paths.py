from treenode import TreeNode


def _all_tree_paths(root):
    if root is None:
        return []
    if not root.left and not root.right:
        return [[root.value]]
    paths = []
    left_sub_paths = _all_tree_paths(root.left)
    for sub_path in left_sub_paths:
        sub_path.append(root.value)
        paths.append(sub_path)
        # paths.append([root.value, *sub_path])
    right_sub_paths = _all_tree_paths(root.right)
    for sub_path in right_sub_paths:
        sub_path.append(root.value)
        paths.append(sub_path)
        # paths.append([root.value, *sub_path])

    return paths


def all_tree_paths(root):
    paths = _all_tree_paths(root)
    for index, path in enumerate(paths):
        paths[index] = path[::-1]
    return paths


if __name__ == "__main__":
    a = TreeNode('a')
    b = TreeNode('b')
    c = TreeNode('c')
    d = TreeNode('d')
    e = TreeNode('e')
    f = TreeNode('f')
    g = TreeNode('g')
    h = TreeNode('h')
    i = TreeNode('i')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h
    f.left = i

    #         a
    #      /    \
    #     b      c
    #   /  \      \
    #  d    e      f
    #      / \    /
    #     g  h   i

    print(all_tree_paths(a))  # ->
    # [
    #   [ 'a', 'b', 'd' ],
    #   [ 'a', 'b', 'e', 'g' ],
    #   [ 'a', 'b', 'e', 'h' ],
    #   [ 'a', 'c', 'f', 'i' ]
    # ]

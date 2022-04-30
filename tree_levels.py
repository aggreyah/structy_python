from collections import deque

from treenode import TreeNode


def tree_levels_breadth_first(root):
    if root is None:
        return []
    levels = []
    queue = deque([(root, 0)])
    while queue:
        current_node, level = queue.pop()
        if level == len(levels):
            levels.append([current_node.value])
        else:
            levels[level].append(current_node.value)

        if current_node.left:
            queue.appendleft((current_node.left, level + 1))
        if current_node.right:
            queue.appendleft((current_node.right, level + 1))
    return levels


def tree_levels_depth_first(root):
    if root is None:
        return []
    levels = []
    stack = [(root, 0)]
    while stack:
        current_node, level = stack.pop()
        if level == len(levels):
            levels.append([current_node.value])
        else:
            levels[level].append(current_node.value)

        if current_node.right:
            stack.append((current_node.right, level + 1))

        if current_node.left:
            stack.append((current_node.left, level + 1))

    return levels


def fill_levels(root, a_list, level=0):
    if root is None:
        return
    if level == len(a_list):
        a_list.append([root.value])
    else:
        a_list[level].append(root.value)
    fill_levels(root.left, a_list, level + 1)
    fill_levels(root.right, a_list, level + 1)
    return a_list


def tree_levels(root):
    if root is None:
        return []
    levels = []
    fill_levels(root, levels, 0)
    return levels


if __name__ == "__main__":
    a = TreeNode('a')
    b = TreeNode('b')
    c = TreeNode('c')
    d = TreeNode('d')
    e = TreeNode('e')
    f = TreeNode('f')

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

    print(tree_levels(a))  # ->
    # [
    #   ['a'],
    #   ['b', 'c'],
    #   ['d', 'e', 'f']
    # ]

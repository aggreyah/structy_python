from treenode import TreeNode
from collections import deque


def breadth_first_values(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        current_node = queue.popleft()
        result.append(current_node.value)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return result


if __name__ == "__main__":
    a = TreeNode('a')
    b = TreeNode('b')
    c = TreeNode('c')
    d = TreeNode('d')
    e = TreeNode('e')
    f = TreeNode('f')
    g = TreeNode('g')
    h = TreeNode('h')

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

    print(breadth_first_values(a))
    #   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

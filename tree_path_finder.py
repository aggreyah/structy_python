from treenode import TreeNode


def path_finder(root, target):
    if _path_finder(root, target):
        return _path_finder(root, target)[::-1]
    else:
        return None


def _path_finder(root, target):
    if root is None:
        return None

    if root.left is None and root.right is None and root.value != target:
        return None

    if root.value == target:
        return [target]

    right_result = _path_finder(root.right, target)
    if right_result:
        right_result.append(root.value)
        return right_result
    left_result = _path_finder(root.left, target)
    if left_result:
        left_result.append(root.value)
        return left_result


if __name__ == "__main__":
    root = TreeNode(0)
    curr = root
    for i in range(1, 19500):
        curr.right = TreeNode(i)
        curr = curr.right

    print(path_finder(root, 16281))

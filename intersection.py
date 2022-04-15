def intersection(a, b):
    a_set = set(a)
    return [ele for ele in b if ele in a_set]


if __name__ == "__main__":
    print(intersection([4, 2, 1, 6], [3, 6, 9, 2, 10]))
    print(intersection([2, 4, 6], [4, 2]))
    print(intersection([4, 2, 1], [1, 2, 4, 6]))
    print(intersection([0, 1, 2], [10, 11]))
    list1 = [i for i in range(0, 50000)]
    list2 = [i for i in range(0, 50000)]
    print(intersection(list1, list2))

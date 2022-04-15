def pair_product(numbers, target_product):
    previous = {}
    for i in range(len(numbers)):
        quotient = target_product / numbers[i]
        if quotient not in previous.keys():
            previous[numbers[i]] = i
        else:
            return previous[quotient], i


if __name__ == "__main__":
    print(pair_product([3, 2, 5, 4, 1], 8))
    print(pair_product([3, 2, 5, 4, 1], 10))
    print(pair_product([4, 7, 9, 2, 5, 1], 5))
    print(pair_product([4, 7, 9, 2, 5, 1], 35))
    print(pair_product([3, 2, 5, 4, 1], 10))
    print(pair_product([4, 6, 8, 2], 16))

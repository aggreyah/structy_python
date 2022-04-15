def pair_sum(numbers, target_sum):
    # create a dictionary of previous seen numbers in the list and their indices as values
    previous = {}
    for i in range(len(numbers)):
        compliment = target_sum - numbers[i]
        # if compliment already in dictionary, return its value plus current index else add current element & index
        # to dictionary.
        if compliment in previous.keys():
            return previous[compliment], i
        else:
            previous[numbers[i]] = i


if __name__ == "__main__":
    print(pair_sum([3, 2, 5, 4, 1], 8))
    print(pair_sum([4, 7, 9, 2, 5, 1], 5))
    print(pair_sum([4, 7, 9, 2, 5, 1], 3))
    print(pair_sum([1, 6, 7, 2], 13))
    print(pair_sum([9, 9], 18))
    print(pair_sum([6, 4, 2, 8], 12))

def swap(i, j, nums):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def five_sort(nums):
    i = 0
    j = len(nums) - 1
    while i <= j:
        if nums[j] == 5:
            if nums[i] != 5:
                i += 1
            j -= 1
        else:
            if nums[i] == 5:
                swap(i, j, nums)
                j -= 1
            i += 1
    return nums


if __name__ == "__main__":
    print(five_sort([12, 5, 1, 5, 12, 7]))
    print(five_sort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]))
    print(five_sort([5, 5, 5, 1, 1, 1, 4]))
    print(five_sort([5, 5, 6, 5, 5, 5, 5]))
    print(five_sort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]))

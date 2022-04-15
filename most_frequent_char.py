def char_count(s):
    count = {}
    for item in s:
        if item not in count.keys():
            count[item] = 0
        count[item] += 1
    return count


def most_frequent_char(s):
    count = char_count(s)
    most_frequent = None
    for item in s:
        if most_frequent is None or count[item] > count[most_frequent]:
            most_frequent = item
    return most_frequent


if __name__ == "__main__":
    print(most_frequent_char("bookeeper"))
    print(most_frequent_char("david"))
    print(most_frequent_char("abby"))
    print(most_frequent_char("mississippi"))
    print(most_frequent_char("potato"))
    print(most_frequent_char("eleventennine"))
    print(most_frequent_char("riverbed"))

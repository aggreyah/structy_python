def compress(s):
    result = ""

    i = 0
    j = 0

    while i < len(s) and j < len(s):
        count = 0
        if s[i] == s[j]:
            j += 1
            if j == len(s):
                count = j - i
                if count == 1:
                    result += f"{s[i]}"
                else:
                    result += f"{count}{s[i]}"
        else:
            count = j - i
            if count == 1:
                result += f"{s[i]}"
            else:
                result += f"{count}{s[i]}"
            i = j
    return result


if __name__ == "__main__":
    print(compress("ccaaatsss"))
    print(compress('nnneeeeeeeeeeeezz'))
    print(compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'))

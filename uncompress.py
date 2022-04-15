def uncompress(s):
    numbers = "0123456789"
    result = ""
    i = 0
    j = i + 1
    while i < len(s) and j < len(s):
        if not s[j:j + 1] in numbers:
            num = int(s[i:j])
            result += s[j:j + 1] * num
            i = j + 1
            j = i + 1
        else:
            j += 1
    return result


if __name__ == "__main__":
    print(uncompress("3n12e2z"))

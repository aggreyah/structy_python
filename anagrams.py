def anagrams(string_1, string_2):
    return char_count(string_1) == char_count(string_2)


def char_count(s):
    count = {}
    for item in s:
        if item not in count.keys():
            count[item] = 0
        count[item] += 1
    return count


if __name__ == "__main__":
    print(anagrams('restful', 'fluster'))
    print(anagrams('cats', 'tocs'))
    print(anagrams('monkeyswrite', 'newyorktimes'))
    print(anagrams('paper', 'reapa'))
    print(anagrams('elbow', 'below'))
    print(anagrams('tax', 'taxi'))
    print(anagrams('taxi', 'tax'))
    print(anagrams('night', 'thing'))
    print(anagrams('abbc', 'aabc'))

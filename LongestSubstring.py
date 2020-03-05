def LongestString():
    dict = {}
    str = 'pwwkew'
    max_substr_length = 0
    max_substr = ''
    print(str == max_substr)
    if len(str)<1:
        return 0
    else:
        for index, letter in enumerate(str):
            if letter not in max_substr:
                print(letter)
                max_substr = max_substr+letter
                print(max_substr)
                max_substr_length = len(max_substr)
                print(max_substr_length)
                dict[max_substr] = dict.get(max_substr, max_substr_length)
            elif letter in max_substr:
                dict[max_substr] = dict.get(max_substr, max_substr_length)
                max_substr = letter
                max_substr_length = 1
    print(dict)
    print(max(dict.values(), default=0))




def BestSolution1(s):
    string_list = []
    max_length = 0
    for letter in s:
        if letter in string_list:
            string_list = string_list[string_list.index(letter)+1:]
        string_list.append(letter)
        max_length = max(max_length, len(string_list))

    return len(string_list)

def BestSolution2(s):
    dicts = {}
    maxlength = start = 0
    for i, value in enumerate(s):
        if value in dicts:
            sums = dicts[value] + 1
            if sums > start:
                start = sums
        num = i - start + 1
        if num > maxlength:
            maxlength = num
        dicts[value] = i
    print(dicts)
    return maxlength

BestSolution2('dvdf')